from fastapi import APIRouter
router = APIRouter()
import slack
import os
# for slack bot token
from dotenv import load_dotenv
load_dotenv()
key = os.environ.get('BOT_TOKEN')


@router.get("/get_test", tags=["slack"])
async def get_test():
    client = slack.WebClient(token = key)
    client.chat_postMessage(channel="#playground", text="GET test")
    return "get_test"

@router.get("/get_test/{id}", tags=["slack"])
async def get_test(id: int):
    return id

