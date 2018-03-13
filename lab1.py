# class generator
import numpy.random as rnd
import matplotlib.pyplot as plt
import math

# number of classes
num_of_class = 3
# type of classes: 0,1,2...
type_of_class = 1
# case 0: centers of classes are really far away from each other
# case 1: centers are pretty much close and classes cross
# case 2: centers not really far away so classes close to cross, but actually don't
# case 3: totally random centers

level_of_cross=10
    #value from 0 to 10 (for type 1)

#number of coordinates for each class
n=2

# minimum and maximum radius of classes (distance between center of class and its members)
min_class_radius = 20
max_class_radius = 40

# number of points in each class
points_in_each_class = 500

# max x and y coords (x=[0,x] , y=[0,y])
max_coord=1000

# matplotlib colors for classes
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
center = []

# container for classes
classes = []

def calc_center(type):
    tempcoords = []
    if type==0:
        bad_center= True
        while (bad_center):
            tempcoords = []
            for i in range(n):
                tempcoords.append(rnd.randint(low=0, high=max_coord))
            if (center.__len__()==0):
                return tempcoords
            for i in range(center.__len__()):
                dif=0
                print("Test")
                for j in range(center[i].__len__()):
                    dif=dif+(center[i][j]-tempcoords[j])*(center[i][j]-tempcoords[j])
                print(dif)
                if (dif>min_class_radius*min_class_radius):
                    bad_center=False
                    print(bad_center)
        return tempcoords
    if type==1:
        bad_center= True
        while (bad_center):
            tempcoords = []
            if center.__len__() == 0:
                for i in range(n):
                    tempcoords.append(rnd.randint(low=0, high=max_coord))
                return tempcoords
            for i in range(n):
                tempcoords.append(rnd.randint(low=2*min_class_radius*(10-level_of_cross)/20+center[center.__len__()-1][i]-1,high=center[center.__len__()-1][i]+2*min_class_radius*(10-level_of_cross)/10+1))
            for i in range(center.__len__()):
                dif=0
                print("Test")
                for j in range(center[i].__len__()):
                    dif=dif+(center[i][j]-tempcoords[j])*(center[i][j]-tempcoords[j])
                print(dif)
                #if (dif<min_class_radius*min_class_radius & dif>min_class_radius*min_class_radius*level_of_cross/10):
                bad_center=False
                print(bad_center)
        return tempcoords
    if type==3:
        return [rnd.randint(low=0, high=max_coord),rnd.randint(low=0, high=max_coord)]

def draw_classes(classes):
    if n==2:
        for i in range(classes.__len__()):
            x = []
            y = []
            for j in range(classes[i].coords.__len__()):
                x.append(classes[i].coords[j][0])
                y.append(classes[i].coords[j][1])
            plt.plot(x,y,'ro', color=color[rnd.randint(low=0, high=7)])
            print(x)
            print(y)
            print("TEST")
        plt.show()

    else:
        print("Drawing avvailible only for 2d classes")
        for i in range(classes.__len__()):
            print(classes[i].coords)
            print()
class Point_class:
    #class_radius = 0
    #class_center = []
    #x = []
    #y = []
    def __init__(self):
        self.class_radius = rnd.randint(low=min_class_radius, high=max_class_radius)
        self.class_center=calc_center(type=type_of_class)
        center.append(self.class_center)
        self.coords=[]
#        for i in range(n):
#            self.coords.append([])
        while (self.coords.__len__()!=points_in_each_class):
            tmpcoords=[]
            dif=0
            for j in range(n):
                tmpcoords.append(rnd.randint(low=self.class_center[j]-self.class_radius,high=self.class_center[j]+self.class_radius))
                dif=dif+(self.class_center[j]-tmpcoords[j])*(self.class_center[j]-tmpcoords[j])
            if dif<=(self.class_radius*self.class_radius):
                self.coords.append(tmpcoords)
#        for i in range(self.coords.__len__()):
#        print(self.coords)
#        print("NEW LINE")
#        plt.plot(self.coords, 'ro', color=color[rnd.randint(low=0, high=7)])

for i in range(num_of_class):
    classes.append(Point_class())
draw_classes(classes)
