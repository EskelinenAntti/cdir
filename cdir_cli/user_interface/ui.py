import curses
from cdir_cli.user_interface.query import Query
from cdir_cli.user_interface.cursor import Cursor
from cdir_cli.user_interface.scroll_position import ScrollPosition
from cdir_cli.user_interface.main_view import MainView
from cdir_cli.user_interface.key_press_handler import KeyPressHandler
from cdir_cli.user_interface.key_press_listener import KeyPressListener

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

        self.key_press_listener = KeyPressListener(
            screen,
            self.__on_key_pressed)

        # screen object is intentionally not saved as class attribute here as we
        # should not access it directly here on higher level.

    def show(self):
        self.__update_screen()
        self.key_press_listener.start()


    def __on_key_pressed(self, key):
        self.key_press_handler.handle_key_press(key)
        self.__update_screen()

    def __update_screen(self):
        self.main_view.print_screen(self.folder_navigator,
            self.query,
            self.cursor,
            self.file_scroll_position)

