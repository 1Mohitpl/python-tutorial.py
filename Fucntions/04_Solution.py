def sum_all (*args):    # * it takes multiple arguments 
    print(args)
    for i in args :
        print(i *2)
    return sum (args)
          
print(sum_all ( 1,3,4))               
print(sum_all ( 1,3,4,9,7,8,3))
print(sum_all ( 1,3,4,4,6,9,6))