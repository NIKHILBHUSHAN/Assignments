import json
json_data='''
{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}
'''
data=json.loads(json_data)

print(data["address"]["city"])
print(data["address"]["zip"])

data["address"]["country"]="India"
updates_json_data=json.dumps(data, indent=2)
print(updates_json_data)