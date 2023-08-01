import json

data = {
    "user" : {
        "name" : "J",
        "phonenumber" : "0231231333",
        "age": "21",
        "address" : "rmit" 
    }
}

with open("user.json", "w") as write:
    json.dump(data, write)