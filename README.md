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

The message encrypter file is the main program and contains all the functions that run the program. It starts by importing the settings and 
operating systems module. The main function is created first as it will create the interface that the user interacts with. It asks the user 
for a number from the interface and runs the corresponding code. If the user enters any number other than one listed on the interface, it will 
tell the user that they have entered an invalid response. 

The interface lists five choices to the user. The first choice is called message encryption; it starts by telling the user that they have 
selected the choice and then running the pass check function. Pass check is the second function created after main. It asks for user for the 
password and then compares it to the string in the options list. If the user enters the wrong password, pass check will ask the user three more 
times before it closes the program. This function is used in all the choices given to the user except for the last one.

The next function message encryption uses is the pause function. Pause is also used in almost all the choices and is the last function in the program. 
It is used to create a delay in the program so the user can understand what is going on. It works by asking the user to press enter to continue. Next, 
main prompts the user to enter the message they would like to encrypt and it passes it to the encryption function.

Encryption is the third function in the program. It works by taking the message and changing each character to an encrypted set. To do this it uses the 
variable encrypt-m, which contains default encryption. It compares each character in the message to one of the dictionary’s keys, and concatenates its 
value to a variable called new-message. Once the program has completed this process, it returns new-message to the variable message and prints it to the 
screen.

The second choice is called message decryption. It works just like message encryption except it takes the message that is already encrypted and uses the 
decryption function to decrypt it. Decryption is similar to encryption; however, it doesn’t necessarily read one character at a time. It using a while loop 
and two control variables based on the integer in options. This allows the user to use any number of characters to encrypt a single character. In order for 
decryption to work it needs a dictionary to work from, which is created in the decryption creation function.

Decryption creation uses encrypt-m to add elements to the decryption dictionary. It works by iterating through the dictionary and taking the value of each 
key and swapping it with the key. Then it adds the values to the variable my decryption which is returned to another variable later in the program.

The next two choices given to the user are file encryption and file decryption. They both work by asking the user for the name of the file rather than the 
message. Based on the user’s choice, the name is then passed to the appropriate function, either file encrypt or file decrypt. Once the function has the file, 
it will open it and copy its contents to a variable. It then closes that file, deletes it, and creates a new file of the same name. Then it takes each line and 
removes the newline character. It passes that line to the function, encryption or decryption, which will translate it and pass it back. Finally, it writes the 
line to the new file, and repeats the process until it has finished. The function then closes the file. 

The last choice of the interface is the exit choice. This choice closes the program by returning the Boolean value False to main, which returns it to the loop’s 
control variable. The only way main will return false is if the user selects exit. This way the program will continue to run.

The original intention I had for creating the Message Encrypter program was for people to send messages to their friends through Facebook. Two people would have 
the program with the same encryption settings. One person would encrypt messages with the program then copy and paste it to Facebook. The other would copy the message 
into the program and decrypt it. This would enhance their privacy and make Facebook more fun to use. I still work on the program and hope to one day make it an app.

