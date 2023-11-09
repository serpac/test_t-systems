from fastapi import FastAPI
from app.url import router
from fastapi.testclient import TestClient

# from app.app_test import test_router
import uvicorn

app = FastAPI()
# client = TestClient(app=app)

app.include_router(router)
# app.include_router(test_router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)