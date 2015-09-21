Hyderick C. Sarrell

The Message Encrypter / Text Message Encryption Program

September 19, 2015

The Message Encrypter is a Python program that I created in early 2013. This version was started later that year and completed 
soon after. It works by asking the user to input a message then the program encrypts it using an encryption dictionary. The 
program can also decrypt the message by using a decryption dictionary created from the encryption dictionary. Using the same 
encryption methods, the program can receive and encrypt files with the same encryptions functions.

The dictionaries are stored in a separate file called settings. The default encryption dictionary stores the encryption that I 
created myself, and it stores the encryption by using the keyboard character as the key and its encryption as the value. However,
the dictionary is empty inside the settings file, because it is created inside the program. This saves the user time when creating 
their own encryption as well as making sure it is accurate. The options list is the only other item contained inside the settings file.

The list contains four items that are used by the program. The first is a string value that is used as a password for the program. 
The second contains the default encryption and the third item is the default decryption. By storing the dictionaries in the list, I 
allow the user to create and use his or her own encryptions. The last item in the list is an integer, and it used to determine how many 
characters each character is encrypted with.

