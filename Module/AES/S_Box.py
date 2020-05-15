import numpy as np

def s_box_affine_mapping(inverseVal):
        """
        Precondition: inverseVal is a string representation of the Inverse of the 
                    initial starting hex value. inverseVal is
                    
        """

        _hexVal = int(inverseVal,16)  #converts inverseVal to hex
        _binVal = bin(_hexVal)        #converst the hexVal to binary
        _bin_str = str(_binVal)[2:]
        # print(_bin_str)
        _bin_str = _bin_str[::-1]     #reverse the string

        b_initial = np.array(list(_bin_str.strip()), dtype = int)
        b_initial = np.pad(b_initial,(0, 8 -_bin_str.__len__()))
        print("b_initial", b_initial)
        b_reshaped = b_initial.reshape((8,1))

        
        # b = matrix_a * b'+ bit_vector mod 2
        matrix_a = np.array([
            [1,0,0,0,1,1,1,1],
            [1,1,0,0,0,1,1,1],
            [1,1,1,0,0,0,1,1],
            [1,1,1,1,0,0,0,1],
            [1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,0],
            [0,0,0,1,1,1,1,1]
        ], dtype = int)

        bit_vector = np.array([1,1,0,0,0,1,1,0], dtype = int)
        
        multresult = matrix_a.dot(b_reshaped)
        multresult = multresult.reshape((1,8))
        print("mult result", multresult)
        
        b_final = multresult.__add__(bit_vector).ravel()
        
        #do modular operation to get only 0's and 1's 
        b_final = b_final.__mod__(2)
        #reverse the array
        b_final = b_final[::-1]
    
        b_final_str = ''.join(str(x) for x in b_final)

        result = hex(int(b_final_str,2))

        print(result)
        





        
        

s_box_affine_mapping("2f")