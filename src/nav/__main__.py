import curses
from curses import wrapper
from nav.data.folder_navigator import FolderNavigator
from nav.user_interface.ui import UI
from nav.data.file_writer import FileWriter
import sys


def main():
    wrapper(run)
    # Exit success
    sys.exit()

def run(screen):

    if len(sys.argv) < 2:
        sys.exit("No output file provided")
    output_file = sys.argv[1]

    init_curses(screen)
    folder_navigator = FolderNavigator()

    # If script was started with path argument
    if len(sys.argv) >= 3:
        current_dir = sys.argv[2]
        folder_navigator.move_to(current_dir)

    ui = UI(screen, folder_navigator)
    ui.show()

    # User has selected a folder
    FileWriter(output_file).write_line(folder_navigator.current_path)

def init_curses(screen):
    curses.curs_set(False)

if __name__ == "__main__":
    main()