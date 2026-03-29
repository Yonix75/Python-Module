friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

print(friends)
print(abroad)
local = friends.difference(abroad)
aboard = abroad.difference(friends)
#print(friends.difference(abroad))#difference verifie lequel nest pas son doublee
#print(abroad.difference(friends))# les deux quil a son egaux donc set
group =""
group = set(group)

#union
local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends = local.union(abroad)
friends = local | abroad#union cest pareil que union

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

#intersection
print(art.intersection(science))#prend seulement les deux qui se ressemble
group = art & science#meme chose 

print("Bob" in art)
print("Anne" in art)
