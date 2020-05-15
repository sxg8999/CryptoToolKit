#This class holds functions related to AES Encryption and Decryption
#
#@author Steven Guan

import numpy as np
import Module.AES.S_Box
from Module.AES import S_Box
class AES():

    def __init__(self):
        

    def s_box_affine_mapping(self, inverseVal):
        # """
        # Precondition: inverseVal is a string representation of the Inverse of the 
        #             initial starting hex value. inverseVal is
                    
        # """

        # _hexVal = int(inverseVal,16)  #converts inverseVal to hex
        # _binVal = bin(_hexVal)        #converst the hexVal to binary
        # _bin_str = str(_binVal)[2:]
        # _bin_str = _bin_str[::-1]     #reverse the string


        # # b = matrix_a * b'+ bit_vector mod 2
        # matrix_a = [
        #     [1,0,0,0,1,1,1,1],
        #     [1,1,0,0,0,1,1,1],
        #     [1,1,1,0,0,0,1,1],
        #     [1,1,1,1,0,0,0,1],
        #     [1,1,1,1,1,0,0,0],
        #     [0,1,1,1,1,1,0,0],
        #     [0,0,1,1,1,1,1,0],
        #     [0,0,0,1,1,1,1,1]
        # ]

        # bit_vector = [1,1,0,0,0,1,1,0]
        pass






    def getCommands():
        pass


