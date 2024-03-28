items =  ["coffe" ,"apple", "coffe" , "orange" , "apple","coffe" ]

unique_item = set()


for item in items :
    if item in unique_item:
        print("Dulicate : ", item)   #list uniqueness checker
        break
    
    unique_item.add(item)