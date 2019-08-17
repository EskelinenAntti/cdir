class Query:

    def __init__(self):
        self.clear()

    def addChar(self, char):
        self.query_text += char

    def removeChar(self):
        if len(self.query_text) > 0:
            self.query_text = self.query_text[:-1]

    def clear(self):
        self.query_text = ""

    def filter_folders(self, folders):
        if not self.query_text:
            return folders

        filtered_folders = []
        for folder in folders:
            if self.query_text in folder:
                filtered_folders.append(folder)

        return filtered_folders
