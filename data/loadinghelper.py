#importing dependencies
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from .config import *
from .jobsrunning import *
import os
import shutil

#class definition for loading helper.
class LoadingHelper:
    def __init__(self, master):
        self.master = master #setting the class master to the value of master(root in the main function)
        self.config = Config() #creating a Config object, so that we have all the data from that file.
        master.title("Loading Helper") #setting title
        master.resizable(0,0) #setting it unresizable.

        #from here, it's all gui stuff. I'll  annotate the special bits.
        self.prod_label = Label(master, text="Product Code:")    
        self.prod_label.grid(row = 0, column=0)

        self.prod_combo = Combobox(master, values = sorted(self.config.product_codes))
        self.prod_combo.grid(row=0, column=1, columnspan=2)

        self.prod_button = Button(master, text="Look Up", command=lambda: self.jobs_list(self.prod_combo.get())) #lambda function is actually only being used because you can't call a function with an argument without doing that AFAIK.
        self.prod_button.grid(row=0, column=3)

        self.job_listbox = Listbox(master, width=50, selectmode= "multiple")
        self.job_listbox.grid(row=1, column=0, rowspan=5, columnspan=2, sticky="NSEW")

        self.select_all_button = Button(master, text="Select All", command= self.select_all)
        self.queue_label = Label(master, text="Queue:")
        self.queue_combo = Combobox(master)
        self.queue_combo['values'] = self.config.queue_names #getting the values for our combo box from the queue names variable in our config object

        self.select_all_button.grid(row=1, column=3)
        self.queue_label.grid(row=2, column=3)
        self.queue_combo.grid(row=3, column=3)

        self.send_button = Button(master, text="Send", command=self.send)
        self.send_button.grid(row=6, column=0, columnspan=4)    

        self.load_top_level()  

    #loading the other window
    def load_top_level(self):
        global jobs_running #need this to have a scope where I can access it later on.
        jobs_running = JobsRunning(Toplevel(), self.config) #creating a child window with the class JobsRunning and passing it the config.

    #jobs_list function
    def jobs_list(self, code): #code is product code.
        self.job_listbox.delete(0, END) #clearing the box upon running this function, else new files would stack on top of old command in the job listbox and that's not the intent
        file_list = os.listdir(self.config.output_directory) #getting all the files in our directory. I can imagine this would get quite hard once you had a LOT of files, but I couldn't find a more efficient way to do it.
        #filter and the lambda look for instances of the code in the file names and collect them
        #the list converts them to a list.
        matchedlist = list(filter(lambda x: code in x, file_list)) 
        matchedlist = sorted(matchedlist) #sorting that list.
        self.job_listbox.insert(END, *matchedlist) #populating the list box with all the filenames.

    #select all function
    def select_all(self):
        for i in range(self.job_listbox.size()): #seeing how many items are in the box
            #i'm actually not completely sure why I have to do all three of these.
            #it seems like activate would be enough to choose a selection, but the other two play a function in highlighting it aswell.
            self.job_listbox.activate(i) 
            self.job_listbox.selection_set(i)
            self.job_listbox.selection_anchor(i)

    #send function
    def send(self):

        #checking if something has been selected in the list box.
        if len(self.job_listbox.curselection()) == 0: #if not, show error, and return 0 so it breaks out of the function.
            messagebox.showinfo("No Selection!", "Please select some files.") 
            return 0
        else:  #if it HAS been selected, we set this variable to the selections so I can play with them.
            selections = self.job_listbox.curselection()

        #getting the destination directory. this lambda and filter combo works the exact same as before.
        #it wouldn't let me do it without the list. 
        dest_directory = list(filter(lambda a: self.queue_combo.get() in a, self.config.queue_directories))
        
        #for loop to go through all the selections
        for i in range(len(selections)):
            file_to_copy = self.job_listbox.get(selections[i]) #getting the value from the list box 
            jobs_running.jobs_combo.insert(END, file_to_copy) #sending it over to the listbox in the other screen.
            source_file = self.config.output_directory + "\\" + file_to_copy #creating a string to look for the file with in the output directory. 
            shutil.copy2(source_file, dest_directory[0]) #copying the files to the hot folder.

        messagebox.showinfo("Files Sent", "The files have been sent!") #showing a message to confirm it's done.
