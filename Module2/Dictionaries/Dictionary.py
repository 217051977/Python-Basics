d = {"Dictionary": 1}

print("Type")
print(type(d))

print("\nGet by key")
print(d["Dictionary"])

print("\nAppended elements to a list")
print(d)
d["newKey"] = "newValue"
print(d)

print("\nUpdate list elements")
print(d)
d["newKey"] = 'UpdatedValue'
print(d)

print("\nDelete list elements")
d = d.copy()
print(d)
del(d["newKey"])
print(d)

