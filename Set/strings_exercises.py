
python = "python"
print(python)
Devops = "Devops"
print(Devops)
print(python+Devops)

s = """ Ligne  
Ligne 2
Ligne 3
"""
print(s)

a = 1
b = 2
result = "result :"
print(result , b)

print(f"result {b}")
print(result,b)
print("result" , b)


array ="""   
hi my name is yoni"""
print(array.strip())
#t = array.strip()
#print(t)


t= array.upper()
print(t)

t =array.lower()
print(t)

file = "file.yaml"
print(file.startswith("f"))#The startswith() method returns True if the string starts with the specified value, otherwise False.

print(file.endswith("yaml"))

path = "/user/local/bin"

result = path.split("/")#split() sert à découper une chaîne de caractères en plusieurs morceaux.

result = "/".join(result)
print(result)

path2 = '/python'
print(result+path2)

print(result[0])
print(result[3:10])

print(len(result))


#17
#!impossible to change str index to arraystring
result[0]= '3'
print(result)