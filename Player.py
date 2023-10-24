class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100

    def move(self, direction):
        if direction == "left":
            self.x -= 10
        if direction == "right":
            self.x += 10
        if direction == "up":
            self.y -= 10
        if direction == "down":
            self.y += 10
