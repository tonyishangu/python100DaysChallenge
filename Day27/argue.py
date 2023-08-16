# *args many positional Arguemants ===> Unlimited Args


def add(*args):     #gets all the arguements passed
    print(args[0])  #access by index
    sum  = 0
    for n in args:
        sum +=n
    return(sum)

print(add(3,4,5))



# **kwargs : many keyworded Arguements

def calc(n, **kwargs):
    print(kwargs)   #makes a dictionary of all keyword arguments
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs['add'])    #get the value of the key add
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calc(3,add=4, multiply=8)