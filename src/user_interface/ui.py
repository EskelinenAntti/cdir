import curses
from cursor import Cursor
from query import Query
from scroll_position import ScrollPosition
from main_view import MainView
from key_press_handler import KeyPressHandler
from key_press_listener import KeyPressListener

class UI:
    """ Represents the higher level user interface. Wraps together components
        that draw UI and controller components that handle user interactions.
        """

    def __init__(self, screen, folder_navigator):
        self.folder_navigator = folder_navigator
        self.query = Query()
        self.cursor = Cursor(len(self.query.filter_folders(folder_navigator.sub_folders)), 2)
        self.file_scroll_position = ScrollPosition(0, len(folder_navigator.sub_files))
        self.main_view = MainView(screen)
        self.key_press_handler = KeyPressHandler(self.cursor,
                                    self.file_scroll_position,
                                    self.folder_navigator,
                                    self.query)
        self.key_press_listener = KeyPressListener(self.key_press_handler, screen)

        # screen obeject is intentionally not saved as class attribute as we
        # should not access it directly on higher level.

    def show(self):



    def __update_screen(self):
        self.main_view.print_screen(self.folder_navigator,
            self.query,
            self.cursor,
            self.file_scroll_position)

