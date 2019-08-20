class FileWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def write_line(self, text):
        with open(self.file_path, 'w+') as file:
            file.write(text + "\n")
