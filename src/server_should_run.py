class ServerShouldRun:
    def __init__(self, initial_value):
        self.should_run = initial_value
    def allow(self):
        self.should_run = True
    def prevent(self):
        self.should_run = False
    def ask(self):
        return self.should_run