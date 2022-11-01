# Jena Vallina Week 9 Lab Quiz Score List
sum = int()
count = int()
num_scores = int()
minimum = int()
maximum = int()
grade = str()
scores_list = list()
grades = list()

sum = 0
count = 0
minimum = 100
maximum = 0
grade = ""


def getScore():
    score = int()
    score = int(input("Enter a quiz score: "))
    return score


def getAvg(sum, count):
    average = float()
    if sum == 0:
        average = 0
    else:
        average = float(sum) / count
    return average


num_scores = int(input("Total number of scores: "))
while count < num_scores:
    score = getScore()
    scores_list.append(score)
    sum = sum + score
    count = count + 1

print("sum is ", sum, "count is ", count)
average = getAvg(sum, count)
print("average is", average)

count = 0
grades = [0, 0, 0, 0, 0]
while count < num_scores:
    if scores_list[count] <= 59:
        grades[4] += 1
    elif scores_list[count] <= 70:
        grades[3] += 1
    elif scores_list[count] <= 80:
        grades[2] += 1
    elif scores_list[count] <= 90:
        grades[1] += 1
    else:
        grades[0] += 1
    count = count + 1

print("Number of A Grades", grades[0])
print("Number of B Grades", grades[1])
print("Number of C Grades", grades[2])
print("Number of D Grades", grades[3])
print("Number of F Grades", grades[4])

# extra credit...

count = 0
while count < num_scores:
    if scores_list[count] < minimum:
        minimum = scores_list[count]
    if scores_list[count] > maximum:
        maximum = scores_list[count]
    count = count + 1

print("Minimum is ", minimum, "Maximum is ", maximum)
