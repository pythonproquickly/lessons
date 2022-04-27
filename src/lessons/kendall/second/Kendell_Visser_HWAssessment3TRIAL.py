import csv
import numpy as np

# t = time
x0 = 100  # t = 0
a = 5
d_t = 0.1  # time step of the simulation.
timeT = 0  # Starting time is at timeT = 0 then we will use the d_t = 0.1 to go by a step size of 0.1 up to a time of 2 seconds.


# xPop =   # This is our x variable. x is the population at time t. The
# population
# starts at a population of 100 at time t.
# x = t += d_t
# t = d_t += 0.1 {0.1 < t < 2}
# xdot = a * x

def xdot_exp_growth(t, x, a):
    # timeT = 0, x0 = 100
    #    print(headers("Time", "Population Value"))
    xdot = a * x
    return xdot


# fileName = "Population_Exponential_Growth.csv" # Empty file csv that we
# will write to and is created in the same working directory.
# file = open(fileName, "w") # We use w instead of r to write to this file,
# and not just read to it.

with open('Population_Exponential_Growth.csv', 'w') as fileName:
    writer = csv.writer(fileName, quoting=csv.QUOTE_ALL)
    writer.writerow(["Time", "Population Value"])  # Creates column header
    # print(writer)
    # Time = writer[0]
    # print(Time)
    # Population_Value = writer[1]
    # print(Population_Value)

    xPop = 0
    xPopList = list(0 for i in range(0,
                                     20))  # Create a list of values initiated to 0 there are 20 rows going from 0 to 2 in a timestep of 10, hence we go to range of 20.  This will make the population values have index positions to call.
    xPopList[
        0] = x0  # The first value in the xPopList column needs to be the time = 0, Population Value = 100.
    # print(xPopList)

for i in range(1, 20):
    xPopList[i] = xPopList[i - 1] + d_t * xdot_exp_growth(timeT,
                                                          xPopList[i - 1], a)
'''
    for i in range(1,20):
        xPopList[i]=xPopList[i-1]+d_t*a
        #print(xPopList)
'''
# print(f'{t[i]:>10g}{y[i]:>10g}')
# f.write(f'{t[i]:g},{y[i]:g}\n')
# f.close()
# print('Data written to',file)
# xPop += x0 + (a * d_t)
xPop = x0
while 0 <= timeT <= 2.1:
    # xPop += 1.5 * xPop
    print(round(timeT, 1), round(xPop, 0))
    # writer.writerow([round(timeT, 1), round(xPop, 0)])
    timeT += d_t
    xPop = xPop + (xPop * d_t * 5)
    # for i in range(1, timeT):
    #    xPop[i] = xPop[i-1] + a*d_t

#        xPop += x0 + a*d_t # xPop is being created as the variable that uses the initial position of 100 and is adding this value to the parameter, a (multiplied to the) timestep, d_t.
# xPopN += xPop + a*d_t
#    print(timeT, int(xPop))
#        writer.writerow([timeT, int(xPop)])
#        timeT += d_t
# Goal for Position Value for Population_Exponential_Growth is {x0 = 100, xPop = 1.5 * previous xPop value}
# Note we are multiplying by a factor of 1.5 from the previous term because a = 5 * d_t = 0.1 is = 0.5 which means that when called recursively, we want to multiply itself (1) + the newly (0.5) to the previous term; therefore, starting with x0 = 100, we want x_n = 1.5 * x_(n-1)
# print(x0 += 1.5)

'''
y=np.zeros(t.shape)
y[0]=x0
for i in range(1,len(t)):
    y[i]=y[i-1]+d_t*ode(t[i-1],y[i-1],a)

'''
