import base64
import io
from minio import Minio
from .Iservice import MainServiceInterface
from starlette.responses import Response
from minio_settings.settings import MINIO_HOST, MINIO_ROOT_PASSWORD, MINIO_ROOT_USER


class MainService(MainServiceInterface ):

    def __init__(self):

        self.client = Minio(MINIO_HOST, MINIO_ROOT_USER, MINIO_ROOT_PASSWORD, secure=False)

        

    def load_file(self, bucket_name: str, object_name:str, file: bytes):
        try:
            if  self.client.bucket_exists(bucket_name=bucket_name):
                file_dec = base64.b64decode(file)
                length_file = len(file_dec)
                file_io = io.BytesIO(file_dec)
                self.client.put_object(bucket_name=bucket_name, object_name=object_name, data=file_io, length=length_file)
                return {"bucket_name":bucket_name, "object_name":object_name, "file":file}
            else:
                self.client.make_bucket(bucket_name=bucket_name)
                file_dec = base64.b64decode(file)
                length_file = len(file_dec)
                file_io = io.BytesIO(file_dec)
                self.client.put_object(bucket_name=bucket_name, object_name=object_name, data=file_io, length=length_file)
                return {"bucket_name":bucket_name, "object_name":object_name, "file":file}


        except Exception as e :
            print(e)
            return Response(f"Internal server error", status_code=500)

    def get_file(self, bucket_name: str, object_name: str):
        try:
            if  self.client.bucket_exists(bucket_name):
                response = self.client.get_object(bucket_name=bucket_name, object_name=object_name)
                content = response.read()
                content_base64 = base64.b64encode(content).decode("utf-8")
                return content_base64
            else:
                return Response("Bucket not found", status_code=404)
        except Exception as e:
            print(e)
            return Response("Internal server error", status_code=500)
