#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bin_to_dec(binary_string):

    integer = 0
    for i in range(0, len(binary_string)):
        integer += int(binary_string[i])*(2**(len(binary_string)-1-i))

    return integer
    


# In[2]:


def dec_to_bin(number):

    binary = ""
    integer = int(number)
    n = 1
    exponent = 0

    # special case for code
    if number == 0:
        return "0"
    if number == 1:
        return "1"
        
    # find largest power of 2
    while number//n != 1:
        n = 2**exponent
        exponent += 1
        
    for i in range(exponent-1, -1, -1):
        if integer//2**i == 1:
            binary += "1" 
            integer = integer - 2**i
        else:
            binary += "0" 
    
    return binary


# In[3]:


def telephone_cipher(message):

    output = ""
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

    for i in range(0, len(message)):
        if output == "":
            output += encoder_dict[message[i]]

        elif output[len(output)-1] == encoder_dict[message[i]][0]:
            output += "_" + encoder_dict[message[i]]
            
        else:
            output += encoder_dict[message[i]]

    return output


# In[4]:


def telephone_decipher(telephone_string):
   
    output = ""
    counter = 0
    key = ""
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }

    while counter < len(telephone_string):
        if telephone_string[counter] == "_":
            counter += 1
            continue
        else:
            key += telephone_string[counter] # for first number
            if counter == (len(telephone_string) -1):
                pass
            else:
                while telephone_string[counter] == telephone_string[counter+1]: # for any succeeding similar numbers
                    key += telephone_string[counter]
                    counter += 1
                    if counter == (len(telephone_string) -1):
                        break
            output += decipher_dict[key]
            counter += 1
            key = ""

    return output


# In[ ]:





# In[ ]:




