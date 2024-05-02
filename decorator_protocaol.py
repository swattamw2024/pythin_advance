def my_decorator(decorated_function_object):

    def replacement_function(a, b):
        print("a:", a, "b:", b) # PREPROCESSING 
        ret = decorated_function_object(a, b)
        print("Return Value:", ret) # POSTPROCESSING
        return ret
    
    return replacement_function

@my_decorator
def compute_1(x, y):
    rs1 = x**2
    rs2 = y**2
    return rs1 - rs2 

r1 = compute_1(20, 10)
r2 = compute_1(30, 20)
r3 = compute_1(300, 200)

print("r1 = %d, r2 = %d, r3 = %d" % (r1, r2, r3))

