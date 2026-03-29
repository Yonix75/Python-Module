ports_list = [8080, 8443, 22, 8080, 443]

unique_ports = set(ports_list)

print(type(unique_ports))

server_names = {"web01", "web02", "web03"}

print(22 in unique_ports)

print(22 in server_names)

unique_ports.add(3000)

print(unique_ports)

unique_ports.remove(22)
print(unique_ports)

#unique_ports.remove(22)
#print(unique_ports)

unique_ports.discard(22)
print(unique_ports)

valid_set = {(1, 2), (3, 4)}
#list with set its error
#invalid_set = {[1, 2], [3, 4]}

myList= [1,2,3,4,5,67,8,9,9,9]
newList= set(myList)
newList.add(888)
print(888 in newList)
