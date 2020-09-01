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
        for extention in extensions["python_project"]:
            if extention not in self.files:
                os.mkdir(direc + "\\" + extention)


folder1 = Folder("Master_Class", direc)

print(folder1.files)

folder1.new_folders()



