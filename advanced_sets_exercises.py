#set([[1, 2], [3, 4]])
#set={{1, 2}, {3, 4}}

set_of_tuples= (1,2), (3,4)
print ((1,2) in set_of_tuples)
print ((1, 3) in set_of_tuples)

developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}
print("Alice" in developers)

#developers.union(admins)
#print(developers)
developers | admins
print(admins)

developers.intersection(admins)

developers & admins

developers.difference(admins)

developers - admins

developers.intersection_update(admins)

developers.intersection(admins)

print(developers)

v1 = {"momo", "pop", "luke"}
v2 = {"Alice", "pop"}

print(v1.union(v2))


print(v1.intersection(v2))


print(v1.difference(v2))
