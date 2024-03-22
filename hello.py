h1 = [2,5,7]
# h2 = h1[:]      # using slice method where generate another copy 
# print(h1)
# print(h2)

# h1[1] = 343
# print(h1)       
# print(h2)
 




import copy
h2 = copy.copy(h1)
print(h2)

h1[1] = 343
print(h2)
print(h1)


























# print('hello world')