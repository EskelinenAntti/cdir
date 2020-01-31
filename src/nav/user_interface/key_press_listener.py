import curses

class KeyPressListener():

    def __init__(self, screen, on_key_pressed: "lambda"):
        self.screen = screen
        self.on_key_pressed = on_key_pressed
        self.screen.keypad(True)

    def start(self):

        while(True):
            key = self.screen.getch()
            s = chr(key)

            if self.__is_escape_key(key):
                break

            self.on_key_pressed(key)

    def __is_escape_key(self, key):
        # From
        # https://stackoverflow.com/questions/5977395/ncurses-and-esc-alt-keys

        if key == curses.KEY_F1:
            return True

        if key == 27:
            self.screen.nodelay(True)
            n = self.screen.getch()
            if n == -1:
                # Escape was pressed
                return True
            self.screen.nodelay(False)
        return False