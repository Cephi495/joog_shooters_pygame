class exit_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 79
        self.height = 35

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class music_play_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 35

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class music_pause_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 35

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class music_skip_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 35

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class music_previous_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 35

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False
