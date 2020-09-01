# MASTER CLASS:
import copy
import os


class Folder:
    def __init__(self, name, path="D:\\Usuarios\\Vicent Joan\\Documents\\REB\\Master_Class"):
        self.name = name
        self.path = path
        self.files = os.listdir(self.path)

    def create (self):
        pass


fd1 = Folder("Master_Class")

print(fd1.files)



