from fastapi import FastAPI
from mangum import Mangum
import json
import httpx
import slack

key = "key"
client = slack.WebClient(token = key)


app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root():
    return {"message": "helloworld!"}

@app.get("/slack_test")
async def slack_test():
    client = slack.WebClient(token = key)
    client.chat_postMessage(channel="#playground", text="GET test")
    return "get_test"