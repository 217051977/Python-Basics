l = ["String", 7.0, 5, ["new list"], ("new", "Tuple"), False, {"Dictionary": 1}, {"sets"}, "dup", "dup"]

print("Type")
print(type(l))

print("\nGet by index")
print(l[0])
print(l[0][-1])

print("\nGet by negative index")
print(l[-len(l)])
print(l[-len(l)][0])

print("\nSlicing a list")
print(l[3:5])

print("\nAdding elements to a list")
extended_list = l[:]
extended_list.extend(['extended'])
print(extended_list)
extended_list.extend('extended')
print(extended_list)

print("\nAppended elements to a list")
appended_list = l[:]
appended_list.append(['appended'])
print(appended_list)
appended_list.append('appended')
print(appended_list)

print("\nUpdate list elements")
updated_list = l[:]
print(updated_list)
updated_list[0] = 'Updated String'
print(updated_list)

print("\nDelete list elements")
deleted_list = l[:]
print(deleted_list)
del(deleted_list[0])
print(deleted_list)

