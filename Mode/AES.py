#This class holds functions related to AES Encryption and Decryption
#
#@author Steven Guan

import numpy as np
from Module.AES import S_Box
from Mode.Mode import Mode


class AES(Mode):

    def __init__(self):
        self.__name = "AES"
        self.__commands = {
            "sbox" : self.s_box,
        }
        
        

    def s_box(self, args):
        
        _len = args.__len__()
        if _len == 1:
            S_Box.s_box_affine_mapping(args[0])
        elif _len == 2:
            if args[0] == "-i":
                S_Box.s_box_affine_mapping(args[1], config = "DECRYPTION")
            else:
                print("Wrong Command")
        
    
    def getName(self):
        return self.__name
    


