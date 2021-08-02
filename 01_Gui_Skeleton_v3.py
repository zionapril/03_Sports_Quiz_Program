from tkinter import *
from functools import partial, wraps   # To prevent unwanted windows
import random
import csv
import re


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
        # self.balance = IntVar()

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
        self.num_correct = IntVar()
        self.num_correct.set(0)

        # Initialise list to hold Quiz History
        self.all_quiz_list = []

        self.played = 0

        self.correct_ans = StringVar()
        self.question_asked = StringVar()

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
                                    wrap=200,
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

        self.answer_1_button.config(state=DISABLED)
        self.answer_2_button.config(state=DISABLED)
        self.answer_3_button.config(state=DISABLED)
        self.answer_4_button.config(state=DISABLED)

        # Next Question Button
        self.next_question_btn = Button(self.answer_frame, text="Next Question",
                                        bg="white", width=11, height=1,
                                        font="Arial 10 bold",
                                        command=self.next_question
                                        )
        self.next_question_btn.grid(row=5, column=0, pady=10)

        self.history_button = Button(self.answer_frame, text="Quiz History",
                                     bg="white", width=15, height=1,
                                     font="Arial 10 bold",
                                     command=lambda:self.history(self.all_quiz_list))
        self.history_button.grid(row=5, column=1, pady=10)

        self.history_button.config(state=DISABLED)

        # if self.played != 10:
        #     self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        num_correct = self.num_correct.get()
        History(self, calc_history, num_correct)

    def next_question(self):

        correct_answer = ""
        answer_options = ""
        question_cat = [
            "team", "stadium", "nickname"
        ]
        self.played +=1

        print("Question {}".format(self.played))

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
            question = "What is {}'s nickname? ".format(question_answer[0])
            hint = question_answer[2]
            question = "{} Hint: {}".format(question, hint)
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
        self.question_asked.set(question)

        for item in range(0, 3):
            answer_options = random.choice(data[1:])

            if category_choice == "nickname":
                ans_opt = answer_options[3]
            else:
                ans_opt = answer_options[0]

            answer_choices.append(ans_opt)
            print()

        print()

        random.shuffle(answer_choices)


        self.answer_1_button.config(state=NORMAL, text="{}".format(answer_choices[0]))
        self.answer_2_button.config(state=NORMAL, text="{}".format(answer_choices[1]))
        self.answer_3_button.config(state=NORMAL, text="{}".format(answer_choices[2]))
        self.answer_4_button.config(state=NORMAL, text="{}".format(answer_choices[3]))

    def check(self, position):

        ans = ""
        number_correct = 0

        correct_answer = self.correct_ans.get()
        print("Correct Answer: ", correct_answer)

        if position == 1:
            # get what's in the button
            ans = self.answer_1_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_1_button.config(state=DISABLED)
            self.answer_2_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)
            self.history_button.config(state=DISABLED)

        elif position == 2:
            ans = self.answer_2_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_1_button.config(state=DISABLED)
            self.answer_2_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)
            self.history_button.config(state=DISABLED)

        elif position == 3:
            ans = self.answer_3_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_1_button.config(state=DISABLED)
            self.answer_2_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)
            self.history_button.config(state=DISABLED)

        elif position == 4:
            ans = self.answer_4_button.cget('text')
            print("Your Answer: ", ans)
            self.answer_1_button.config(state=DISABLED)
            self.answer_2_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)
            self.history_button.config(state=DISABLED)

        if correct_answer == ans:
            self.history_button.config(state=DISABLED)
            self.question_label.config(text="Correct", fg="green")
            number_correct = self.num_correct.get()
            number_correct += 1
            self.num_correct.set(number_correct)

        else:
            self.history_button.config(state=DISABLED)
            self.question_label.config(text="Incorrect", fg="red")

        if self.played == 10:
            self.next_question_btn.config(state=DISABLED)
            self.answer_1_button.config(state=DISABLED)
            self.answer_2_button.config(state=DISABLED)
            self.answer_3_button.config(state=DISABLED)
            self.answer_4_button.config(state=DISABLED)
            self.history_button.config(state=NORMAL)
            print("------------------------------------")
            print("You got {} out of 10".format(number_correct))
            self.question_label.config(text="You got {} out of 10"
                                            .format(number_correct))
            print("You have completed the quiz!!!")

        # Add Answer to list for History

        get_question = self.question_asked.get()




        if ans != "yes":

            self.all_quiz_list.append("Question: {}\n"
                                      "Your Answer: {}\n"
                                      "Correct Answer:{}\n\n"
                                      "You got out {} of 10\n\n"
                                      .format(get_question, ans, correct_answer, number_correct)
                                      )
            # self.history_button.config(state=NORMAL)


class History:
    def __init__(self, partner, calc_history, num_correct, ):

        print(calc_history)

        background = "#C0C0C0"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Quiz Results",
                                 font="arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="You got {} out of 10."
                                       .format(num_correct), wrap=250,
                                  font="arial 10 italic",
                                  justify=LEFT, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  width=10, font="arial 12 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back ro normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):

        background = "#C0C0C0"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "and press the Save "
                                                         "button to save your "
                                                         "calculation history "
                                                         "to a text file.",
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning Text (row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your calculation "
                                                         "history",
                                 justify=LEFT, width=10, bg="#ffafaf", fg="maroon", font="arial 10 italic",
                                 wrap=225, padx=70, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 10 bold",
                                    justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # heading...
            f.write("Premier League Quiz History\n\n")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Premier League Quiz Program")
    something = Start()
    root.mainloop()
