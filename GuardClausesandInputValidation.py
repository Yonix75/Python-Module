def process_data_guarded(list444):
    
    
    print(list444,len(list444),sep="\t")
    if list444 is True:
        print("Is not list")
    else:
        print(list444,len(list444),sep="\t")    
   

    
list1 = []
list2 =[1, 2, 3]
process_data_guarded(list1)
process_data_guarded(list2)
process_data_guarded(None)