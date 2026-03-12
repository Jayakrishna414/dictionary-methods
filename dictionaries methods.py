data = {"name": "Krishna", "age": 22}

# get
print(data.get("name"))

# keys
print(data.keys())

# values
print(data.values())

# items
print(data.items())

# copy
new_data = data.copy()
print(new_data)

# update
data.update({"city": "Hyderabad"})
print(data)

# setdefault
data.setdefault("country", "India")
print(data)

# pop
data.pop("age")
print(data)

# popitem
data.popitem()
print(data)

# clear
data.clear()
print(data)
