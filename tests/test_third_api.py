# Author:
# created_time:
import json

import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '
}
data = {
    "user": "宇将军",
    "response_mode": "streaming",
    "inputs": {
        "user_text": "早早早早早早早早早早早早东风街"
                     "道事件流看电视剧了法兰卡丹仨绝地反"
                     "击第十六课防控力度数据库的法兰卡丹"
                     "神将世界法兰卡丹刷卡积分家法律手段"
                     "福建省东街道港口肯定是绝对对方拉开"
                     "距离肯定是网卡了撒的感觉倒过来看王"
                     "俊凯的说了啥都说了刚打上来管理局肯"
    }
}
response = requests.post('http://localhost:5001/completion-messages',
                         headers=headers, data=json.dumps(data))
print(response.text)
