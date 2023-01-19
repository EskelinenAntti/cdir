import curses
from cdir_cli.user_interface.cursor import Cursor
from cdir_cli.user_interface.query import Query
from cdir_cli.user_interface.scroll_position import ScrollPosition
from cdir_cli.data.folder_navigator import FolderNavigator
import os

class MainView:
    """ Lower level class for printing data to shell. Does not modify or update
        any data.
        """

    # Color pair enumerations
    CUR_DIR_COLOR = 1
    FILE_HEADER_COLOR = 2
    SEARCH_HEADER_COLOR = 3
    DIRECTORY_COLOR = 4
    FILE_COLOR = 0 # Note: color pair 0 is white on black by default

    N_HEADER_ROWS = 3

    def __init__(self, screen):
        self.screen = screen
        self.folder_pad = curses.newpad(1,1)
        ## self.folder_pad.keypad(1)
        self.file_pad = curses.newpad(1,1)
        # Windows requires calling color first before any prints for commandline colors to work.
        if (os.name == 'nt'):
            os.system('color')
        curses.init_pair(self.CUR_DIR_COLOR, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(self.FILE_HEADER_COLOR, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(self.SEARCH_HEADER_COLOR, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(self.DIRECTORY_COLOR, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    def print_screen(self, folder_navigator: FolderNavigator, query: Query, cursor: Cursor, scroll_position: ScrollPosition):

        if (self.screen.getmaxyx()[0] > self.N_HEADER_ROWS + 1):
            self.__draw_header_rows(folder_navigator.current_path, query, cursor)
            self.__draw_folders(query.filter_folders(folder_navigator.sub_folders), cursor)
            self.__draw_files(folder_navigator.sub_files, scroll_position)

    def __draw_header_rows(self, folder_navigator, query, cursor):

        self.screen.clear()

        if query.query_text:
            search_header = "Search: "
            self.screen.addstr(0, 0,
                               search_header[:self.__get_folder_column_width()-1],
                               curses.color_pair(self.SEARCH_HEADER_COLOR))
            search_header_width = len(search_header[:self.__get_folder_column_width()-1])
            self.screen.addstr(0, search_header_width,
                               query.query_text[:self.__get_folder_column_width()-1-search_header_width])
        else:
            self.screen.addstr(0, 0,
                               "Current Path: " + folder_navigator[:self.__get_folder_column_width()-1],
                               curses.color_pair(self.CUR_DIR_COLOR))

        if cursor.column_index == 0:
            self.screen.addstr(1, 0,
                               "Directories:"[:self.__get_file_column_width()],
                               curses.A_UNDERLINE + curses.color_pair(self.FILE_HEADER_COLOR))
        else:
            self.screen.addstr(1, 0,
                               "Directories:"[:self.__get_file_column_width()],
                               curses.color_pair(self.FILE_HEADER_COLOR))

        if cursor.column_index == 1:
            self.screen.addstr(1, self.__get_folder_column_width(),
                               "Files:"[:self.__get_file_column_width()],
                               curses.A_UNDERLINE + curses.color_pair(self.FILE_HEADER_COLOR))
        else:
            self.screen.addstr(1, self.__get_folder_column_width(),
                               "Files:"[:self.__get_file_column_width()],
                               curses.color_pair(self.FILE_HEADER_COLOR))

        self.screen.refresh()

    def __draw_folders(self, folders, cursor):

        pad_max_y_size = self.screen.getmaxyx()[0] - self.N_HEADER_ROWS
        self.file_pad.resize(max(len(folders), pad_max_y_size),
                               self.__get_folder_column_width())
        self.file_pad.clear()

        for i in range(0, len(folders)):
            # Print only letters that fit to screen
            printed_sub_folder_name = \
                folders[i][:self.__get_folder_column_width()]

            if (i == cursor.row_index and cursor.column_index == 0):
                # Highlight cursor
                self.file_pad.addstr(i, 0, printed_sub_folder_name,
                                     curses.A_STANDOUT + curses.color_pair(self.DIRECTORY_COLOR))
            else:
                self.file_pad.addstr(i, 0, printed_sub_folder_name, curses.color_pair(self.DIRECTORY_COLOR))

        screen_max_y_coord = self.screen.getmaxyx()[0] - 1
        folder_pad_max_x_coord = self.__get_folder_column_width() - 1
        self.file_pad.refresh(max(0, (cursor.row_index + self.N_HEADER_ROWS)  - screen_max_y_coord) ,0,
                        self.N_HEADER_ROWS,0, screen_max_y_coord, folder_pad_max_x_coord -1)

    def __draw_files(self, files, file_scroll_position):
        screen_max_y_size = self.screen.getmaxyx()[0]
        self.file_pad.resize(max(len(files), screen_max_y_size),
                             self.__get_file_column_width())
        self.file_pad.clear()

        for i in range(0, len(files)):
            # Print only letters that fit to screen
            printed_file_name = \
                files[i][:self.__get_file_column_width()]

            self.file_pad.addstr(i, 0, printed_file_name, curses.color_pair(self.FILE_COLOR))

        screen_max_y_coord = screen_max_y_size - 1
        file_pad_max_x_coord = self.screen.getmaxyx()[1] - 1

        file_scroll_position.update_visible_height(self.__get_file_column_heigth())

        self.file_pad.refresh(file_scroll_position.get_first_visible_index(), 0,
                              self.N_HEADER_ROWS, self.__get_folder_column_width(),
                              screen_max_y_coord, file_pad_max_x_coord)

    def __get_folder_column_width(self):
        return round(self.screen.getmaxyx()[1]/2)

    def __get_file_column_width(self):
        return self.screen.getmaxyx()[1] - self.__get_folder_column_width()

    def __get_file_column_heigth(self):
        return self.screen.getmaxyx()[0] - self.N_HEADER_ROWS
