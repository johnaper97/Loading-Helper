class Config():
    def __init__(self):
        self.product_codes = ["XXY", "XYX", "ABC", "HIJ", "HEY"]
        self.output_directory = "Example Directory\\output"
        self.queue_directories = ["Example Directory\\xxy_aps", "Example Directory\\xyx_aps", "Example Directory\\abc_aps", "Example Directory\\hij_aps", "Example Directory\\hey_aps",]

        self.queue_names = self.queue_name(self.queue_directories)
        print(self.queue_names)

    def queue_name(self, directory):
        names_list = []

        for i in range(len(directory)):
            sub = directory[i].split("\\")
            name = sub.pop(-1)
            print(name)
            names_list.append(name)

        return names_list
