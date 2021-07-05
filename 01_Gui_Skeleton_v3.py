from tkinter import *
from functools import partial, wraps   # To prevent unwanted windows
import random
import csv


# with open('03_Sports_Quiz_Program\\team_stadium.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)

with open('team_stadium.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    random.shuffle(data[1:])


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
        # Play Button
        self.club_nickname_button = Button(self.quiz_button_frame, text="Play",
                                           width=10, bg="white",
                                           font="Arial 9 bold",
                                           command=self.quiz)
        self.club_nickname_button.grid(row=2, column=0, pady=10)

        # Help button
        self.help_button = Button(self.quiz_button_frame, text="Help",
                                  width=10, bg="white", font="arial 9 bold",
                                  command=self.help)
        self.help_button.grid(row=2, column=1, pady=10)

    def help(self):
        Help(self)

    def quiz(self):
        Play(self)


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
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Play:
    def __init__(self, partner):

        # initialise variables
        self.balance = IntVar()
        self.played = 0

        self.correct_ans = StringVar()

        # GUI Setup
        self.game_box = Toplevel()

        background_colour = "#C0C0C0"

        '''# If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)'''
        self.game_frame = Frame(self.game_box, bg=background_colour)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Premier League Quiz",
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
        self.answer_1_button = Button(self.answer_frame, text="", wrap=100,
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold", command=lambda:self.check(1))
        self.answer_1_button.grid(row=3, column=0, pady=10)

        # Answer 2 Button
        self.answer_2_button = Button(self.answer_frame, text="", wrap=100,
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold", command=lambda:self.check(2))
        self.answer_2_button.grid(row=3, column=1, pady=10)

        # Answer 3 Button
        self.answer_3_button = Button(self.answer_frame, text="", wrap=100,
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold", command=lambda:self.check(3))
        self.answer_3_button.grid(row=4, column=0, pady=10)

        # Answer 4 Button
        self.answer_4_button = Button(self.answer_frame, text="", wrap=100,
                                      bg="white", width=15,
                                      height=5,
                                      font="Arial 10 bold", command=lambda:self.check(4))
        self.answer_4_button.grid(row=4, column=1, pady=10)

        # Next Question Button
        self.next_question_btn = Button(self.answer_frame, text="Next Question",
                                        bg="white", width=11, height=1,
                                        font="Arial 10 bold",
                                        command=self.next_question
                                        )
        self.next_question_btn.grid(row=5, column=0, pady=10)

    def next_question(self):

        #  self.question_label = Label(self.question_frame, text="",
        #                              bg="#C0C0C0",
        #                              font="Arial 20 bold", padx=10,
        #                              pady=10)
        #  self.question_label.grid(row=2, pady=10)

        correct_answer = ""
        answer_options = ""
        question_cat = [
            "team", "stadium", "nickname"
        ]
        self.played +=1
        print(self.played)

        #if self.played == 10:
            #self.next_question_btn.config(state=DISABLED)
            #print("You got {} out of 10".format(self.correct_ans))
            #print("You have completed the quiz!!!")

        question_answer = random.choice(data[1:])

        category_choice = random.choice(question_cat)
        if category_choice == "team":
            answer = question_answer[0]
        else:
            answer = question_answer[3]

        answer_choices = []
        if category_choice == "team":
            q_ans_index = 1
            question = "What team plays in {}? ".format(question_answer[1])
            correct_answer = question_answer[0]

            # store correct answer as string variable (use .set)
            self.correct_ans.set(correct_answer)

            print(question)
            print("Answer: ", correct_answer)
            print("Choices...")
            answer_choices.append(correct_answer)
            print(answer_choices)

        elif category_choice == "nickname":
            q_ans_index = 3
            to_ask = "What is {}'s nickname? ".format(question_answer[0])
            hint = question_answer[2]
            question = "{} Hint: {}".format(to_ask, hint)
            correct_answer = question_answer[3]
            print(question)
            print("Answer: ", correct_answer)
            print("Choices...")
            answer_choices.append(correct_answer)
            print(answer_choices)
            # store correct answer as string variable (use .set)
            self.correct_ans.set(correct_answer)

        else:
            question = "Which team is based in {}".format(question_answer[1])
            correct_answer = question_answer[0]
            print(question)
            # store correct answer as string variable (use .set)
            self.correct_ans.set(correct_answer)
            print("Answer: ", correct_answer)
            print("Choices...")
            answer_choices.append(correct_answer)
            print(answer_choices)

        self.question_label.config(text=question, fg="black")

        for item in range(0, 3):
            answer_options = random.choice(data[1:])

            if category_choice == "nickname":
                ans_opt = answer_options[3]
            else:
                ans_opt = answer_options[0]

            # # Row which includes the team, stadium, nickname
            # print("Answer options row", answer_options)
            # ans_opt = answer_options[0]
            # # Answer
            # print("Answer Option", ans_opt)
            # # Answer choices (4) which go to answer buttons
            answer_choices.append(ans_opt)
            print()

        # answer_choices.append(correct_answer)

        # print("Answer Row:", answer_choices)

        # print(question)
        # print("Answer: ",answer)

        print()
        # print("Choices...")
        # print(answer_choices)
        self.answer_1_button.config(state=NORMAL, text="{}".format(answer_choices[0]))
        self.answer_2_button.config(state=NORMAL, text="{}".format(answer_choices[1]))
        self.answer_3_button.config(state=NORMAL, text="{}".format(answer_choices[2]))
        self.answer_4_button.config(state=NORMAL, text="{}".format(answer_choices[3]))

    def check(self, position):

        ans = ""

        correct_answer = self.correct_ans.get()
        print("Correct Answer: ", correct_answer)

        if position == 1:
            # get what's in the button
            ans = self.answer_1_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_2_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)

        elif position == 2:
            ans = self.answer_2_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_1_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)

        elif position == 3:
            ans = self.answer_3_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_1_button.config(state=DISABLED)
            self.answer_2_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)

        elif position == 4:
            ans = self.answer_4_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_1_button.config(state=DISABLED)
            self.answer_2_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)


        #self.question_label.config(text="Correct Answer: {}\n"
                                        #"Your Answer: {}".format(correct_answer, ans))

        if correct_answer == ans:
            self.question_label.config(text="Correct", fg="green")

        else:
            self.question_label.config(text="Incorrect", fg="red")

        if self.played == 10:
            self.next_question_btn.config(state=DISABLED)
            print("------------------------------------")
            print("You got {} out of 10".format(self.correct_ans))
            print("You have completed the quiz!!!")











        # Get the string answer
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Premier League Quiz Program")
    something = Start()
    root.mainloop()
