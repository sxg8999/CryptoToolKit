class Mode():

    def __init__(self):
        self.__commands = {}


    def analyze(self, args):
        funcName = args[0]
        func = self.__commands.get(funcName)
        func(args[1:])
