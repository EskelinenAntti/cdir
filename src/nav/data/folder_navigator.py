import os


class FolderNavigator:
    """ Core class used to navigate in file system and to read folder contents.

    Attributes:
        current_path: Path where the navigator is located currently
        sub_folders: List of folders in current_path
        sub_files: List of files in current_path
    """

    def __init__(self):
        self.__initialize_in_cwd()

    def __get_current_path(self):
        return os.getcwd()

    def __get_all_sub_folders(self, dir):
        sub_folders = []

        for sub_dir in os.listdir(dir):
            if os.path.isdir(os.path.join(dir, sub_dir)):
                """try:
                    os.listdir(sub_dir)
                except PermissionError:
                    continue
                """
                # The commented code could be used to remove dirs that contents
                # we do not have rights.
                sub_folders.append(sub_dir)

        return [os.pardir] + self.__sort_hidden_last(sub_folders)

    @property
    def sub_folders(self):
            return self.__all_sub_folders

    def __sort_hidden_last(self, items):
        normal_items = sorted([item for item in items
                                 if item[0] != "."], key=lambda s: s.lower( ))

        hidden_items = sorted([item for item in items
                                 if item[0] == "."], key=lambda s: s.lower())

        return normal_items + hidden_items

    def __get_sub_files(self):
        sub_files = [f for f in os.listdir('.') if os.path.isfile(f)]
        return self.__sort_hidden_last(sub_files)

    def __initialize_in_cwd(self):
        self.current_path = self.__get_current_path()
        self.__all_sub_folders = self.__get_all_sub_folders(self.current_path)
        self.sub_files = self.__get_sub_files()
        self.sub_folders

    def move_to(self, folder):
        os.chdir(folder)
        self.__initialize_in_cwd()
