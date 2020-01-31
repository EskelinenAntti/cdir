from nav.data.file_writer import FileWriter
import os

CD_SCRIPT_FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/../../tmp/navigate_to"

class ScriptWriter():

    @staticmethod
    def write(current_path):
        output_script = "cd \"" + current_path + "\""
        # If running on windows
        if os.name == "nt":
            bat_file_writer = FileWriter(CD_SCRIPT_FILE_PATH + ".bat")
            bat_file_writer.write_line(output_script)

            ps_file_writer = FileWriter(CD_SCRIPT_FILE_PATH + ".ps1")
            ps_file_writer.write_line(output_script)

        else:
            file_writer = FileWriter(CD_SCRIPT_FILE_PATH + ".sh")
            file_writer.write_line(output_script)