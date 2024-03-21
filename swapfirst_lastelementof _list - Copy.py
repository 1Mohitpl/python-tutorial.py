mylist=[23,24,27,29,30,31] #approach1 

size =len(mylist)

temp =mylist[0]
mylist[0]= mylist[size-1]
mylist[size-1] =temp
print(mylist)