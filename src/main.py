import os
import curses
from curses import wrapper
from folder import Folder
from cursor import Cursor
from ui import UI
from scroll_position import ScrollPosition
from key_press_handler import KeyPressHandler
from query import Query
from file_writer import FileWriter
import sys


CD_SCRIPT_FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/tmp/navigate_to"

def main():
    wrapper(run)
    # Exit success
    sys.exit()

def run(screen):

    init_curses(screen)

    query = Query()
    folder = Folder(query)

    if len(sys.argv) > 1:
        current_dir = sys.argv[1]
        folder.move_to(current_dir)

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

    # If running on windows
    if os.name == "nt":
        file_writer = FileWriter(CD_SCRIPT_FILE_PATH + ".bat")
        file_writer.write_line("cd /d \"" + folder.current_path+"\"")
    else:
        file_writer = FileWriter(CD_SCRIPT_FILE_PATH + ".sh")
        file_writer.write_line("cd " + folder.current_path)



def init_curses(screen):
    curses.curs_set(False)

main()
