operation = input("which operation would you like to do?(1 for addition, 2 for subtraction)? ")
term1 = int(input("what is your first number? "))
term2 = int(input("what is your second number? "))

if operation =="1":
    answer = term1++term2
if operation =="2":
    answer = term1 - term2


print("Your answer is: "+str(answer))
