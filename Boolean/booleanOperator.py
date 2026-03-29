var = 10
var2 = 12

print(var == var2)
print(var!=var2)
print(var >= var2)
print(var <=var2)
print("=================================")
result = 5>3
print(result)
result = 5<3
print(result)
print("=================================")
#list1 = {"coco", "caca","cucu"}
#list2 = {"coco", "caca","cucu"}

#print(list1 is list2)

list1 = ["coco", "caca","cucu"]
list2 = ["coco", "caca","cucu"]
print(list1 == list2)
print(list1 is list2)#is not same object

print("=================================")#same object same contenu
varlist = list1
print(varlist == list1)
print(varlist is list1)


