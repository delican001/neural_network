import numpy as np
def func(left_value,right_value):
    return booth_func(left_value,right_value)
def booth_func(x,y):
    return (x+2*y-7)*(x+2*y-7)+(2*x+y-5)*(2*x+y-5)
def init_function(left_x,right_x,left_y,right_y,elem_number):
    func_values=[]
    for i in range (elem_number):
        point =[]
        point.append(np.random.randint(left_x,right_x))
        point.append(np.random.randint(left_y, right_y))
        point.append(func(point[0],point[1]))
        func_values.append(point)
    return func_values
def chose_best(values):
    print(values)
    new_values = np.sort(values,order=values[2])
    print()
    print(new_values)

if (__name__== '__main__'):
    values = init_function(-10,10,-10,10,100)
    chose_best(values)