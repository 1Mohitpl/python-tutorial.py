number = 28
count = 0

if number>1:

    for i in range(1,number+1):
     if (number%i)==0:
           count = count+1
    if count == 2:
            print("number is prime")

    else:
          print("number is not prime")
