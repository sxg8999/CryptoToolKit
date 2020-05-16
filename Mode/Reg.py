#This class holds functions related to general cryptography
#
#@author Steven Guan

import numpy as np 

class Reg():
    
    def __init__(self):
        self.__name = "REG"
        self.__command = {

        }

    def getCommands(self):
        return self.__command

    def getName(self):
        return self.__name