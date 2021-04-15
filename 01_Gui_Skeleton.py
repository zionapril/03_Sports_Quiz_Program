from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self):

        # Formatting Variables
        background_colour = "dark orchid"

        # SAP (SPORTS ANALYSIS PROGRAM) Main Screen GUI
        self.sap_frame = Frame(width=500, height=500, bg=background_colour,
                               pady=10)
        self.sap_frame.grid()

        # SAP Heading (row 0)
        self.sap_label = Label(self.sap_frame, text="SPORTS ANALYSIS PROGRAM",
                               font="Arial 16 bold", bg=background_colour,
                               padx=10, pady=10)
        self.sap_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.sap_frame, text="Help",
                                  font="Arial 14 bold",
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="SPORTS ANALYSIS PROGRAM\n\n"
                                          "This program allows you to check daily "
                                          "results, fixtures, times and events for "
                                          "English Premier League Football.")


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

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sports Analysis Program")
    something = Start()
    root.mainloop()