#set1 = {"momo","mama","mimi"}
#user_movie = input("Enter a movie you have watched recently: ")
#if user_movie in set1:
 #   print("inside")
#else:
 #   print("outside")
    
secretNumber= 4
user_input = input("Enter Y if you would like to play: ")        
while(user_input == "y"):
    print("Guess the number")
    user_answers= input()
    user_answers =int(user_answers)
    if user_answers<secretNumber:
        print("to small")
    elif user_answers > secretNumber:
        print("to big")
    else:
         print("bravo")
         break
            
     