import curses
from cdir_cli.user_interface.cursor import Cursor
from cdir_cli.user_interface.query import Query
from cdir_cli.user_interface.scroll_position import ScrollPosition
from cdir_cli.data.folder_navigator import FolderNavigator


class MainView:
    """ Lower level class for printing data to shell. Does not modify or update
        any data.
        """

    def __init__(self, screen):
        self.screen = screen
        self.folder_pad = curses.newpad(1,1)
        ## self.folder_pad.keypad(1)
        self.file_pad = curses.newpad(1,1)

    def print_screen(self, folder_navigator: FolderNavigator, query: Query, cursor: Cursor, scroll_position: ScrollPosition):

        if (self.screen.getmaxyx()[0] > 2):
            self.__draw_header_row(folder_navigator.current_path, query, cursor)
            self.__draw_folders(query.filter_folders(folder_navigator.sub_folders), cursor)
            self.__draw_files(folder_navigator.sub_files, scroll_position)

    def __draw_header_row(self, folder_navigator, query, cursor):

        self.screen.clear()

        if query.query_text:
            folder_view_header = "Search: " + query.query_text
        else:
            folder_view_header = folder_navigator

        self.screen.addstr(0, 0,
                           folder_view_header[:self.__get_folder_column_width()-1])

        if cursor.column_index == 1:
            self.screen.addstr(0, self.__get_folder_column_width(),
                               "Files:"[:self.__get_file_column_width()], curses.A_UNDERLINE)
        else:
            self.screen.addstr(0, self.__get_folder_column_width(),
                               "Files:"[:self.__get_file_column_width()])

        self.screen.refresh()

    def __draw_folders(self, folders, cursor):

        pad_max_y_size = self.screen.getmaxyx()[0] - 2
        self.file_pad.resize(max(len(folders), pad_max_y_size),
                               self.__get_folder_column_width())
        self.file_pad.clear()

        for i in range(0, len(folders)):
            # Print only letters that fit to screen
            printed_sub_folder_name = \
                folders[i][:self.__get_folder_column_width()]

            if (i == cursor.row_index and cursor.column_index == 0):
                # Highlight cursor
                self.file_pad.addstr(i, 0, printed_sub_folder_name, curses.A_STANDOUT)
            else:
                self.file_pad.addstr(i, 0, printed_sub_folder_name)

        screen_max_y_coord = self.screen.getmaxyx()[0] - 1
        folder_pad_max_x_coord = self.__get_folder_column_width() - 1
        self.file_pad.refresh(max(0, (cursor.row_index + 2)  - screen_max_y_coord) ,0,
                        2,0, screen_max_y_coord, folder_pad_max_x_coord -1)

    def __draw_files(self, files, file_scroll_position):
        screen_max_y_size = self.screen.getmaxyx()[0]
        self.file_pad.resize(max(len(files), screen_max_y_size),
                             self.__get_file_column_width())
        self.file_pad.clear()

        for i in range(0, len(files)):
            # Print only letters that fit to screen
            printed_file_name = \
                files[i][:self.__get_file_column_width()]

            self.file_pad.addstr(i, 0, printed_file_name)

        screen_max_y_coord = screen_max_y_size - 1
        file_pad_max_x_coord = self.screen.getmaxyx()[1] - 1

        file_scroll_position.update_visible_height(self.__get_file_column_heigth())

        self.file_pad.refresh(file_scroll_position.get_first_visible_index(), 0,
                              2, self.__get_folder_column_width(),
                              screen_max_y_coord, file_pad_max_x_coord)

    def __get_folder_column_width(self):
        return round(self.screen.getmaxyx()[1]/2)

    def __get_file_column_width(self):
        return self.screen.getmaxyx()[1] - self.__get_folder_column_width()

    def __get_file_column_heigth(self):
        return self.screen.getmaxyx()[0] - 2
