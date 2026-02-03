# write a programm to findout the maximum number in a list of number
numbers = input("Enter all the numbers :")

number_list = numbers.split()
for  i in range(0, len(number_list)):
    number_list[i] = int(number_list[i])

print(number_list)

max_num = 0

for i in range(0, len(number_list)):
    if(number_list[i] > max_num):
        max_num = number_list[i]


print(max_num)



