from fastapi import FastAPI
from mangum import Mangum
import json
import httpx
import slack
import boto3

ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name='/slackapi/BOT_TOKEN', WithDecryption=False)
key = parameter['Parameter']['Value']
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
    return "get_test with lambda function (FastAPI Runtime)"

@app.post("/crawl_data")
async def crawl_data():
    client = slack.WebClient(token = key)
    client.chat_postMessage(channel="#playground", text="GET test")
    return "get_test with lambda function (FastAPI Runtime)"