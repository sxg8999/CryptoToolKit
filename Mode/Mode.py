class Mode():

    def __init__(self):
        self.command = {}


    def analyze(self, args):
        funcName = args[0]
        func = self.command.get(funcName)
        func(args[1:])
