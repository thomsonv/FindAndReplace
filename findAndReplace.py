""" 1/25/2018:
Problem: Have loads of log files with multiple 'keys'.
But the log file processing tool does not recognize 'key' strings but wants 'code' strings!

Solution: Write a python based tool, were a user can define list of strings that they want
replaced over mutiple files in one directory """

#import tkinter as tk
import os
import fileinput
from tkinter import Tk, Label, Button

class userInterface:
    def __init__(self, master):
        self.master = master
        master.title("Find and Replace")

        self.label = Label(master, text="Once stop shop for 'Find and Replace'")
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

root = Tk()
my_gui = userInterface(root)
root.mainloop()
