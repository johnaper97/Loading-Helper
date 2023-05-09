#config class.
class Config():
    def __init__(self):
        self.product_codes = ["XXY", "XYX", "ABC", "HIJ", "HEY"] #product codes
        self.output_directory = "Example Directory\\output" #output directory
        self.queue_directories = ["Example Directory\\xxy_aps", "Example Directory\\xyx_aps", "Example Directory\\abc_aps", "Example Directory\\hij_aps", "Example Directory\\hey_aps",] #hot folder directories

        self.queue_names = self.queue_name(self.queue_directories) #setting queue names to the output of the function (a list)

    #queue name function
    def queue_name(self, directory):
        names_list = [] #creating an empty list to add to.

        for i in range(len(directory)):
            sub = directory[i].split("\\") #this loop splits the directories up by the \
            name = sub.pop(-1) #since directories always run in a particular way, we just need the last value. pop it off. 
            names_list.append(name) #add that value to the names_list list.

        return names_list #after it's done, return that list.
