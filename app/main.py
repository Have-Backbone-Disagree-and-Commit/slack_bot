from ..lib.fastapi import FastAPI
from .routers import crawlRouter
from ..lib.mangum import Mangum

app = FastAPI()
app.include_router(crawlRouter.router)
handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "helloworld!"}