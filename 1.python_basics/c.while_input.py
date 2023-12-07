import json
x = '{ "name":"John", "age":30, "city":"New York"}'
print("Type of x is ",type(x))
y = json.loads(x)
x["sex"] = "male"
print(y)
print("Type of y is ",type(y))
print("name is ",y["name"])