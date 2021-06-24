from typing import Optional
from fastapi import FastAPI

API_VERSION = os.environ.get("API_VERSION")
API_ENVIRON = os.environ.get("API_ENVIRON", "dev")

app = FastAPI()

@app.get("/")
def index():
    return {
        "success": True,
        "version": API_VERSION,
        "environ": API_ENVIRON
    }

