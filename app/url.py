from fastapi import APIRouter
from pydantic import BaseModel, field_validator
import base64
from .Iservice import *
from .service import MainService

router = APIRouter()



class Item(BaseModel):
    bucket_name: str
    object_name: str
    file : bytes

    @field_validator("file")
    def validate_base64_data(cls, value):
        try:
            decoded_data = base64.b64decode(value)
            return value
        except Exception as e:
            raise ValueError("Invalid Base64 data")


@router.post("/items/", )
def create_item(input: Item):
    main_service = MainService()
    return main_service.load_file(bucket_name=input.object_name, object_name=input.object_name, file=input.file)
    

@router.get("/items/", )
def create_item(object_name: str, bucket_name: str):
    main_service = MainService()
    return main_service.get_file(bucket_name=bucket_name, object_name=object_name)
