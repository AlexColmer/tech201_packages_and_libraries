import requests
import json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(post_codes_req)  # <Response [200]>
#
# print(post_codes_req.status_code)  # 200
#
# print(post_codes_req.headers)  # http headers returned
#
# print(post_codes_req.content)  # raw content
#
# print(post_codes_req.json())  # json content
#
# print(type(post_codes_req.json()))  # <'class dict'>

json_body = json.dumps({"postcodes": ["PR8 OSG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
print(post_multi_req.json())