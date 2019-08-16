import random
import matplotlib.pyplot as plt


def hypothesis(i,theta):
    theta1=theta[0]
    for j in range(1,len(theta)):
        theta1=theta1+theta[j]*float(i[j-1])

    return theta1;


def cost_find(training,theta):
    cost=0
    for i in training:
        y_current=hypothesis(i,theta)
        cost=cost+((float(i[6])-y_current)**2)
    cost=float(cost/(2*len(training)))

    return cost;


def gradient_descent(training):

    theta = [0]*7 #initialising theta with 0
    rate=0.03     #learning rate
    m=float(len(training)) #no. of  instance in dataset
    cost1=[]
    for i in range(20000):
        diff_cost=[0]*len(theta)

        for i in training:
            y_current=hypothesis(i,theta)
            y=float(i[6])
            a=y-y_current

            diff_cost[0]=diff_cost[0]+a

            for k in range(1,len(diff_cost)):

                diff_cost[k]=diff_cost[k]+a*float(i[k-1])


        for j in range(0,len(theta)):
            theta[j]=theta[j]+(rate*(diff_cost[j]/m))   #updating theta values


        cost=cost_find(training,theta)
        # print(cost)
        cost1.append(cost)

    return theta,cost1;


#reading the file and appending the values in the list line by line
arr2=[]
file=open("Group57_regression.txt","r")
for line in file:
    arr1=line.split()
    arr2.append(arr1)
file.close()

#shuffling the date
random.shuffle(arr2)

training=arr2[0:200] #training dataset
testing=arr2[200:]  #testing dataset

theta,cost1=gradient_descent(training) #gradient function call

#ploting cost vs no. of iterations
plt.plot(cost1)
plt.ylabel('Cost')
plt.xlabel('No. of iterations')
plt.show()

#training error
tr_error=cost_find(training,theta)
print("Training error=",tr_error)

#testing error
ts_error=cost_find(testing,theta)
print("Testing error",ts_error)
