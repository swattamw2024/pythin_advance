#Parmetarised Function

def smart_divide(func):
    print("Oustside Function")
    def inner(a, b):
        print("inner function")
        if b == 0:
            print("ooops number cant divide by 0")
            return
        return func(a,b)
    return inner
        

@smart_divide
def divide(a, b):
    return a/b

print(divide(5,5))

print(divide(15,5))
