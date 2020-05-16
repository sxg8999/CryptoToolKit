#This is the main program
#
#@author Steven Guan

from Mode import AES, Reg

class ToolKit():

    def __init__(self):
        mode_AES = AES.AES()
        mode_Reg = Reg.Reg()
        
        self.__mode = mode_Reg
        self.__M0DE_DICT = {
            "AES": mode_AES,
            "REG": mode_Reg
        }
        self.__END_SET = set(["q", "exit", "quit"])
    
    def run(self):
        """
        Until user specifically enter the quit command, the program will keep running
        """
        
        while(True):
            user_input = input("(" + self.__mode.getName() + ")" + " Enter:\t")
            args = user_input.split(" ")

            if(args[0].lower() in self.__END_SET):
                
                #if the current mode is REG then quit the program
                if(self.__mode.getName() == "REG"):
                    print("Exited")
                    break
                else:
                    mode_name = "REG"
                    self.__mode = self.__M0DE_DICT.get(mode_name)
            elif(args[0].lower() == "mode"):
                
                mode_name = args[1].upper()
                self.__mode = self.__M0DE_DICT.get(mode_name)
            else:
                self.__mode.analyze(args)
        
    
    


def main():
    tk = ToolKit()
    tk.run()
    


if __name__ == "__main__":
    main()