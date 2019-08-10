class ScrollPosition():

    def __init__(self, visible_height, total_height):
        self.clear(visible_height, total_height)

    def move_down(self):
        self.last_visible_index = min(self.last_visible_index + 1,
                                      self.__get_last_index())

    def move_up(self):
        self.last_visible_index = max(self.last_visible_index - 1,
                                      0)

    def update_visible_height(self, new_visible_height):
        if not self.__visible_items_fill_screen(new_visible_height,
                                                self.last_visible_index):
            self.last_visible_index = new_visible_height - 1

        self.visible_height = new_visible_height

    def clear(self, new_total_height, new_visible_height):
        self.last_visible_index = 0
        self.total_height = new_total_height
        self.visible_height = new_visible_height

    def content_changed(self, new_total_height):
        self.last_visible_index = 0
        self.total_height = new_total_height

    def get_first_visible_index(self):
        return max(0, self.last_visible_index + 1 - self.visible_height)

    def __get_last_index(self):
        return self.total_height - 1

    def __visible_items_fill_screen(self, visible_height, last_visible_index):
        if visible_height < self.total_height:
            return last_visible_index + 1 >= visible_height