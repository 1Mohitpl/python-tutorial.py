# write a program to calculate the avarage hight from all the hight in the list

hights = [10,14, 12, 11, 18, 3]

total_hights = 0
sum_hights = 0
for i in hights:
    total_hights+=1
    sum_hights += i

avarage_hight = sum_hights/total_hights

print(round(avarage_hight))

