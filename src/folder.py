import os
from query import Query


class Folder:

    def __init__(self, query):
        self.query = query
        self.__initialize_in_cwd()


    def __get_current_path(self):
        return os.getcwd()

    def __get_all_sub_folders(self):
        sub_folders = (next(os.walk('.'))[1])
        return [os.pardir] + self.__sort_hidden_last(sub_folders)

    @property
    def sub_folders(self):
            return self.query.filter_folders(self.__all_sub_folders)

    def __sort_hidden_last(self, items):
        normal_items = sorted([item for item in items
                                 if item[0] != "."], key=lambda s: s.lower( ))

        hidden_items = sorted([item for item in items
                                 if item[0] == "."], key=lambda s: s.lower())

        return normal_items + hidden_items

    def num_sub_folders(self):
        return len(self.sub_folders)

    def num_sub_files(self):
        return len(self.__get_sub_files())

    def __get_sub_files(self):
        sub_files = [f for f in os.listdir('.') if os.path.isfile(f)]
        return self.__sort_hidden_last(sub_files)

    def __initialize_in_cwd(self):
        self.current_path = self.__get_current_path()
        self.__all_sub_folders = self.__get_all_sub_folders()
        self.sub_files = self.__get_sub_files()
        self.sub_folders

    def move_to(self, folder):
        os.chdir(folder)
        self.__initialize_in_cwd()
