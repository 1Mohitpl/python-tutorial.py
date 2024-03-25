#straing methodes
# course= 'pthon for beginners'
# course
# print(course.upper())

# name = input("Enter an your name :  ")
# age =  int (input ("Enter your age: "))
# print(type(age))

# print(age)






# chai = "Masala chai"
# print(chai.find("chai"))             #find function to determine the postioin of the strings
 


# name = "mohit kumar paul"
# print(name.count("m")) 
#                                        #Count function to use to determine the number of repeating char, numbers 
# word = "562125543565"
# print(word.count("6"))           




# drink_type = "soft drinks"
# quantity = "2"
# order = "I ordered {} bottels of {}"     #{} => its an placeholder to carry variables 

# print(order.format(quantity,drink_type))    #format function to use add variables



# tea_types = "Lemon tea" , "Masala tea" ,"Ginger tea"

# print(",". join (tea_types))      #join function to use to add values in the list 


# range(10)
# print(range(10))

# age = int (input ("Enter your age"))   #age Group categorization problem


# if   age <13:
#     print("you are underEighteen")
# elif  age <20:
#     print("You are an Tenneger") 
# elif  age <60 :
#     print("you are Adult")
# else :
#     print("senior") 

# password = input("put it here password : ")

# if len (password) <6 :
#     strenght = "weak"                         #password strenght checker
# elif len(password) <=10:
#     strenght = "medium"
# else: 
#     strenght = "Strong"
# print("Your password strenght is very :" ,strenght)


year = int (input ("Enter an year : "))

if (year % 400 == 0) or (year % 4 == 0) and (year % 100 !=0):
    print("Given year is Leap year")                                 #check the year is leap year or not 

else: 
    print("Given year is not a Leap year")
















































# name = 'mohitpaul'
# print(name[1:-1])


# #dynamically insert value into string 
# first = ' mohiyt '
# last = 'paul '
# message =  first + ' [' + last + '] is a coder'
# mesg = f'{first} [{last}] is a coder'
# print(mesg)