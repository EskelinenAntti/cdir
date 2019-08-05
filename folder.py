import os


class Folder:

    def __init__(self):
        self.__initialize_in_cwd()

    def __get_current_path(self):
        return os.getcwd()

    def __get_sub_folders(self):
        sub_folders = (next(os.walk('.'))[1])
        return  [os.pardir] + self.__sort_hidden_last(sub_folders)

    def __sort_hidden_last(self, items):
        normal_items = sorted([item for item in items
                                 if item[0] != "."], key=lambda s: s.lower())

        hidden_items = sorted([item for item in items
                                 if item[0] == "."], key=lambda s: s.lower())

        return normal_items + hidden_items

    def num_sub_folders(self):
        return len(self.__get_sub_folders())

    def __get_sub_files(self):
        sub_files = [f for f in os.listdir('.') if os.path.isfile(f)]
        return self.__sort_hidden_last(sub_files)

    def __initialize_in_cwd(self):
        self.current_path = self.__get_current_path()
        self.sub_folders = self.__get_sub_folders()
        self.sub_files = self.__get_sub_files()

    def move_to(self, folder):
        os.chdir(folder)
        self.__initialize_in_cwd()
