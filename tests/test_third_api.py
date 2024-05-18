# Author:
# created_time:
import requests
import json

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer app-sH92UTScnJGS5rR4hViuGmkA'
}
data = {
    "user": "宇将军",
    "inputs": {
        "user_text": "传递的中文"
    }
}
response = requests.post('https://api.dify.ai/v1/workflows/run',
                         headers=headers, data=json.dumps(data))
print(response.text)
