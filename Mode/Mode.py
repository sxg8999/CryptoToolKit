class Mode():

    def __init__(self):
        self.command = {}


    def analyze(self, funcName, args):
        func = self.command.get(funcName)
        