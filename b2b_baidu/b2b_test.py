import json

# json string:
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print(s)
print(type(s))
print(s.keys())
print(s["name"])
print(s["type"]["name"])
print(s["type"]["parameter"][1])
