import json

data ={
    "name":"abhishek",
    "age": 30,
    "city":"newyork"
}

with open("data.json","w") as f:
    json.dump(data,f, indent =4)

print("data written in file")

with open("data.json","r") as f:
    data_load = json.load(f)

print(data_load)