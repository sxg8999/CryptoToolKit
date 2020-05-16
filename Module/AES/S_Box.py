import numpy as np


def s_box_affine_mapping(_val, config = "ENCRYPTION"):
        """
        Preconditions: 
            -_val is a string representation of a hexadecimal value
            - if config = ENCRYPTION then _val must be the inverse of the original hexadecimal value
                    
        """
        matrix_dict = {
            "ENCRYPTION" : [
            [1,0,0,0,1,1,1,1],
            [1,1,0,0,0,1,1,1],
            [1,1,1,0,0,0,1,1],
            [1,1,1,1,0,0,0,1],
            [1,1,1,1,1,0,0,0],
            [0,1,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,0],
            [0,0,0,1,1,1,1,1]
        ],
            "DECRYPTION" : [
            [0,0,1,0,0,1,0,1],
            [1,0,0,1,0,0,1,0],
            [0,1,0,0,1,0,0,1],
            [1,0,1,0,0,1,0,0],
            [0,1,0,1,0,0,1,0],
            [0,0,1,0,1,0,0,1],
            [1,0,0,1,0,1,0,0],
            [0,1,0,0,1,0,1,0]
        ]
        }

        bit_vector_dict ={
            "ENCRYPTION":[1,1,0,0,0,1,1,0],
            "DECRYPTION":[1,0,1,0,0,0,0,0]
        }

        matrix = np.array(matrix_dict.get(config), dtype = int)
        bit_vector = np.array(bit_vector_dict.get(config), dtype = int)


        _hexVal = int(_val,16)  #converts inverseVal to hex
        _binVal = bin(_hexVal)        #converst the hexVal to binary
        _bin_str = str(_binVal)[2:]
        _bin_str = _bin_str[::-1]     #reverse the string

        b_initial = np.array(list(_bin_str.strip()), dtype = int)
        b_initial = np.pad(b_initial,(0, 8 -_bin_str.__len__()))
        
        b_reshaped = b_initial.reshape((8,1))

        
        multresult = matrix.dot(b_reshaped)
        multresult = multresult.reshape((1,8))
    
        
        b_final = multresult.__add__(bit_vector).ravel()
        
        #do modular operation to get only 0's and 1's 
        b_final = b_final.__mod__(2)
        #reverse the array
        b_final = b_final[::-1]
    
        b_final_str = ''.join(str(x) for x in b_final)

        result = hex(int(b_final_str,2))

        print(result)
        

        
        

s_box_affine_mapping("2f")                          #OUTPUT: 0x25
s_box_affine_mapping("25", config = "DECRYPTION")   #OUTPUT: 0x2F