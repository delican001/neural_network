import random as rnd
import math
import sys

left_x =-512
left_y =-512
right_x=512
right_y=512
n=2
length=10000
mutate_coeff=0.1
hem_const=0.0001
iterations_num=200000


def func(x):
    return f(x)

ranges = [[-512,512],[-512,512]]
def f(v):
    v147 = v[1]+47
    first = -(v147) * math.sin(math.sqrt(math.fabs(v[0]/2 + v147)))
    second = v[0]*math.sin(math.sqrt(math.fabs(v[0]-v147)))
    return  first - second

def booth_func(x):
    left_x = -10
    left_y = -10
    right_x = 10
    right_y = 10
    return (x[0]+2*x[1]-7)*(x[0]+2*x[1]-7)+(2*x[0]+x[1]-5)*(2*x[0]+x[1]-5)

def rosenbrock(x):
    left_x=float('-inf')
    right_x=float('inf')
    left_y=None
    right_y=None
    res=0
    for i in range (n-1):
        res=res+100*(x[i+1]-x[i]*x[i])*(x[i+1]-x[i]*x[i])+(1-x[i])*(1-x[i])
    return res

def init():
    values=[]
    for i in range(length):
        point=[]
        if (left_y==None):
            for i in range(n):
                point.append(rnd.uniform(left_x,right_x))
        else:
            point.append(rnd.uniform(left_x,right_x))
            point.append(rnd.uniform(left_y, right_y))
        values.append(point)
    return values

def cross(point1,point2):
    new_points=[[],[]]
    for i in range(int(n/2)):
        new_points[0].append(point2[i])
        new_points[1].append(point1[i])
    for i in range (int(n/2),n,1):
        new_points[0].append(point1[i])
        new_points[1].append(point2[i])
    return new_points

def check_hemming(point1,point2):
    hem_calc=0
    for i in range(n):
        hem_calc=hem_calc+math.fabs(point1[i]-point2[i])
    if (hem_calc>hem_const):
        return True
    return False

def selection(values):
    values.sort(key=lambda x:func(x))
    new_arr=values[0:length]
    return new_arr

def mutate(values):
    for i in range(length):
        for j in range(n):
            values[i][j]=values[i][j]+rnd.uniform(-mutate_coeff,mutate_coeff)
            if n==2:
                if values[i][0]>right_x:
                    values[i][0]=right_x
                if values[i][1]>right_y:
                    values[i][1]=right_y
                if values[i][0]<left_x:
                    values[i][0]=left_x
                if values[i][1]<left_y:
                    values[i][1]=left_y
    return values

values = init()
for j in range(iterations_num):
    values = mutate(values)
    for i in range(length-1):
        if (check_hemming(values[i],values[i+1])):
            children = cross(values[i],values[i+1])
            values.append(children[0])
            values.append(children[1])
    values=selection(values)
    print(str(j) +" " +str(values[0]))
    print(func(values[0]))
print(values[0])