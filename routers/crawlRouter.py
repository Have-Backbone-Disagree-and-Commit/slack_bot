from fastapi import APIRouter
router = APIRouter()
import json
import httpx
import slack

key = "key"
client = slack.WebClient(token = key)

@router.get("/get_test", tags=["slack"])
async def get_test():
    client = slack.WebClient(token = key)
    client.chat_postMessage(channel="#playground", text="GET test")
    return "get_test"

@router.get("/get_test/{id}", tags=["slack"])
async def get_test(id: int):
    return id

@router.post("/crawl_data", tags=["slack"])
async def elastic(data : dict):
    jsondata = json.dumps(data, indent = 4)
    jsondata = json.loads(jsondata)
        
    for key in jsondata:
        obj = jsondata[key]
        
        title = obj["title"]
        location = obj["location"]
        position = obj["position"]
        description = obj["description"]
        sitename = obj["sitename"]
        posturl = obj["url"]
        
        if title == "":
            title = "There is no title data."
        if location == "":
            location = "There is no location data."
        if position == "":
            position = "There is no position data."
        if description == "":
            description = "There is no description data."
        if sitename == "":
            sitename = "There is no sitenmae data."
        if posturl == "":
            posturl = "There is no posturl data."
            
        print(obj)
        #headers = {'Content-Type': 'application/json'}
        #response = httpx.post("http://localhost:8003/ics_gen", data=obj)
        
        #fileUrl = "http://localhost:8003/" + response.text[16:]
        #if response == "./generatedFiles/noname.ics":
        #    fileUrl = "http://localhost:8003/nofile.html"
            
        #fileUrl = str(response.text) 
        #title, location, position, description = "none","none","none","none"
        
        blocks = [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*채용공고가 올라왔습니다!*"
				}
			},
			{
				"type": "divider"
			},
            {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*" + sitename + "*"
				}
			},
            {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": title
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": posturl
				}
			},
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": location,
				}
			},
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": position,
				}
			},
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": description,
				}
			},
			{
				"type": "divider"
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "📅   캘린더에 추가하기"
				},
				"accessory": {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Add to Calendar",
					},
					"value": "calendar_add_btn",
					"url": "https://naver.com",
					"action_id": "button-action"
				}
			}
        ]
        
        
        #print("\r\n response : " + response.text)
        #if response.text :
        client.chat_postMessage(channel="#playground", text="text", blocks=blocks)
    
    print("\r\nok\r\n")
    return "ok"

@router.get("/get_test/{id}", tags=["slack"])
async def get_test(id: int):
    return id

@router.get("/get_test/{id}", tags=["slack"])
async def get_test(id: int):
    return id

