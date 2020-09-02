# MASTER CLASS:
import copy
import os
import json

direc = "D:\\Usuarios\\Vicent Joan\\Documents\\REB\\Master_Class"

with open(os.path.join(direc, "extensions.json")) as f:
    extensions = json.load(f)


class Folder:
    def __init__(self, name, path=None):
        self.name = name
        self.path = path
        self.files = os.listdir(self.path)

    def create (self):
        pass

    def new_folders(self):
        for extension in extensions["python_project"]:
            if extension not in self.files:
                os.mkdir(direc + "\\" + extension)

    def re_locate(self):
        for file in self.files:
            file_list = file.rsplit('.', 1)
            print(file_list)
            for extension in extensions["python_project"]:
                if file_list[1].lower() == extension:
                    os.rename(direc + "\\" + file, direc + "\\" + extension + "\\" + file)


folder1 = Folder("Master_Class", direc)

print(folder1.files)

folder1.new_folders()

folder1.re_locate()



