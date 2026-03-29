
#1
server_list = [
    "web01", "web02", "web03"
]
#2
print(server_list)

#
print(server_list[0])
#
print(server_list[1])
#
print(server_list[-1])

print(server_list[-2])

#print(server_list[-5])

server_list2 = [
    "web01", "web02", "web03" ,"web04", "web05"
]

print(server_list2[:2])

print(server_list2[1:5])

print(server_list2[0::2])



mixed_list =  [
    "web01", 34, True 
]

print(mixed_list)

newList = server_list2[0::2]
newList[1] = "web02"
newList[2] = "web03"
print(newList)