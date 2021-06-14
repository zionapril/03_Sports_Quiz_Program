import random

data = [

['Arsenal ', 'Emirates Stadium ', '', 'The Gunners'],
['Aston Villa ', 'Villa Park ', 'One word, 5 letters', 'Villa'],
['Brighton & Hove Albion ', 'Falmer Stadium ', 'The bird, not the place', 'The Seagulls'],
['Burnley ', 'Turf Moor ', '', 'The Clarets'],
['Chelsea ', 'Stamford Bridge ', 'The colour', 'The Blues'],
['Crystal Palace ', 'Selhurst Park ', 'The bird', 'The Eagles'],
['Everton ', 'Goodison Park ', 'The sweet treat', 'The Toffees'],
['Fulham ', 'Craven Cottage ', 'Colour of kit', 'Whites'],
['Leeds United ', 'Elland Road ', '8 lettered animal', 'The Peacocks'],
['Leicester City ', 'King Power Stadium ', 'Animal On the badge', 'The Foxes'],
['Liverpool ', 'Anfield ', 'Colour of kit', 'The Reds'],
['Manchester City ', 'City of Manchester Stadium ', '', 'City'],
['Manchester United ', 'Old Trafford ', '', 'The Red Devils'],
['Newcastle United ', "St James' Park ", '', 'The Magpies'],
['Sheffield United ', 'Bramall Lane ', '', 'The Blades'],
['Southampton ', "St Mary's Stadium ", '', 'The Saints'],
['Tottenham Hotspur ', 'Tottenham Hotspur Stadium ', '', 'Spurs'],
['West Bromwich Albion ', 'The Hawthorns ', '', 'The Hammers'],
['West Ham United ', 'London Stadium ', '', 'Albion'],
['Wolverhampton Wanderers ', 'Molineux Stadium ', '', 'The Wanderers']

]

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
        question = "Hints available: {}? ".format(question_answer[2])
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

