from tkinter import *
from functools import partial   # To prevent unwanted windows
import random
import csv

with open('03_Sports_Quiz_Program\\team_stadium.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


class Start:
    def __init__(self):

        background_colour= "#C0C0C0"
        # initialise variables
        self.balance = IntVar()

        # GUI Setup
        self.game_frame = Frame(bg=background_colour)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Premier League Quiz",
                                   bg=background_colour,
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Picture frames go here
        self.picture_frame = Frame(self.game_frame)
        self.picture_frame.grid(row=1, pady=10)

        photo = PhotoImage(file="Pl nicknames.gif")

        self.picture_label = Label(self.picture_frame,
                                   image=photo, padx=10, pady=10)
        self.picture_label.photo = photo
        self.picture_label.grid(row=2, column=0)

        # Quiz Button frame
        self.quiz_button_frame = Frame(self.game_frame, bg=background_colour)
        self.quiz_button_frame.grid(row=2, pady=10)
        # Club nickname Button
        self.club_nickname_button = Button(self.quiz_button_frame, text="PL Club\n"
                                                                        "Nicknames",
                                           width=10, bg="white",
                                           font="Arial 9 bold",
                                           command=self.nickname)
        self.club_nickname_button.grid(row=2, column=0, pady=10)

        # Stadiums Button
        self.stadiums_button = Button(self.quiz_button_frame, text="PL Club\n"
                                                                   "Stadiums",
                                      width=10, bg="white",
                                      font="Arial 9 bold",
                                      command=self.stadium)
        self.stadiums_button.grid(row=2, column=1, pady=10)
        # Managers Button
        self.managers_button = Button(self.quiz_button_frame, text="PL Club\n"
                                                                   "Managers",
                                      width=10, bg="white", font="Arial 9 bold",
                                      command=self.manager)
        self.managers_button.grid(row=2, column=2, pady=10)

        # Help button
        self.help_button = Button(self.quiz_button_frame, text="Help",
                                  width=10, bg="white", font="arial 9 bold",
                                  command=self.help)
        self.help_button.grid(row=3, column=1, pady=10)

    def help(self):
        Help(self)

    def nickname(self):
        Nicknames(self)

    def stadium(self):
        Stadiums(self)

    def manager(self):
        Managers(self)


class Help:
    def __init__(self, partner):

        background_colour = "#C0C0C0"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background_colour)
        self.help_frame.grid()

        # Set Up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold", bg=background_colour)
        self.how_heading.grid(row=0)

        # Help Text(label, row 1)
        self.help_text = Label(self.help_frame, text="Before you continue !\nThese are the different topics:\n"
                                                     "Club Nicknames - Pick the correct "
                                                     "nickname for the club given.\n"
                                                     "\nStadiums - Pick the correct stadium "
                                                     "for the club given.\n"
                                                     "\nEach Topic will consist of 10 questions.\n"
                                                     "Good luck !!!",
                               justify=LEFT, width=40, bg=background_colour, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss Button (row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                     width=10, bg="white", font="arial 10 bold",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2,pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Nicknames:
    def __init__(self, partner):

        # initialise variables
        self.balance = IntVar()

        # GUI Setup
        self.game_box = Toplevel()

        background_colour = "#C0C0C0"

        '''# If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)'''
        self.game_frame = Frame(self.game_box, bg=background_colour)
        self.game_frame.grid()           

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Premier League Club Nicknames",
                                   bg=background_colour,
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Question Frame
        self.question_frame = Frame(self.game_frame, bg=background_colour)
        self.question_frame.grid(row=2, pady=10)

        # Question Label
        self.question_label = Label(self.question_frame, text="Push 'next' to start",
                                    bg=background_colour,
                                    font="Arial 20 bold", padx=10,
                                    pady=10)
        self.question_label.grid(row=2, pady=10)

        # Frame and Button for multiple choice answers
        self.answer_frame = Frame(self.game_frame, bg=background_colour)
        self.answer_frame.grid(row=3, pady=10)

        # Answer 1 Button
        self.answer_1_button = Button(self.answer_frame, text="",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_1_button.grid(row=3, column=0, pady=10)

        # Answer 2 Button
        self.answer_2_button = Button(self.answer_frame, text="",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_2_button.grid(row=3, column=1, pady=10)

        # Answer 3 Button
        self.answer_3_button = Button(self.answer_frame, text="",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_3_button.grid(row=4, column=0, pady=10)

        # Answer 4 Button
        self.answer_4_button = Button(self.answer_frame, text="",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_4_button.grid(row=4, column=1, pady=10)

        # Next Question Button
        self.next_question_btn = Button(self.answer_frame, text="Next Question",
                                        bg="white", width=11, height=1,
                                        font="Arial 10 bold",
                                        command = self.nextquestion
                                        )
        self.next_question_btn.grid(row=5, column=0, pady=10)

    def nextquestion(self):
        #  self.question_label = Label(self.question_frame, text="",
        #                              bg="#C0C0C0",
        #                              font="Arial 20 bold", padx=10,
        #                              pady=10)
        #  self.question_label.grid(row=2, pady=10)

        question_cat = [
            "team", "stadium", "nickname"
        ]

        for item in range(1, 4):
            question_answer = random.choice(data)

            category_choice = random.choice(question_cat)
            answer = question_answer[0]

            answer_choices = []

            if category_choice == "team":
                q_ans_index = 1
                question = "What team plays in {}? ".format(question_answer[1])
                team_q = question
            

            elif category_choice == "nickname":
                q_ans_index = 3
                to_ask = "What is {}'s nickname? ".format(question_answer[0])
                hint = question_answer[2]
                question = "{} Hint: {}".format(to_ask, hint)
                correct_answer = question_answer[3]
                nickname_q = question
            else:
                question = "Which team is based in {}".format(question_answer[1])
                correct_answer = question_answer[0]
                q_ans_index = 2

            self.question_label.config(text=question)

            for item in range(0,3):
                answer_options = random.choice(data)
                # Row which includes the team, stadium, nickname
                print("Answer options row", answer_options)
                print("answer 1: {}".format)(answer_choices[0])
                ans_opt = answer_options[0]
                # Answer 
                print("Answer Option", ans_opt)
                # Answer choices (4) which go to answer buttons
                answer_choices.append(ans_opt)
                print()

            answer_choices.append(answer)

            print(question)
            print(answer)

            print()
            print("Choices...")
            print(answer_choices)



class Stadiums:
    def __init__(self, partner):

        # initialise variables
        self.balance = IntVar()

        # GUI Setup
        self.game_box = Toplevel()

        background_colour = "#C0C0C0"

        '''# If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)'''
        self.game_frame = Frame(self.game_box, bg=background_colour)
        self.game_frame.grid()

        question_cat = [
            "team", "stadium", "nickname clue", "nickname"
        ]

        for item in range(1, 4):
            question_answer = random.choice(data)

            category_choice = random.choice(question_cat)
            answer = question_answer[0]

            answer_choices = []

            if category_choice == "team":
                q_ans_index = 1
                question = "What team plays in {}? ".format(question_answer[1])
                team_q = question
            

            elif category_choice == "nickname":
                q_ans_index = 3
                question = "What team is associated with {}? ".format(question_answer[3])
                nickname_q = question
            else:
                question = "Hints available: {} ".format(question_answer[2])
                q_ans_index = 2

            for item in range(0,4):
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

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Premier League Club Stadiums",
                                   bg=background_colour,
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Question Frame
        self.question_frame = Frame(self.game_frame, bg=background_colour)
        self.question_frame.grid(row=2, pady=10)

        # Question Label
        self.question_label = Label(self.question_frame, text=team_q,
                                    bg=background_colour,
                                    font="Arial 20 bold", padx=10,
                                    pady=10)
        self.question_label.grid(row=2, pady=10)

        # Frame and Button for multiple choice answers
        self.answer_frame = Frame(self.game_frame, bg=background_colour)
        self.answer_frame.grid(row=3, pady=10)

        # Answer 1 Button
        self.answer_1_button = Button(self.answer_frame, text="Answer 1",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_1_button.grid(row=3, column=0, pady=10)

        # Answer 2 Button
        self.answer_2_button = Button(self.answer_frame, text="Answer 2",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_2_button.grid(row=3, column=1, pady=10)

        # Answer 3 Button
        self.answer_3_button = Button(self.answer_frame, text="Answer 3",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_3_button.grid(row=4, column=0, pady=10)

        # Answer 4 Button
        self.answer_4_button = Button(self.answer_frame, text="Answer 4",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_4_button.grid(row=4, column=1, pady=10)

        # Next Question Button
        self.next_question_btn = Button(self.answer_frame, text="Next Question",
                                        bg="white", width=11, height=1,
                                        font="Arial 10 bold")
        self.next_question_btn.grid(row=5, column=0, pady=10)


class Managers:
    def __init__(self, partner):

        # initialise variables
        self.balance = IntVar()

        # GUI Setup
        self.game_box = Toplevel()

        background_colour = "#C0C0C0"

        '''# If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)'''
        self.game_frame = Frame(self.game_box, bg=background_colour)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Premier League Club Managers",
                                   bg=background_colour,
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Question Frame
        self.question_frame = Frame(self.game_frame, bg=background_colour)
        self.question_frame.grid(row=2, pady=10)

        # Question Label
        self.question_label = Label(self.question_frame, text="Question",
                                    bg=background_colour,
                                    font="Arial 20 bold", padx=10,
                                    pady=10)
        self.question_label.grid(row=2, pady=10)

        # Frame and Button for multiple choice answers
        self.answer_frame = Frame(self.game_frame, bg=background_colour)
        self.answer_frame.grid(row=3, pady=10)

        # Answer 1 Button
        self.answer_1_button = Button(self.answer_frame, text="Answer 1",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_1_button.grid(row=3, column=0, pady=10)

        # Answer 2 Button
        self.answer_2_button = Button(self.answer_frame, text="Answer 2",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_2_button.grid(row=3, column=1, pady=10)

        # Answer 3 Button
        self.answer_3_button = Button(self.answer_frame, text="Answer 3",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_3_button.grid(row=4, column=0, pady=10)

        # Answer 4 Button
        self.answer_4_button = Button(self.answer_frame, text="Answer 4",
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold")
        self.answer_4_button.grid(row=4, column=1, pady=10)

        # Next Question Button
        self.next_question_btn = Button(self.answer_frame, text="Next Question",
                                        bg="white", width=11, height=1,
                                        font="Arial 10 bold")
        self.next_question_btn.grid(row=5, column=0, pady=10)
        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Premier League Quiz Program")
    something = Start()
    root.mainloop()