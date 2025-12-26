def debug(func):
    def wrapper (*args, **kwargs) :
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join()
        return func (*args, **kwargs)
       

    return wrapper

 

def greet(name, greeting = "nameskar"):

    print(f"{greeting}, {name}")



greet("world", greeting = "hello")