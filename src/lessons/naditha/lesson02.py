questions = (
    (
        "q1", 
        "a2",
        "a1",
    ), 
    (
        "q2", 
        "77",

    )
)

numbers = (1, 2)
print(type(numbers))

names = ("fred", "bert")

# names[1] = "andy"
print(names[1])

car = {'model': "toyota", 'color': "red", 'price': 1200}
print(car['color'])

q_and_a = {'question': "How long?", 'correct_ans': "32", 'user_ans': ""}

q_and_a['user_ans'] = input(q_and_a['question'])
print(q_and_a)