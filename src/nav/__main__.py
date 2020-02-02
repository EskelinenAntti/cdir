import curses
from curses import wrapper
from nav.data.folder_navigator import FolderNavigator
from nav.user_interface.ui import UI
from nav.data.script_writer import ScriptWriter
import sys


def main():
    wrapper(run)
    # Exit success
    sys.exit()

def run(screen):

    init_curses(screen)

    folder_navigator = FolderNavigator()

    # If script was started with path argument
    if len(sys.argv) > 1:
        current_dir = sys.argv[1]
        folder_navigator.move_to(current_dir)

    ui = UI(screen, folder_navigator)
    ui.show()

    # User has selected a folder
    ScriptWriter.write(folder_navigator.current_path)

def init_curses(screen):
    curses.curs_set(False)

if __name__ == "__main__":
    main()