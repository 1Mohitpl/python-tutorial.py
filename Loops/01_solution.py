numbers = [4,-5,5,-6,7,2,3,-9,9,-8,8]

positive_num_count = 0

for num in numbers:
    if num >0:                                      #count how many positive numbers are in the given list
        positive_num_count +=1

print("Total positive numbers are :", positive_num_count)