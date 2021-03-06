import random
import csv


with open('03_Sports_Quiz_Program\\team_stadium.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

question_cat = [
    "team", "stadium", "nickname clue", "nickname"
]


for item in range(1, 3):
    question_answer = random.choice(data)

    category_choice = random.choice(question_cat)
    answer = question_answer[0]

    answer_choices = []

    if category_choice == "team":
        q_ans_index = 1
        question = "What team plays in {}? ".format(question_answer[1])

    elif category_choice == "nickname":
        q_ans_index = 3
        question = "What team is associated with {}? ".format(question_answer[3])
    else:
        question = "Hints available: {} ".format(question_answer[2])
        q_ans_index = 2

    for item in range(0,3):
        answer_options = random.choice(data)
        print("Answer options row", answer_options)
        ans_opt = answer_options[0]
        print("Answer Option", ans_opt)
        answer_choices.append(ans_opt)
        print()

    answer_choices.append(answer)

    print(question)
    print(answer)

    print()
    print("Choices...")
    print(answer_choices)

