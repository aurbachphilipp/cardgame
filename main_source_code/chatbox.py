class Chatbox:
    def __init__(self):
        self.lines = []
        self.maxlines = 10   # max number of lines stored
        self.update = [False, False, False, False]

    def new_line(self, id, msg):
        if len(self.lines) >= self.maxlines:
            self.lines.pop(0)
        self.lines.append(str(id) + ": " + msg)
        self.set_update()
        return "1"

    def last_line(self):
        return self.lines[-1]

    def set_update(self):
        self.update = [True, True, True, True]