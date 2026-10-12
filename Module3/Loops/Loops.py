print("For in a range of 3")
for x in range(3):
    print(x)

print("\nFor in a range from 0 to 3")
for x in range(0, 3):
    print(x)

print("\nFor in a range from 0 to 3, with an incrementation of 2")
for x in range(0, 3, 2):
    print(x)

print("\nLoop through a list")
for i in [1982,1980,1973]:
    print(i)

print("\nLoop through a list using index")
l = [1982,1980,1973]
for i in range(len(l)):
    print(l[i])

print("\nLoop through a list using for each")
l = [1982,1980,1973]
for i, e in enumerate(l):
    print(f"With index: {l[i]} | Element: {e}")

print("\nExercise: Multiplication of a String")
l = [1982,1980,1973]
for i, e in enumerate(["A", "B", "C"]):
    print(i,2*e)