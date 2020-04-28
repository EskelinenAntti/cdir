from nav_cli.data.file_writer import FileWriter
import os

CD_SCRIPT_FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/../../tmp/navigate_to"

class ScriptWriter():

    @staticmethod
    def write(current_path, output_file):
        bat_file_writer = FileWriter(output_file)
        bat_file_writer.write_line(current_path)
