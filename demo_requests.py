import requests
import json

# 无参数get请求
# url = 'http://httpbin.org/get'
# res = requests.get(url)
# print(res.text)

# 有参数get请求，url
# url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好"
# res = requests.get(url = url)
# print(res.text)

# 有参数get请求，params
# url = "http://www.tuling123.com/openapi/api"
# params = {"key":"ec961279f453459b9248f0aeb6600bbe","info":"你好"}
# res = requests.get(url = url, params = params)
# print(res.text)

# post请求，data为字典
# url = "http://httpbin.org/post"
# data = {"name": "hanzhichao", "age": 18}
# res = requests.post(url = url, data = data)
# print(res.text)

# post请求，data为json
# url = "http://httpbin.org/post"
# data1 = '{"name": "hanzhichao", "age": 18}'
# data2 = '''{
#     "name": "hanzhichao",
#     "age": 18
#     }'''
# res1 = requests.post(url = url, data = data1)
# res2 = requests.post(url = url, data = data2)
# print(res1.text)
# print(res2.text)
# print(res1.text == res2.text)

# post请求，字典转json
# url = "http://httpbin.org/post"
# data = {
#         "name": "hanzhichao",
#         "age": 18
#         }
# headers = {"Content-Type":"application/json"}
# res1 = requests.post(url=url, data=json.dumps(data), headers=headers)
# res2 = requests.post(url=url, json=data)
# print(res1.text)
# print(res2.text)
# print(res1.text == res2.text)


# 练习1，
# 利用图灵聊天接口（GET） http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好，
# 结合Python的input编写一个机器人聊天室
# url_p1 = "http://www.tuling123.com/openapi/api"
# while True:
#     info = input("say something: ")
#     if info == "退出":
#         break
#     params = {"key":"ec961279f453459b9248f0aeb6600bbe", "info": info}
#     res_p1 = requests.get(url=url_p1, params=params)
#     print(res_p1.json().get("text"))

# 练习2，
# 利用图灵查询接口（POST）http://openapi.tuling123.com/openapi/api/v2，
# 封装一个实用的查询方法，查询你附近的美食等等

url_p2 = "http://openapi.tuling123.com/openapi/api/v2"
while True:
    text = input("what to search: ")
    if text == "退出":
        break
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": text
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": "ec961279f453459b9248f0aeb6600bbe",
            "userId": "206379"
        }
    }
    res_p2 = requests.post(url=url_p2, json=data)
    res_dict = res_p2.json()
    # print(res_dict)
    # print(json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False))
        # indent: 缩进空格数，indent=0输出为一行
        # sork_keys=True: 将json结果的key按ascii码排序
        # ensure_ascii=Fasle: 不确保ascii码，如果返回格式为utf-8包含中文，不转化为\u…
    for result in res_dict.get("results"):
        values = result.get("values")
        for v in values:
            print(values.get(v))

