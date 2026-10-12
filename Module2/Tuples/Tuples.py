t = ("String", 7.0, 5, ["new list"], ("new", "Tuple"), False, {"Dictionary": 1}, {"sets"}, "dup", "dup")

print("Type")
print(type(t))

print("\nGet by index")
print(t[0])
print(t[0][-1])

print("\nGet by negative index")
print(t[-len(t)])
print(t[-len(t)][0])

print("\nSlicing a list")
print(t[3:5])

print("\nAdding elements to a tuple")
print(t)
t += ("new Item 1", "new Item 2")
print(t)
