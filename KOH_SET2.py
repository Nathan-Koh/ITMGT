#!/usr/bin/env python
# coding: utf-8

# In[198]:


def shift_letter(letter, shift):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if letter == " ":
        return(" ")
    elif shift + alphabet.index(letter) > 25: 
        return(letter.replace(letter, alphabet[alphabet.index(str(letter)) + shift - 26*(1+(shift//26)) ]))
    else:
        return(letter.replace(letter, alphabet[alphabet.index(str(letter)) + shift]))


# In[199]:


def caesar_cipher(message, shift):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ""
    for x in message:
        if x == " ":
            new_message += " "
        else:
            if shift + alphabet.index(x) > 25: 
                new_message += alphabet[alphabet.index(str(x)) + shift - 26*(1+(shift//26))]
            else:
                new_message += alphabet[alphabet.index(str(x)) + shift]
    return new_message


# In[200]:


def shift_by_letter(letter, letter_shift):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = alphabet.index(letter_shift)

    if letter == " ":
        return(" ")
    elif shift + alphabet.index(letter) > 25: 
        return(alphabet[alphabet.index(str(letter)) + shift - 26*(1+(shift//26)) ])
    else:
        return(alphabet[alphabet.index(str(letter)) + shift])



# In[201]:


def vigenere_cipher(message, key):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_key = key*((len(message)//len(key))+1)
    new_message = ""
    counter = 0

    for x in message:
        if message[counter] == " ":
            new_message += " "
            counter += 1
        elif alphabet.index(new_key[counter]) + alphabet.index(message[counter]) > 25: 
            new_message += alphabet[alphabet.index(message[counter]) + alphabet.index(new_key[counter]) - 26*(1+(alphabet.index(new_key[counter])//26))]
            counter += 1
        else:
            new_message += alphabet[alphabet.index(message[counter]) + alphabet.index(new_key[counter])]
            counter += 1
    return new_message




# In[202]:


def scytale_cipher(message, shift):

    if len(message)%shift == 0:
        message = message
    else:
        message = message + "_"*(shift-len(message)%shift)
    encoded_message = ""
    counter = 0

    for i in message:
            encoded_message += message[(counter // shift) + (len(message) // shift) * (counter % shift)]
            counter += 1 
    return encoded_message



# In[197]:


def scytale_decipher(message, shift):
   
    decoded_message = ""
    counter = 0
    for i in message:
        decoded_message += message[(counter*shift)%(len(message))+(counter*shift)//(len(message))]
        counter += 1
    return decoded_message



# In[ ]:





# In[ ]:




