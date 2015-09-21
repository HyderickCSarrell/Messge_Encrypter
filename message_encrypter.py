'''
Hyderick C. Sarrell
Originally created in 2013
Modified on 19, September 2015


This is the first version of the Text message encrypter and the second revision
It uses the substitution method to encrypt messages that the user enters or a file
given to the program by the user. It also creates a dencryption dictionary to be
used to decrypt the message or the file.

'''

import os
import settings # A file that contains a list for options and the dictionaries
#for encryption and dencryption.

def main():

    '''
        Creates the main menu for the program. Encryption functions are run from
        here.
    '''
    
    print("Welcome to Message Encrypter Ver. 1 Rev. 2.\nPlease select the method of encryption.\n1. Message Encryption\n2. Message Decryption\n3. File Encryption\n4. File Decryption\n5. Exit")
    userinput = int(raw_input())
    if userinput == 1:
        print("Message Encryption selected")
        pass_check()
        pause()
        print("First type in your message:")
        message = str(raw_input())
        message = encryption(message)
        print(message)
        return True
    elif userinput == 2:
        print("Message Decryption selected")
        pass_check()
        pause()
        print("First type in your encrypted message:")
        message = str(raw_input())
        message = decryption(message)
        print(message)
        return True
    elif userinput == 3:
        print("File Encryption selected")
        pass_check()
        pause()
        file_encrypt()
        return True
    elif userinput == 4:
        print("File Decryption selected")
        pass_check()
        pause()
        file_decrypt()
        return True
    elif userinput == 5:
        print("Thanks for using ")
        myvalue = closure()
        return myvalue
    else:
        print("\nError: Invalid reponse!\n")

def pass_check():

    '''
        Asks the user for the password and compares it to the string in the settings
        option list. If the password is incorrect, the function will asks the user
        three more times before returning the false boolean thus closing the program.
    '''
    password = str(raw_input("Please enter the correct security password:"))
    counter = 3
    myvalue = True
    if password == settings.options[0]:
        print("password accepted")
    while counter > 0 and password != settings.options[0]:
        print("incorrect password try again:")
        password = str(raw_input())
        counter = counter-1
    if counter == 0:
        print("Warning: Non-User Ending Program!")
        myvalue = False
    return myvalue

def encryption(message):
    '''
        This is the function that encryptions the text from the files and text.
        It takes the individual characters from the message arguement and encrypts
        them using the default dictionary from the settings file.
    '''
    new_message = ""
    for letter in message:
        if letter in encryptm:
            letter = encryptm[letter]
            new_message = new_message + letter
        else:
            letter = "NT"
            new_message = new_message + letter
    return new_message

def decryption_creation(encryption):
    '''
    This is the function that creates the dictionary that is used to decrypted
    text and files. However it is only temporary and does not modify the dictionary
    in the settings file.
    '''
    
    my_decryption = settings.options[2]
    
    for my_letter in encryptm:
       my_decryption[encryptm[my_letter]] = my_letter

    return my_decryption
       
def decryption(message):
    '''
    This is the function that decrypts messages using the dencryption dictionary.
    It works simiarly to the encryption fuction, however rather than working
    with inidividual characters it works with however many characters are used for
    each character.
    '''
    new_message = ""
    encrypt_num = settings.options[3]
    temp_num = 0
    temp_num2 = encrypt_num
    
    while temp_num2 <= len(message):
        
        letters = message[temp_num:temp_num2]
        
        if letters in my_decryption:
            letters = my_decryption[letters]
            new_message = new_message + letters
            temp_num = temp_num + 2
            temp_num2 = temp_num + 2

        else:
            letters = "NT"
            new_message = new_message + letters
            temp_num = temp_num + 2
            temp_num2 = temp_num2 + 2

    return new_message

def file_encrypt():
    '''
    This is the function that encrypts files. It works by asking the using for
    the name of the file then it searches for the file in the same directory as
    this file. It then copies it contains into a variable then closes the file.
    It then deletes the old file and creates a new one in its place.It uses
    the encryption function to encrypt each line in the varaible and copies it
    to the new file.
    '''
    file_name = raw_input("Please enter the name of the file. Must be in the same directory as this fule and you must include the type. Ex. = monkey.txt:")
    myfile = open(file_name, "r+", 1)
    file_info = myfile.readlines()
    myfile.close()
    os.remove(file_name)
    newfile = open(file_name, "w", 1)
    newline = ""
    for line in file_info:
        if line != "\n":
            line = line.rstrip('\n')
            newline = encryption(line)
            newline = str(newline) + "\n"
            newfile.write(newline)
        else:
            newline = "\n"
            newfile.write(newline)
    newfile.close()

def file_decrypt():
    '''
    This function is used to decrypt files. It works like the encryption method
    but uses the dencryption function to decrypt the file.
    '''
    print("Please enter the name of the file. Must be in the directory as this file and you must include the type. Ex. = monkey.txt")
    file_name = str(raw_input())
    my_file = open(file_name, "r+", 1)
    my_lines = my_file.readlines()
    my_file.close()
    os.remove(file_name)
    new_file = open(file_name, "w", 1)
    for line in my_lines:
        if line != "\n":
            my_sent = line.rstrip('\n')
            my_encsent = decryption(my_sent)
            new_sent = str(my_encsent) + "\n"
            new_file.write(new_sent)
        else:
            newline = "\n"
            new_file.write(newline)
    new_file.close()

def closure():
    '''
    This function is used to close the program. It works by setting the control
    variable to False to end the program loop.
    '''
    print('Press enter to exit...')
    close = raw_input()
    myvalue = False
    return myvalue

def pause():
    '''
    This function is used to pause the program between functions. It works by
    asking the user for input.
    '''
    cont = str(raw_input('Press enter to continue...'))

#This is the control variable
myvalue = True
#These are the dictionaries.
encryptm = settings.options[1]
my_decryption = decryption_creation(encryptm)
#This is the loop that runs the main function and the program.
while myvalue == True:
    myvalue = main()
    if myvalue != False:
        print("complete")
        pause()
