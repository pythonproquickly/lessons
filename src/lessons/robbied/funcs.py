# My Birthday Match Monte Carlo Simulation

import csv

from random import randint


# hmwk4Q4.py

def myBirthday(N):
    myBirthday = randint(1, 365)
    for _ in range(N):
        if myBirthday == randint(1, 365):
            return True
    return False


# hmwk4Q5.py

def main():
    nTrials = 1000
    nPeople = 400

    probData = [['People', 'Percent']]  # list of lists....

    for i in range(2, nPeople + 1):  # varying the number of people
        count = 0
        for j in range(nTrials):  # repeating the number of trials
            if myBirthday(i) is True:
                count += 1
        # row of data being calculated
        data = []
        data.append(i)
        data.append(count / nTrials)  # estimate for likelihood percentage
        probData.append(data)  # include a row of data into our list

    with open('birthMatch.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(probData)


if __name__ == "__main__":
    main()
