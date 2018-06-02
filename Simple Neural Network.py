
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'inline')
import pip
pip.main(["install","numpy"])

# In[3]:


from matplotlib import pyplot as plt
import numpy as np


# In[232]:


data = [[0,1,0,1,1],
       [1,1,0,1,0],
       [0.01,.92,.1,.93,1],
        [0,.75,.05,.75,1],
        [.75,.80,.1,.90,0],
        [.12,.95,.11,.79,1],
        [0.1,.9,0.01,.75,1],
        [0,0.90,.06,.60,1],
        [.95,.75,0.2,.75,0],
        [.85,.75,.09,.95,0],
        [.01,.01,.09,.01,0],
        [.90,.87,.70,86,0],
        [.96,.01,.99,.01,0],
        [.01,.01,.95,.95,0],
        [.15,.65,.19,.59,1],
        [.16,.62,.20,.55,1],
       [.10,.10,.12,.09,0],
       [.20,.55,.10,.60,1],
       #[.50,.50,.50,.50,0],
       [.50,.01,.01,.40,0],
       [.60,.60,.04,.04,0],
       [.19,.85,.20,.75,1],
       [.22,.75,.11,.69,1]]

mystery_number=[.02,.70,.08,.75]


# In[134]:


data[2][0]


# In[135]:


#     o  flower type
#    / \   w1,w2,b
#   o   o   length, width

w1 = np.random.randn()
w2 = np.random.randn()
w3 = np.random.randn()
w4 = np.random.randn()
b = np.random.randn()


# In[132]:


def sigmoid(x):
    #Ensures that the answer is between 1 and 0 
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    #derivative of sigmoid, sigmoid prime
    return sigmoid(x)*(1-sigmoid(x))


# In[184]:


T = np.linspace(-6,6,100)
#Y = sigmoid(T)
#This plots the sigmoid and sigmoid prime graphs
plt.plot(T,sigmoid(T),c='r')
plt.plot(T,sigmoid_p(T),c='b')


# In[233]:


plt.axis([0,1.5,0,1.25])
plt.grid()
for i in range(len(data)):
    point = data[i]
    color = "r"
    if point[4]==0:
        color="b"
    plt.scatter(point[0],point[1],c=color)


# In[240]:


# training loop
learning_rate = 0.2
costs = []
w1 = np.random.randn()
w2 = np.random.randn()
w3 = np.random.randn()
w4 = np.random.randn()
b = np.random.randn()
for i in range(50000):
    ri = np.random.randint(len(data))
    point = data[ri]
    #extremely important equation in training neural network
    z = point[0]*w1 +point[1]*w2+point[2]*w3+point[3]*w4+b
    #condense it to be between0 and 1
    prediction = sigmoid(z)
    #whatever the target is
    target = point[4]
    #the difference squared of the prediction- target is the cost between them
    #this should decrease with more iterations
    cost = np.square(prediction-target)
    #add it to array of costs
    costs.append(cost)
    #derivative of cost with respect to prediction
    dcost_pred = 2*(prediction-target)
    #derivate of prediction with respect to z is sigmoid prime
    dpred_dz = sigmoid_p(z)
    #derivative of z with respect to w1
    dz_dw1= point[0]
    #derivative of z with respect to w2
    dz_dw2 = point[1]
    dz_dw3 = point[2]
    dz_dw4 = point[3]

    #derivative of z with respect to b
    dz_db = 1
    #Now you find the derivative of the costs with respect to different values
    #derivative of the cost with respect to z
    #uses partial derivatives
    dcost_dz =dcost_pred*dpred_dz
    dcost_dw1 = dcost_dz *dz_dw1
    dcost_dw2 = dcost_dz*dz_dw2
    dcost_dw3 = dcost_dz*dz_dw3
    dcost_dw4 = dcost_dz*dz_dw4
    dcost_db = dcost_dz*dz_db
    w1 = w1-learning_rate*dcost_dw1
    w2 = w2-learning_rate*dcost_dw2
    w3 = w3-learning_rate*dcost_dw3
    w4 = w4-learning_rate*dcost_dw4
    b = b-learning_rate*dcost_db
plt.plot(costs)


# In[241]:


for i in range(len(data)):
    point=data[i]
    print(point)
    z = point[0]*w1+point[1]*w2+b
    prediction = sigmoid(z)
    print(prediction)


# In[254]:


z = mystery_number[0]*w1+mystery_number[1]*w2+b
prediction = sigmoid(z)
prediction


# In[255]:


import os


# In[266]:


def which_number(pixel1,pixel2,pixel3,pixel4):
    z = pixel1*w1+pixel2*w2+pixel3*w3+pixel4*w4+b
    prediction = sigmoid(z)
    if prediction>.5:
        os.system("say one")
    else:
        os.system("say not one")


# In[253]:


#which_number(0.10,.55,0.20,.70)


# In[333]:


p1,p2,p3,p4 = input("Please give 4 numbers between 0 and 1, depicting pixels in a 4 pixel image in clockwise direction split by commas. \n For example, 0,1,0,1 means that \n0 1\n0 1\nis the number one since the rightmost pixels are filled, whereas 1,0,1,1: \n1 0\n1 1\nis not one since it does not resemble a 1\nThe numbers given can be decimals (ex. .01,.75,.86,90)\n").split(',')
p1=float(p1)
p2=float(p2)
p3=float(p3)
p4= float(p4)
which_number(p1,p2,p3,p4)
#print ("{:10s} {:3d}  {:7.2f}".format('xxx', 123, 98))
print()
print ("{:5.2f} {:5.2f}".format(p1, p2))
print ("{:5.2f} {:5.2f}".format(p3, p4))


# In[330]:





# In[265]:




