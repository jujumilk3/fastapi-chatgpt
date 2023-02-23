# fastapi-chatgpt

## Deployment
```dotenv
# .env
# choose one of the following to login to openai
# 1
OPENAPI_ACCOUNT=<OPENAPI-ACCOUNT>
OPENAPI_PASSWORD=<OPENAPI-PASSWORD>

# 2
OPENAPI_SESSION_TOKEN=<YOUR-SESSION-TOKEN>

# 3
OPENAPI_ACCESS_TOKEN=<YOUR-ACCESS-TOKEN>

```
### command
`docker build -t fastapi-chatgpt .`  or   
`docker pull jujumilk3/fastapi-chatgpt`

`docker run -d -p 8000:8000 --env-file .env fastapi-chatgpt` or  
`docker run -d -p 8000:8000 --env-file .env jujumilk3/fastapi-chatgpt`

## Reference
1. https://github.com/acheong08/ChatGPT
