import json

#with open("./PIoT_TL3_code/person.json", "r") as read_content:
#	print(json.load(read_content))

o = open("PIoT_TL3_code/person.json")
read_content = json.load(o)
l = read_content["firstName"] 
print(l)