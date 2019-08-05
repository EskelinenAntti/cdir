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

    cursor = Cursor(folder.num_sub_folders())

    ui = UI(screen, cursor)
    pad = ui.folder_pad

    while(True):

        ui.update_screen(folder)

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


def print_folders(pad, screen, folder, cursor):

    screen_max_y_size = screen.getmaxyx()[0]
    files_max_x_size = round(screen.getmaxyx()[1] / 2)
    pad.resize(max(folder.num_sub_folders() + 1, screen_max_y_size),
               files_max_x_size)
    pad.clear()

    screen.clear()
    screen.addstr(0, 0, folder.current_path)

    screen.refresh()

    for i in range(0, len(folder.sub_folders)):
        # Print only letters that fit to screen
        printed_sub_folder_name = folder.sub_folders[i][:files_max_x_size]
        if (i == cursor.row_index):
            # Highlight cursor
            pad.addstr(i, 0, printed_sub_folder_name, curses.A_STANDOUT)
        else:
            pad.addstr(i, 0, printed_sub_folder_name)

    screen_max_y_coord = screen_max_y_size - 1
    screen_max_x_coord = files_max_x_size - 1
    pad.refresh(max(0, (cursor.row_index + 1)  - screen_max_y_coord) ,0,
                    2,0, screen_max_y_coord, screen_max_x_coord)


def print_files(pad, screen, folder, cursor):
    screen_max_y_size = screen.getmaxyx()[0]
    files_max_x_size = screen.getmaxyx()[1]
    pad.resize(max(folder.num_sub_folders() + 1, screen_max_y_size),
               files_max_x_size)
    pad.clear()

    screen.clear()
    screen.addstr(0, 0, folder.current_path)

    screen.refresh()

    for i in range(0, len(folder.sub_folders)):
        # Print only letters that fit to screen
        printed_sub_folder_name = folder.sub_folders[i][:files_max_x_size]
        if (i == cursor.row_index):
            # Highlight cursor
            pad.addstr(i, 0, printed_sub_folder_name, curses.A_STANDOUT)
        else:
            pad.addstr(i, 0, printed_sub_folder_name)

    screen_max_y_coord = screen_max_y_size - 1
    screen_max_x_coord = files_max_x_size - 1
    pad.refresh(max(0, (cursor.row_index + 1)  - screen_max_y_coord) ,0,
                    2,0, screen_max_y_coord, screen_max_x_coord)


def select_folder(folder, cursor):
    folder.move_to(folder.sub_folders[cursor.row_index])
    cursor.clear_cursor(folder.num_sub_folders())


def init_curses(screen):
    curses.curs_set(False)


main()
