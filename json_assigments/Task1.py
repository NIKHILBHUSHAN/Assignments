import json

userprofile={
    "name":"Yeddu Nikhil Bhushan",
    "age":18,
    "Email":"xxxxxx@gmail.com",
    "is_actice":True

}
user=json.dumps(userprofile,indent=2)
print(user)