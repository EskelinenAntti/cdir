import os


class Folder:

    def __init__(self):
        self.current_path = self.__get_current_path()
        self.sub_folders = self.__get_sub_folders()

    def __get_current_path(self):
        return os.getcwd()

    def __get_sub_folders(self):
        return next(os.walk('.'))[1] + [os.pardir]

    def num_sub_folders(self):
        return len(self.__get_sub_folders())

    def move_to(self, folder):
        os.chdir(folder)
        self.current_path = self.__get_current_path()
        self.sub_folders = self.__get_sub_folders()
