arr=[4,7,9,11,24]

max= arr[0]

n = len(arr)

for i in range(1,n):
    if(arr[i]>max):
        max = arr[i]

print(max)        

arr=[4,7,9,11,24]

min= arr[0]

n = len(arr)

for i in range(1,n):
    if(arr[i]<min):
        min= arr[i]

print(min)    