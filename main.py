from tkinter import * #importing tkinter
from tkinter.ttk import * #importing ttk
from data.loadinghelper import * #importing the loading helper class
from data.jobsrunning import * #import the jobs running class

#main definition
def main():
    root = Tk()  #initiliazing tcl/tk intepreter
    loading_helper = LoadingHelper(root) #creating new instance of class
    root.mainloop() #running loop

if __name__ == "__main__": #checking if we are running this file itself
    main() #if so, run main.