from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


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
                                      font="Arial 9 bold")
        self.stadiums_button.grid(row=2, column=1, pady=10)
        # Managers Button
        self.managers_button = Button(self.quiz_button_frame, text="PL Club\n"
                                                                   "Managers",
                                      width=10, bg="white", font="Arial 9 bold")
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
    def __init__(self, partner, prompt, answer):

        # initialise variables
        self.balance = IntVar()
        self.prompt = prompt
        self.answer = answer

        # GUI Setup
        self.game_box = Toplevel()

        background_colour = "#C0C0C0"

        '''# If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)'''
        self.game_frame = Frame(self.game_box, bg=background_colour)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Premier League Club Nicknames",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Questions
        question_prompts = ["What is the nickname for Manchester Utd\n"
                            "(a)Red Devils \n"
                            "(b)Reds",]

        questions = [
            Question(question_prompts[0], "a"),
            Question(question_prompts[1], "b"),
                    ]

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Premier League Quiz Program")
    something = Start()
    root.mainloop()