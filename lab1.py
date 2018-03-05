# class generator
import numpy.random as rnd
import matplotlib.pyplot as plt
import math

# number of classes
num_of_class = 3
# type of classes: 0,1,2...
# type_of_class =0

# number of points in each class
points_in_each_class = 500

# max x and y coords (x=[0,x] , y=[0,y])
max_x = 1000
max_y = 1000

# matplotlib colors for classes
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
center = []


class Point_class:
    # max distance between center of class and its points
    class_radius = 30
    x_center=0
    y_center=0

    def __init__(self):
        self.class_radius = rnd.randint(low=20, high=40)
        self.x_center=rnd.randint(low=0, high=max_x)
        self.y_center=rnd.randint(low=0, high=max_y)
        center.append([self.x_center, self.y_center])
        x = []
        y = []
        for i in range(points_in_each_class):
            tmpx = rnd.randint(low=-self.class_radius + 1, high=self.class_radius - 1)
            x.append(self.x_center + tmpx)
            tmpy=int(math.sqrt(self.class_radius * self.class_radius - tmpx * tmpx))
            y.append(self.y_center + rnd.randint(low=-tmpy,high=tmpy))
        plt.plot(x, y, 'ro', color=color[rnd.randint(low=0, high=7)])

for i in range(num_of_class):
    point_class = Point_class()
plt.show()
