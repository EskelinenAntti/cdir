import curses


class UI:

    def __init__(self, screen, cursor, file_scroll_position):
        self.screen = screen
        self.folder_pad = curses.newpad(1,1)
        self.folder_pad.keypad(1)
        self.file_pad = curses.newpad(1,1)
        self.cursor = cursor
        self.file_scroll_position = file_scroll_position

    def update_screen(self, folder):

        if (self.screen.getmaxyx()[0] > 2):
            self.__draw_header_row(folder.current_path)
            self.__draw_folders(folder.sub_folders)
            self.__draw_files(folder.sub_files)

    def __draw_header_row(self, current_folder):

        self.screen.clear()
        self.screen.addstr(0, 0,
                        current_folder[:self.__get_folder_column_width()-1])

        if self.cursor.column_index == 1:
            self.screen.addstr(0, self.__get_folder_column_width(),
                               "Files:"[:self.__get_file_column_width()], curses.A_UNDERLINE)
        else:
            self.screen.addstr(0, self.__get_folder_column_width(),
                               "Files:"[:self.__get_file_column_width()])

        self.screen.refresh()

    def __draw_folders(self, folders):
        pad_max_y_size = self.screen.getmaxyx()[0] - 2
        self.file_pad.resize(max(len(folders), pad_max_y_size),
                               self.__get_folder_column_width())
        self.file_pad.clear()

        for i in range(0, len(folders)):
            # Print only letters that fit to screen
            printed_sub_folder_name = \
                folders[i][:self.__get_folder_column_width()]

            if (i == self.cursor.row_index and self.cursor.column_index == 0):
                # Highlight cursor
                self.file_pad.addstr(i, 0, printed_sub_folder_name, curses.A_STANDOUT)
            else:
                self.file_pad.addstr(i, 0, printed_sub_folder_name)

        screen_max_y_coord = self.screen.getmaxyx()[0] -1
        folder_pad_max_x_coord = self.__get_folder_column_width() - 1
        self.file_pad.refresh(max(0, (self.cursor.row_index + 2)  - screen_max_y_coord) ,0,
                        2,0, screen_max_y_coord, folder_pad_max_x_coord -1)

    def __draw_files(self, files):
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

        self.file_scroll_position.update_visible_height(self.__get_file_column_heigth())

        self.file_pad.refresh(self.file_scroll_position.get_first_visible_index(), 0,
                              2, self.__get_folder_column_width(),
                              screen_max_y_coord, file_pad_max_x_coord)

    def __get_folder_column_width(self):
        return round(self.screen.getmaxyx()[1]/2)

    def __get_file_column_width(self):
        return self.screen.getmaxyx()[1] - self.__get_folder_column_width()

    def __get_file_column_heigth(self):
        return self.screen.getmaxyx()[0] - 2
