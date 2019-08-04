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

    pad = curses.newpad(folder.num_sub_folders() + 1, screen.getmaxyx()[1])
    pad.keypad(1)

    while(True):

        print_folder(pad, screen, folder, cursor)

        key = pad.getch()
        if key == curses.KEY_UP:
            cursor.move_up()
        elif key == curses.KEY_DOWN:
            cursor.move_down()
        elif key == curses.KEY_ENTER or key == 10 or key == 13:
            select_folder(folder, cursor)
        elif key == curses.KEY_RESIZE:
            pass
        elif key == ord('q'):
            break


def print_folder(pad, screen, folder, cursor):

    screen_max_y_size = screen.getmaxyx()[0]
    screen_max_x_size = screen.getmaxyx()[1]
    pad.resize(max(folder.num_sub_folders() + 1, screen_max_y_size),
               screen_max_x_size)
    pad.clear()
    pad.addstr(0, 0, folder.current_path)
    for i in range(0, len(folder.sub_folders)):
        # Print only letters that fit to screen
        printed_sub_folder_name = folder.sub_folders[i][:screen_max_x_size]
        if (i == cursor.row_index):
            # Highlight cursor
            pad.addstr(i+1, 0, printed_sub_folder_name, curses.A_STANDOUT)
        else:
            pad.addstr(i+1, 0, printed_sub_folder_name)

    screen_max_y_coord = screen_max_y_size - 1
    screen_max_x_coord = screen_max_x_size - 1

    pad.refresh(max(0, (cursor.row_index + 1)  - screen_max_y_coord) ,0,
                    0,0, screen_max_y_coord, screen_max_x_coord)


def select_folder(folder, cursor):
    folder.move_to(folder.sub_folders[cursor.row_index])
    cursor.clear_cursor(folder.num_sub_folders())


def init_curses(screen):
    curses.curs_set(False)


main()
