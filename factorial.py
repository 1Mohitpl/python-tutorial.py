def factorail(n):
    return 1 if(n==0 or n==1) else n*factorail(n-1)
num = 8
print(num,factorail(num))    
