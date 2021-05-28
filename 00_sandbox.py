import random

data = [

["yellow", "sun", "cowardice", "happyness"],
["green", "grass", "jealousy", "nature"],
["blue", "sky", "depression", "calm"]

]

question_cat = [
    "object", "positive", "negative"
]


for item in range(1, 10):
    question_answer = random.choice(data)

    category_choice = random.choice(question_cat)
    answer = question_answer[0]

    if category_choice == "object":
        question = "What colour is {}? ".format(question_answer[1])
    elif category_choice == "positive":
        question = "What colour is associated with {}? ".format(question_answer[3])
    else:
        question = "What colour is associated with {}? ".format(question_answer[2])

    print(question)
    print(answer)


     