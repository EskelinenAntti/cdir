import os
import curses
from curses import wrapper
from folder import Folder
from cursor import Cursor
from ui import UI


def main():
    wrapper(run)

    # Move terminal to python working directory
    os.system("/bin/bash")


def run(screen):
    init_curses(screen)

    folder = Folder()

    cursor = Cursor(folder.num_sub_folders(), 2)

    file_scroller = Cursor(calculate_rows_for_files(folder, screen), 1)

    ui = UI(screen, cursor, file_scroller)
    pad = ui.folder_pad

    while(True):
        ui.update_screen(folder)
        file_scroller.rows = calculate_rows_for_files(folder, screen)

        key = pad.getch()

        if key == ord('q'):
            break

        if cursor.column_index == 0:
            move_cursor(key, cursor, folder)
        elif cursor.column_index == 1:
            move_file_scroller(key, cursor, file_scroller)


def move_cursor(key, cursor, folder):
    if key == curses.KEY_UP:
        cursor.move_up()
    elif key == curses.KEY_DOWN:
        cursor.move_down()
    elif key == curses.KEY_LEFT:
        cursor.move_left()
    elif key == curses.KEY_RIGHT:
        cursor.move_right()
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        select_folder(folder, cursor)

def move_file_scroller(key, cursor, file_scroller):
    if key == curses.KEY_UP:
        file_scroller.move_up()
    elif key == curses.KEY_DOWN:
        file_scroller.move_down()
    elif key == curses.KEY_LEFT:
        cursor.move_left()
    elif key == curses.KEY_RIGHT:
        cursor.move_right()

def select_folder(folder, cursor):
    if (is_cursor_on_folder_list(cursor)):
        folder.move_to(folder.sub_folders[cursor.row_index])
        cursor.clear_cursor(folder.num_sub_folders(), 2)

def is_cursor_on_folder_list(cursor):
    return cursor.column_index == 0

def calculate_rows_for_files(folder, screen):
    # Always (number of rows) >= 1
    rows = max(folder.num_sub_files() - screen.getmaxyx()[0] + 3, 1)
    return rows

def init_curses(screen):
    curses.curs_set(False)


main()
