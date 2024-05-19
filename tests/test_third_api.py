# Author:
# created_time:
import json

import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer app-sH92UTScnJGS5rR4hViuGmkA'
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
                     "定撒空间领奖斯大林攻击速度捷安高科"
                     "仨就够了关了点水打散卡里古拉拿到了"
                     "赶紧撒高楼大厦开关机达萨罗概括吉安"
                     "巨联看过了卡孤苦伶仃结案率会计估计"
                     "亏大了口干苦巨安大厦葛拉卡达价格感"
                     "觉东大时刻超话地理课刚到家了卡死华"
                     "东卡流口水的感觉固拉多挂灯笼挂到两"
                     "个过来打龙吗打开了国际服大力国际服"
                     "管理会计艾迪康公积金大概可骄傲的双"
                     "联开关过奖啦开个房间卡单联开关巨安"
                     "大厦兰考卡德加固拉多健康管理科复读"
                     "机安哥拉大姐夫葛拉卡达赶紧打算了嘎"
                     "吉噶两个就溜达结束了管理会计艾赛杜拉"
    }
}
response = requests.post('https://api.dify.ai/v1/workflows/run',
                         headers=headers, data=json.dumps(data))
print(response.text)
