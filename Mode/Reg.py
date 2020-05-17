#This class holds functions related to general cryptography
#
#@author Steven Guan

import numpy as np
from Mode.Mode import Mode
from Module.Reg import ExtendedEuclideanAlgo

class Reg(Mode):
    
    def __init__(self):
        self.__name = "REG"
        self.__commands = {
            "eea": self.EEA
        }

    def EEA(self, args):
        if args[0] == "-i":
            ExtendedEuclideanAlgo.EEA_int(int(args[1]), int(args[2]))
        elif args[1] == "-p":
            ExtendedEuclideanAlgo.EEA_poly(args[1], args[2])

    def getName(self):
        return self.__name