#This is the main program
#
#@author Steven Guan

from Mode import AES, Reg

class ToolKit():
    def __init__(self):
        self.__M0DE_DICT = {
            "AES": AES,
            "REG": Reg
        }
        self.__END_SET = set(["q", "exit", "quit"])
    
    


def main():
    
    pass


if __name__ == "__main__":
    main()