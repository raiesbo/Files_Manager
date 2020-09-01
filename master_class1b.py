# MASTER CLASS:
import copy
import os


class Folder:
    def __init__(self, name, path="D:\\Usuarios\\Vicent Joan\\Documents\\REB\\Master_Class"):
        self.name = name
        self.path = path
        self.files = []

    def create (self):
        pass

    def add_files(self):
        files = os.listdir(self.path)
        self.files.append(files)
    

fd1 = Folder("Master_Class")

fd1.add_files()

print(fd1.files)



