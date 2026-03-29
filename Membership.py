
List1 = [ "Jen","Bob","Rolf"]
print("Jen" in List1)
print("Anne" in List1)

List2 = { "Matrix","One piece","Jumanji"}
user_movie = input("Enter a movie you have watched recently: ")
print(user_movie in List2)

print("rix" in "Matrix")
print("xyz" in List2)

if user_movie in List2:
    print("inside")
else:
    print("outside")    

set1 = {"Matrix","Matrix","coco"}
print(set1)