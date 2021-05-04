from tkinter import *
from tkinter.ttk import *
from functools import partial   # To prevent unwanted windows
from PIL import ImageTk,Image
import random


class Start:
    def __init__(self):

        # Formatting Variables
        background_colour = "DarkOrchid1"

        # Sports Quiz Main Screen GUI
        self.sports_quiz_frame = Frame(width=500, height=500, bg=background_colour,
                               pady=10)
        self.sports_quiz_frame.grid()

        # SAP Heading (row 0)
        self.quiz_label = Label(self.sports_quiz_frame, text="ENGLISH PREMIER LEAGUE QUIZ",
                               font="Arial 16 bold", bg=background_colour,
                               padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.sports_quiz_frame, text="Help",
                                  font="Arial 14 bold",
                                  command=self.help, bg="pale green")
        self.help_button.grid(row=1, column=0, padx=2)

        # Play Button (row 1)
        self.play_button = Button(self.sports_quiz_frame, text="Play",
                                  font="Arial 14 bold", bg="yellow",
                                  command=self.play)
        self.play_button.grid(row=2, column=0, padx=2)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="ENGLISH PREMIER LEAGUE QUIZ\n\n"
                                          "This program consists of a bunch of "
                                          "questions about EPL teams :)")

    def play(self):
        Game(self)


class Help:
    def __init__(self, partner):

        background_colour = "pale green"

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
        self.help_text = Label(self.help_frame, text="",
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


class Game:
    def __init__(self, partner):

        background_colour= "DarkOrchid1"
        # initialise variables
        self.balance = IntVar()

        # disable play button
        partner.play_button.config(state=DISABLED)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box, width=300, height=300, bg=background_colour)
        self.game_frame.grid()

        # If users press cross at top, closes help and 'releases' help button
        self.game_box.protocol('WM_DELETE_WINDOW', partial(self.close_game, partner))

        # Heading Row
        self.heading_label = Label(self.game_frame, text="QUIZ TIME !!!",
                                   bg=background_colour,
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Club nickname Button
        photo = PhotoImage(file =  )
        self.club_nicknames_button = Button(self.game_frame, text= 'Club Nicknames!',
                                            image = photo).pack(side = BOTTOM)
        # Stadiums Button
        # Managers Button

        # Dismiss Button (row 2)
        self.dismiss_button = Button(self.game_frame, text="Dismiss",
                                     width=10, bg="white", font="arial 10 bold",
                                     command=partial(self.close_game, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_game(self, partner):
        # Put Play button back to normal...
        partner.play_button.config(state=NORMAL)
        self.game_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Premier League Quiz Program")
    something = Start()
    root.mainloop()