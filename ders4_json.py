import json

x = '{"name":"furkan"}'

y = json.loads(x)                   # JSON'u parse eder.

mydict = {"name":"myName","surname":"mySurname"}
print(type(mydict))

myDictJSON = json.dumps(mydict)     # Python veri tipini JSON'a çevirir.
print(type(myDictJSON))

"""with open("data.json","r") as f:
    print(type(f.read()))"""