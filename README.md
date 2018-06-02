# Neural-Network Practice
Simple neural network involving a inputting data for a four pixel image which can guess if you are giving the number 1 or not.
In this very simple example, we give the neural network 4 data points (4 pixels) of a 4 pixel image:

p1  p2
p3  p4

If the value is 1, the pixel is completely on. If the value os 0, the pixel is completely off. However, the values can vary between 0 and 1. For example, the number 1 is as shown like this:

0   1<br/>
0   1

This shows the number 1 shown through two pixels on the far right turned on. The number 1 can also be:

0.10   0.65<br/>
0.08   0.74

The following is *not* 1 because the incorrect pixels are turned on:

1   1<br/>
0   1

0.75   .98<br/>
0.65   .10

This is because the leftmost pixels, while slightly on, have values small enough to be treated as off. The rightmost pixels, while not entirely on, have high enough values to be treated as on, thus creating the number 1.

The point of the neural network is to give it any 4 data points and guess if the number is 1 or not. 
To train the neural network, we feed around 20 data points of given arrays [p1,p2,p3,p4,t], where p1-p4 are the pixel values and t is either 0 or 1 (1 is if the value is 1 and 0 is if the value is not 1). We run the training loop 50000 times to decrease the cost of the neural network e.g. the target number minus the predicted value. 

The user therefore only needs to give 4 data points, and the neural network should be able to guess if the given data points are 1 or 0. 

***DIRECTIONS***
1. Ensure numpy and matplotlib are installed for Python.
2. If you have troubleshooting issues, I followed this tutorial for a similar neural network:
https://www.youtube.com/watch?v=ZzWaow1Rvho&list=PLxt59R_fWVzT9bDxA76AHm3ig0Gg9S3So
,so you can also set up jupyter notebook to work in.
