#movie tickets price based on some condition 
# age = int(input("Enter Your age:"))
# day = "Wednesday"
# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     price = price-2

# print("Ticket price for you : ", price)


# assign a student's grade based on student's score

marks = int(input("Enter your score: "))

if marks < 0 or marks > 100:
    print("Invalid score")

elif marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks <= 89:
    print("B")
elif marks >= 70 and marks <= 79:
    print("C")
elif marks >= 60 and marks <= 69:
    print("D")
else:
    print("F")

