# Kendell Visser
# Dr. Siebrase
# COMP 3006 - Python Software Development
# University of Denver
# Master of Science - Data Science

'''
Assignment 3.1:
Simulate a population exponential growth system xdot = a * x where
x0 is the value of x at t=0,
a is a parameter,
t is time,
xdot is the rate of change of x,
and x is the population.
Use the following: x0 = 100; a=5; d_t = 0.1 the time step of the simulation.
Start t at 0 and stop the simulation at t=2.
Hint: see lesson 2 slide 12 on an object subject to gravity.
Hint: see also https://docs.python.org/3/library/csv.html
Display the results of each time step and write the results to a csv file.

'''



'''
FROM LESSON 2, SLIDE 12:

import csv
## equations of motion
s = 0 ## position
v = 100 ## velocity, initially upward
G = -9.8 ## gravity, downward
d_t = 0.1 ## deltaT - timestep
t = 0 ## total time
with open('Data.csv', 'wb') as o_file:
writer = csv.writer(o_file, quoting=csv.QUOTE_ALL)
writer.writerow(["T", "S", "V"])
while s >= 0:
t += d_t
s = s + v*d_t - 0.5*G*(d_t**2)
v = v + G * d_t
writer.writerow([t, s, v])


'''
import csv
import numpy as np

# t = time
x0 = 100 # t = 0
a = 5
d_t = 0.1 # time step of the simulation.
timeT = 0 # Starting time is at timeT = 0 then we will use the d_t = 0.1 to go by a step size of 0.1 up to a time of 2 seconds.
#xPop =   # This is our x variable. x is the population at time t. The population
# starts at a population of 100 at time t.
#x = t += d_t
#t = d_t += 0.1 {0.1 < t < 2}
#xdot = a * x

def xdot_exp_growth(t,x,a):
    #timeT = 0, x0 = 100
#    print(headers("Time", "Population Value"))
    xdot = a * x
    return xdot
#fileName = "Population_Exponential_Growth.csv" # Empty file csv that we will write to and is created in the same working directory.
#file = open(fileName, "w") # We use w instead of r to write to this file, and not just read to it.

with open('Population_Exponential_Growth.csv', 'w') as fileName:
    writer = csv.writer(fileName, quoting=csv.QUOTE_ALL)
    writer.writerow(["Time", "Population Value"]) # Creates column header
    xPop = 0
    while timeT >= 0 and timeT <=2.1:
        # define xdot and adjust population based on xdot.
        # update xdot as xPop is going to be changing.
        # Augment time based on growth factor.
        # if(timeT == 0):
            # print(xPop = 100) # x0 = 100.

        #timeT += d_t
        xPop += x0 + a*d_t # xPop is being created as the variable that uses the initial position of 100 and is adding this value to the parameter, a (multiplied to the) timestep, d_t.
        #print(timeT, int(xPop))
        writer.writerow([timeT, int(xPop)])
        timeT += d_t
'''
for i in range(1,len(t)):
    y[i]=y[i-1]+d_t*ode(t[i-1],y[i-1],a)

'''


'''
import csv
import numpy as np

# t = time
x0 = 100 # t = 0
a = 5
d_t = 0.1 # time step of the simulation.
#x = t += d_t
#t = d_t += 0.1 {0.1 < t < 2}
xdot = a * x

def xdot_exp_growth(t,x,a):
    return xdot
'''
