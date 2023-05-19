# Lambda를 활용한 FastAPI 애플리케이션, Github, CodePipeline, CodeBuild를 활용한 CI/CD, Amazon EventBridge와 Lambda를 활용한 Pipeline 상태감지와 Slack전송

# 1. Lambda function 생성

1. CI/CD 파이프라인 구성을 위한 backbone Lambda 생성
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled.png)
    

# 2. Github을 활용하여 Source 지정

1. CodeBuild의 소스로 지정할 깃허브 레포지토리 생성
    - https://github.com/Have-Backbone-Disagree-and-Commit/slack_bot
    - AWS Cloud Bootcamp Organization Repository로 생성
2. 레포지토리 clone 후 Lambda 생성을위한 최소한의 Test Code 작성
    
    ```python
    def lambda_handler(event, context):
        print("hello world")
    ```
    
3. 파이썬 Dependencies를 위한 requirements.txt 작성
    
    ```
    fastapi
    ```
    
4. Codebuild를 위한 buildspec.yaml 작성
    
    ```yaml
    version: 0.2
    phases:
      install:
        runtime-versions:
          python: 3.9
        commands:
          - echo "Installing dependencies..."
    			# requirements.txt에 명시된 디펜던시를 lib디렉토리에 설치
          - pip install -r requirements.txt -t lib
      build:
        commands:
    			# 디펜던시 패키지(lib)을 압축
          - echo "Zipping deployment package..."
          - cd lib
          - zip -r9 ../deployment_package.zip .
          - cd ..
          - zip -g deployment_package.zip lambda_function.py
      post_build:
        commands:
    			# aws cli를 활용하여 lambda function 업로드
          - echo "Updating lambda Function..."
          - aws lambda update-function-code --function-name Slackbot-FastAPI --zip-file fileb://deployment_package.zip
          - echo "DONE!!"
    ```
    
5. CodePipeline 을 위한 Build Project(Code Build)생성
    - Create build project
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%201.png)
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%202.png)
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%203.png)
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%204.png)
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%205.png)
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%206.png)
    
6. Service Role 설정 (CodeBuild에 붙어있는 IAM Policy 편집)
    
    IAM Policy 편집
    
    ```json
    {
        "Effect": "Allow",
        "Action": [
            "lambda:AddPermission",
            "lambda:RemovePermission",
            "lambda:CreateAlias",
            "lambda:UpdateAlias",
            "lambda:DeleteAlias",
            "lambda:UpdateFunctionCode",
            "lambda:UpdateFunctionConfiguration",
            "lambda:PutFunctionConcurrency",
            "lambda:DeleteFunctionConcurrency",
            "lambda:PublishVersion"
        ],
        "Resource": "arn:aws:lambda:us-east-1:your-aws-account-number:function:your-lambda-function-name"
    }
    ```
    

# 3. CodeBuild를 통한 빌드 테스트

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%207.png)

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%208.png)

# 4. Lambda 확인 및 테스트

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%209.png)

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2010.png)

# 5. CodePipeline 생성 및 동작 확인

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2011.png)

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2012.png)

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2013.png)

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2014.png)

![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2015.png)

### 앞으로 Github를 통한 push 및 merge 요청으로 자동으로 Lambda에 배포됨

# 6. Lambda 환경설정 및 FastAPI 환경 구축

- Runtime 세팅 변경 (main.py의 handler function을 사용할 것이므로)
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2016.png)
    
- Mangum을 활용하여 FastAPI 환경 구축
    
    ```python
    from fastapi import FastAPI
    from mangum import Mangum
    import json
    import httpx
    
    app = FastAPI()
    handler = Mangum(app)
    
    @app.get("/")
    async def root():
        return {"message": "helloworld!"}
    ```
    
    ```
    fastapi
    uvicorn
    mangum
    ```
    
    ```yaml
    version: 0.2
    phases:
      install:
        runtime-versions:
          python: 3.9
        commands:
          - echo "Installing dependencies..."
          - pip install -t lib -r requirements.txt
      build:
        commands:
          - echo "Zipping deployment package..."
          - cd lib
          - zip -r9 ../deployment_package.zip .
          - cd ..
          - zip -g deployment_package.zip main.py
      post_build:
        commands:
          - echo "Updating lambda Function..."
          - aws lambda update-function-code --function-name Slackbot-FastAPI-Lambda --zip-file fileb://deployment_package.zip
          - echo "DONE!!"
    ```
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2017.png)
    
- Lambda test 진행
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2018.png)
    

# 7. 기존의 FastAPI앱 마이그레이션

### Get Test function 동작시켜보기

- Systems Manager의 Parameter Store를 활용한 키 숨김처리
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2019.png)
    
- SSM을 활용하여 Parameter Store의 밸류를 처리
    
    ```python
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
        return "get_test"
    ```
    
- Lambda의 Role에 SSM의 파라미터를 참조 할 수 있는 정책을 추가
    
    ([ERROR] ClientError: An error occurred (AccessDeniedException) when calling the GetParameter operation: User: arn:aws:sts::userid:assumed-role/Slackbot-FastAPI-Lambda-role-suc778in/Slackbot-FastAPI-Lambda is not authorized to perform: ssm:GetParameter on resource: arn:aws:ssm:ap-northeast-2:userid:parameter/slackapi/BOT_TOKEN because no identity-based policy allows the ssm:GetParameter action)
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2020.png)
    
- get test 성공
    
    ![Untitled](Lambda%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20FastAPI%20%E1%84%8B%E1%85%A2%E1%84%91%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%84%8F%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB,%20Github%20f4f1fe30f5674d80936378f7dc8c4aba/Untitled%2021.png)
    

# 8. CodePipeline 상태를 슬랙에 출력하는 Lambda function 작성

- 런타임 환경작성
    - Runtime : Node.js 12.x
    - Handler : index.handler
    - Configuration { Key : Value }
        - CHANNEL : #91-devops
        - SERVICES :/services/T04GZFUND7H/B04SQP3V5DH/wbClZZRFuK6sk7FXSTedy7Fl
