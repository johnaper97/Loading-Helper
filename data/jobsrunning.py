#importing dependencies
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from .config import *
from .loadinghelper import *
import os
import shutil

#class Jobs Running definition
class JobsRunning:

    #__init__ definition
    def __init__(self, master, config): #need to include the config in definition, since this is a slave to loadinghelper class and doesn't actually initiliaze it itself.
        self.master = master #setting self.master to master 
        master.title("Jobs Entered") #title of window
        self.config = config #setting self.config to config
        master.resizable(0,0) #setting it unresizable.

        #from here on, it's just setting up the gui
        self.jobs_combo = Listbox(master, width=50, selectmode="multiple")
        self.jobs_combo.grid(row=0, column=0, columnspan=2)

        self.queue_combo = Combobox(master)
        self.queue_combo.grid(row=1, column = 0)
        self.queue_combo['values'] = self.config.queue_names

        self.resend_button = Button(master, text="Resend Job", command=self.send)
        self.resend_button.grid(row=1, column=1)

    #send function for sending files.
    #extremely similar to the one in loadinghelper, but I will mark the differences.    
    def send(self):
        
        #checking to see if anything is actually selected, and if so, making it into a list i can play with.
        if len(self.jobs_combo.curselection()) == 0:
            messagebox.showinfo("No Selection!", "Please select some files.") 
            return 0
        else:
            selections = self.jobs_combo.curselection()

        dest_directory = list(filter(lambda a: self.queue_combo.get() in a, self.config.queue_directories))
        for i in range(len(selections)):
            file_to_copy = self.jobs_combo.get(selections[i]) #getting file from the listbox 
            #no need to send the information to the jobs running class, since that's this class, and we don't want to send it again.
            source_file = self.config.output_directory + "\\" + file_to_copy
            shutil.copy2(source_file, dest_directory[0])

        messagebox.showinfo("Files Sent", "The files have been sent!")
