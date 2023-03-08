from fastapi import FastAPI
from .routers import crawlRouter
from mangum import Mangum

app = FastAPI()
app.include_router(crawlRouter.router)
handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "helloworld!"}