from fastapi.testclient import TestClient
from main import app  
import json

client = TestClient(app)

def test_post_file():
    response = client.post("/items", data=json.dumps({"bucket_name":"bucket_test", "object_name":"bucket_test", "file":"YnVlbm9zIGRpYXMK"}))
    if response.status_code==200:
        response = json.loads(response.text)
        assert response == {"bucket_name":"bucket_test", "object_name":"bucket_tests", "file":"YnVlbm9zIGRpYXMK"}

def test_get_file():
    response = client.get("/items", params={"bucket_name":"bucket_test", "object_name":"bucket_tests"})
    print(response.status_code)
    if response.status_code==200:
        response = json.loads(response.text)
        assert response == {"file":"YnVlbm9zIGRpYXMK"}