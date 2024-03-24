laptop_types = {"Lenevo" : "i3", "MSI" : "i4" , "Asus" : "i5"}     #create an dictonary 
print (laptop_types)

print (laptop_types.get("Asus"))   #to get  the value of an dictonary 

laptop_types["Asus"] = "I7"
print(laptop_types)

for my in laptop_types :
    print(my)

for my in laptop_types :
    print(my, laptop_types[my])