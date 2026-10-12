s = {"A", "B"}

print("Type")
print(type(s))

print("\nAdding elements to a set")
print(s)
s.add('extended')
print(s)

print("\nDelete set elements")
print(s)
s.remove("extended")
print(s)

print("\nIntersepting sets")
s2 = {"B"}
print(s&s2)

print("B" in s)