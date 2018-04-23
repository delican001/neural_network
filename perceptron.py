import numpy as np
import lab1 as generator
import matplotlib.pyplot as plt

teach_speed=0.05
def sigm(x):
    if (x>10):
        return 1
    elif (x<-10):
        return 0
    else:
        return 1./(1+np.exp(-x))

def check_if_match(coords):
    for i in range (neuron.__len__()):
        sum=0
        for j in range(coords.__len__()):
            sum=sum+neuron[i][j]*coords[j]
        if (sigm(sum)<0.1):
            return False
        else:
            return True


classes = generator.generate_classes()
neuron = []
for i in range (classes.__len__()):
    neuron.append(np.zeros(classes[0].coords[0].__len__()+1))
eps = 0.05
error_value=1
step=0
#while((np.abs(error_value)>eps) & (number<classes[0].coords.__len__())):
while(True):
    step=step+1
    number = 0
    error_number=0
    x=[]
    y=[]
    for i in range(int(classes[0].coords.__len__()/2)):
        error_value=0
        for i in range (classes.__len__()):
            for j in range(neuron.__len__()):
                sum = 0
                for k in range(neuron[j].__len__()-1):
                    sum=sum+neuron[j][k]*classes[i].coords[number][k]
                sum=sum+neuron[j][neuron[j].__len__()-1]*1
                sigm_val=sigm(sum)
                if (i==j):
                    change=1-sigm_val
                else:
                    change=0-sigm_val
                for k in range(neuron[j].__len__()-1):
                    calced_change=teach_speed*change*classes[i].coords[number][k]
                    neuron[j][k]=neuron[j][k]+calced_change
                    error_value=error_value+calced_change
                calced_change = teach_speed * change * 1
                neuron[j][neuron[j].__len__()-1] = neuron[j][neuron[j].__len__()-1] + calced_change
                error_value = error_value + calced_change
        number = number + 1
    x.append(step)
    y.append(error_number)

    plt.clf()
    plt.plot(x,y)
    plt.draw()
    plt.pause(0.1)

print()
print()
print()
print()
print()
for i in range(int(classes[0].coords.__len__()/2)):
    for j in range(classes.__len__()):
        check_if_match(classes[j].coords[i])
        print('{} {}'.format(i,j))


