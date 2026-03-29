def fonc(x,y):
    x+=y
    print(x)
    pass

def hello():
    print("hello")

def name(name):
    print(name)
    
def nameAge(name,surname):
    print(surname+name,sep="  ")

def calcul(x,y):
    if x == 0:
        print("you fool")
    elif y == 0:
        print("you fool")
    else:        
         x/=y
    
def calcul2(x,y):
    return x+y#positional    
        
fonc(3,4)
hello()
nameAge("benarrous","yoni")
calcul(3,0)
print(calcul2(x=5.0,y=0))#keyword

#always keyword first and after positional because python assigned the value and if i coding x=3,3 Error