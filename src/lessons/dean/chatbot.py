

questions_and_answers = {
    "hello": "hello, how are you?",
    "andy": "you must be andy",
    "bye": "thanks for chatting",
}

"""for word, question in questions_and_answers.items():
    print(word)
    print(question)"""


while True:
    answer = input("? ")
    answer = answer.split(" ")
    for word in answer:
        word = word.lower()
        if word == "bye":
            exit()
        if word in questions_and_answers:
            print(questions_and_answers[word])
