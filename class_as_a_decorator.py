# Class statement + Operator Overloading 

class logger: 
    def __init__(self, decorated_function_object): 
        self.decorated_function_object = decorated_function_object 
    def __call__(self, *args, **kwargs): 
        print("Nonkeyword arguments")
        for i in range(len(args)): 
            print("args[{}]:{}".format(i, args[i]))
        print("Keyword arguments")
        for (v_name, v_val) in kwargs.items():
            print(v_name, v_val)
        ret = self.decorated_function_object(*args, **kwargs)
        print("Return Value:", ret, "type(Return Value):", type(ret))
        print("-" * 80)
        return ret 

@logger 
def compute_1(x, y):
    rs1 = x**2 
    rs2 = y**2 
    return rs1 - rs2 

print("type(compute_1):", type(compute_1))
# compute_1 = logger(compute_1)

def main(): 
    r1 = compute_1(10, 20)
    r2 = compute_1(20, 10)
    r3 = compute_1(25, 13) 

    print("From main:r1={}, r2={}, r3={}".format(r1, r2, r3))

main()
