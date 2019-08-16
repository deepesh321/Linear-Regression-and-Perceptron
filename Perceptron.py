import random
import matplotlib.pyplot as plt

def hypothesis(i,theta):
    theta1=theta[0]
    for j in range(1,len(theta)):
        theta1=theta1+theta[j]*float(i[j-1])

    return theta1;


def gradient_descent(training):

    #theta=[10,10,-2,-10,10]
    theta = [0]*5
    rate=0.03
    m=float(len(training))
    for t in range(10000):
        diff_cost=[0]*len(theta)


        for i in training:
            y_current=hypothesis(i,theta)  #assigning values based on the value of hypothesis fn.

            if y_current>=0:
                y_current=1
            else:
                y_current=-1

            y=i[4]

            if y=="Iris-versicolor":   #assigning values based on class
                y=1
            else:
                y=-1

            a=y-y_current

            diff_cost[0]=diff_cost[0]+a

            for k in range(1,len(diff_cost)):

                diff_cost[k]=diff_cost[k]+a*float(i[k-1])


        for j in range(0,len(theta)):
            theta[j]=theta[j]+(rate*(diff_cost[j]))   #updating theta

    #print(theta)
    return theta;


def error_cal(training,theta):
    error=0

    for i in training:
        y_current=hypothesis(i,theta)

        if y_current >=0:
            y_current="Iris-versicolor"
        else:
            y_current="Iris-virginica"

        if i[4]!=y_current:
            error=error+1
    return error;

#reading the file and appending the values in the list line by line
arr2=[]
file=open("Group57_perceptron.txt","r")
for line in file:
    arr1=line.rstrip("\r\n").split(',')
    arr2.append(arr1)
file.close()

random.shuffle(arr2)

training=arr2[0:70] #training dataset
testing=arr2[70:]  #testing dataset

theta=gradient_descent(testing)
print("theta values=",theta)

tr_error=error_cal(training,theta)
print("error on training set=",float(tr_error/70))

ts_error=error_cal(testing,theta)
print("error on testing set=",float(ts_error/30))
