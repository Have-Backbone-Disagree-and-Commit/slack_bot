from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/get")
async def get():
    return {"message": "OK"}

handler = Mangum(app)