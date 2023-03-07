from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from mangum import Mangum

app = FastAPI(default_response_class=UJSONResponse)

@app.get("/get")
async def get():
    return {"message": "OK"}

handler = Mangum(app)