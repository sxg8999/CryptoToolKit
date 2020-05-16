class Mode():

    def __init__(self):
        self.commands = {}


    def analyze(self, args):
        funcName = args[0]
        func = self.commands.get(funcName)
        func(args[1:])
