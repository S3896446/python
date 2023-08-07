import json

o = open("C:/Users/patel/Documents/Python/python/Labs/PIoT_TL3_code/person.json")
read_content = json.load(o)
l = read_content["firstName"] 
print(l)
