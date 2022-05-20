print("hello")

questions = ("Why ", "How ", "What ", "When ")


answers = []

for question in questions:
    answer = input(question)
    answers.append(answer)

print(answers)

print(questions[0], answers[0])
