# hmwk5Q5

import csv
from random import randint


def main():
    '''Call our function and produce a csv file named anyBirthday.csv. '''

    trials = 1000
    N = 100

    probData = [['People', 'Percent']]  # This is a list in a list.

    for i in range(2, 101):
        sumoftruebirthdays = 0
        for j in range(trials):
            if anyBirthday(i) == True:
                sumoftruebirthdays += 1

        data = []  # empty list
        data.append(i)  # Append all the number of people
        data.append(sumoftruebirthdays / trials)  # percentage probability
        probData.append(data)

    with open('anyBirthday.csv', 'w', newline='') as file:  # Creates csv file.
        writer = csv.writer(file)
        writer.writerows(probData)


def anyBirthday(N):
    '''Single trial of a group of N people in the room. Function returns True or False.'''
    a = []  # empty list

    for i in range(0, N):  # forloop for number of people.
        l = randint(1,
                    365)  # variable will be equal to a random number from range 1 to 365
        a.append(l)  # We will append the random numbers to list
    if len(a) == len(list(set(
            a))):  # Set will help identify the unique birthdates and seperate duplicates.
        return False  # Return False if no birthdate match. Return True if there was a match.
    else:
        return True


if __name__ == "__main__":
    main()
