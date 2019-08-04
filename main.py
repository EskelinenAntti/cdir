import os
import curses
from curses import wrapper
from folder import Folder
from cursor import Cursor


def main():
    wrapper(run)

    # Move terminal to python working directory
    os.system("/bin/bash")


def run(screen):
    init_curses(screen)

    folder = Folder()

    cursor = Cursor(folder.num_sub_folders())

    while(True):
        print_folder(screen, folder, cursor)

        key = screen.getch()
        if key == curses.KEY_UP:
            cursor.move_up()
        elif key == curses.KEY_DOWN:
            cursor.move_down()
        elif key == curses.KEY_ENTER or key == 10 or key == 13:
            select_folder(folder, cursor)
        elif key == ord('q'):
            break


def print_folder(screen, folder, cursor):
    screen.clear()
    screen.addstr(0, 0, folder.current_path)
    for i in range(0, len(folder.sub_folders)):
        if (i == cursor.row_index):
            # Highlight cursor
            screen.addstr(i+1, 0, folder.sub_folders[i], curses.A_STANDOUT)
        else:
            screen.addstr(i+1, 0, folder.sub_folders[i])

    screen.refresh()


def select_folder(folder, cursor):
    folder.move_to(folder.sub_folders[cursor.row_index])
    cursor.clear_cursor(folder.num_sub_folders())


def init_curses(screen):
    curses.curs_set(False)


main()
