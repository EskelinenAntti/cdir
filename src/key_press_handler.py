import curses

FOLDER_COLUMN = 0
FILES_COLUMN = 1


class KeyPressHandler():

    def __init__(self, cursor, file_scroll_position, folder, query, main_view):
        self.cursor = cursor
        self.file_scroll_position = file_scroll_position
        self.folder = folder
        self.query = query

    def handle_key_press(self, key):
        if self.cursor.column_index == FOLDER_COLUMN:
            self.move_cursor(key)
        elif self.cursor.column_index == FILES_COLUMN:
            self.move_scroll_position(key)

    def handle_escape_press(self):


    def move_cursor(self, key):

        # TODO: add home and end key handling
        if key == curses.KEY_UP:
            self.cursor.move_up()
        elif key == curses.KEY_DOWN:
            self.cursor.move_down()
        elif key == curses.KEY_LEFT:
            self.cursor.move_left()
        elif key == curses.KEY_RIGHT:
            self.cursor.move_right()
        elif key == curses.KEY_ENTER or key == 10 or key == 13:
            self.__select_folder()
        # support backspace on windows also
        elif key == curses.KEY_BACKSPACE or key == 8:
            self.query.removeChar()
            self.__clear_cursor()
        else:
            self.query.addChar(chr(key))
            self.__clear_cursor()


    # Use inheritation to avoid more if-elif structures
    def move_scroll_position(self, key):
        if key == curses.KEY_UP:
            self.file_scroll_position.move_up()
        elif key == curses.KEY_DOWN:
            self.file_scroll_position.move_down()
        elif key == curses.KEY_LEFT:
            self.cursor.move_left()
        elif key == curses.KEY_RIGHT:
            self.cursor.move_right()
        else:
            # some other key pressed: handle input
            pass

    def __select_folder(self):
        selected_folder = self.folder.sub_folders[self.cursor.row_index]
        self.query.clear()

        self.folder.move_to(selected_folder)
        self.__clear_cursor()

        self.file_scroll_position.content_changed(self.folder.num_sub_files())

    def __clear_cursor(self):
        self.cursor.clear_cursor(self.folder.num_sub_folders(), 2)
