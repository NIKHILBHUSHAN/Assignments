import json

api_response='''
{
    "status":"success",
    "data":{
        "user_id":101,
        "username":"alex999",
        "score":87.5
    }
}'''
data=json.loads(api_response)
print(data["data"]["username"])
print(data["data"]["score"])
print(f"User{data['data']["username"]} scored {data['data']["score"]} points")