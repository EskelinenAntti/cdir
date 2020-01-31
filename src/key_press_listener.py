from key_press_handler import KeyPressHandler

class KeyPressListener():

    def __init__(self, key_press_handler: KeyPressHandler, screen):
        self.key_press_handler = key_press_handler
        self.screen = screen

        self.screen.keypad(True)

    def start(self):

        while(True):
            key = self.screen.getch()
            s = chr(key)

            if self.__is_escape_key(key):
                break

            self.key_press_handler.handle_key_press(key)


    def __is_escape_key(self, key):
        # From
        # https://stackoverflow.com/questions/5977395/ncurses-and-esc-alt-keys

        if key == curses.KEY_F1:
            return True

        escape_was_pressed = False
        if key == 27:
            self.screen.nodelay(True)
            n = self.screen.getch()
            if n == -1:
                # Escape was pressed
                escape_was_pressed = True
            self.screen.nodelay(False)

        prg_should_exit = False
        if escape_was_pressed:
            if self.query.query_text:
                self.query.clear()
                self.__clear_cursor()
            else:
                prg_should_exit = True

        return prg_should_exit