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


class restart_game_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 90
        self.height = 34

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class quit_game_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 102
        self.height = 34

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class X_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15

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


class playlist_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class info_button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class checkbox1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class checkbox2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False


class Credits:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 25

    def isOver(self, mouse):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return True
        return False
