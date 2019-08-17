import os
import curses
from curses import wrapper
from folder import Folder
from cursor import Cursor
from ui import UI
from scroll_position import ScrollPosition
from key_press_handler import KeyPressHandler
from query import Query


def main():
    wrapper(run)

    # Move terminal to python working directory
    os.system("/bin/bash")


def run(screen):
    init_curses(screen)

    query = Query()
    folder = Folder(query)

    cursor = Cursor(folder.num_sub_folders(), 2)
    file_scroll_position = ScrollPosition(0, folder.num_sub_files())

    keyPressHandler = KeyPressHandler(cursor, file_scroll_position, folder,
                                      query)

    ui = UI(screen, cursor, file_scroll_position, query)
    pad = ui.folder_pad

    while(True):
        ui.update_screen(folder)

        key = pad.getch()
        s = chr(key)

        if keyPressHandler.is_escape_key(key, pad):
            break

        keyPressHandler.handle_key_press(key)


def init_curses(screen):
    curses.curs_set(False)

main()
