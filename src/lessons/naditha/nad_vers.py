quiz_question_answer = [{'How many days in the month of Feb?':'28','user_ans': ''},
                        {'how many days in week?':'5', 'user_ans': ''},
                        {'what is September 1st?':'labor day', 'user_ans': ''}]

questions = [
        {
            'question': 'How many days in the month of Feb?', 
            'correct_answer': '28',
            'user_ans': ""
        },
        {
            'question': 'How many days in a week?', 
            'correct_answer': '5',
            'user_ans': ""
        },
        {
            'question': 'xxxxx', 
            'correct_answer': 'Laboxxxr Day',
            'user_ans': ""
        }, 
        {
            'question': 'How is Sept 1?', 
            'correct_answer': 'Labor Day',
            'user_ans': ""
        },        
]

for question in questions:
    question['user_ans'] = input(question['question'])
    if question['user_ans'] == question['correct_answer']:
        print("Correct")
    else:
        print("incorrect")

print(questions)




"""print(q_and_a['question'])
print(q_and_a['correct_answer'])

q_and_a['user_ans'] = "xyz"
q_and_a['xxxxxxx'] = 99999

print(q_and_a)
"""

"""q_and_a['user_ans'] = input(q_and_a['question'])

if int(q_and_a['user_ans']) != q_and_a['correct_answer']:
    print("YOU GOT IT WRONG!!!")
else:
    print("CORRECT!!!!")
    
print(q_and_a)"""


"""for question in quiz_question_answer:
    for key in question:
            real_ans=question[key]
            print(f"what is the answer for {key}")
            user_ans=input("type answer")
            question['user_ans'] = user_ans
            print(f"Printing the dict with updated user_ans value {question}")
            if user_ans==real_ans:
                print("correct")
            else:
                print(f"answer is not {user_ans} , it is {real_ans}")
                
                
person = {'name': 'andy', 'age': 43}"""



numbers =[{}, {}, {}]

