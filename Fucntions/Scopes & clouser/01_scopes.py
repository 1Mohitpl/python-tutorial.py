# username  = "mohitpaul"

# def func ():
#     username = "mohit"
#     print(username)


# func()
# print(username)

x = 67

def f1():

    # x=88
    def f2():
        print(x)
    f2()
f1()    



def hardCoder(num):
    def actual (y):
        return y ** num
    return actual


f = hardCoder(2)
h = hardCoder(3)

print(f(2))
print(h(3))