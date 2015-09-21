#This is the default dictionary that contains the encryption.
default_encryption = {"A":"J&", "B":"2n", "C":"\$", "D":"4l", "E":"]#", "F":"6j", "G":"3.", "H":"8h", "I":"g_", "J":"0f", "K":"!=", "L":">d", "M":"/b", "N":"/c", "O":"?a",
 "P":"!_", "Q":"Of", "R":";_", "S":"83", "T":"}A", "U":"Jj", "V":"]:", "W":"4V", "X":"X$", "Y":"2 ", "Z":"*$", "1":"Zp", "2":"BG", "3":"Xs", "4":"D#", "5":"V!",
 "6":"FE", "7":"TG", "8":"H.", "9":"R_", "0":"+C", "<":"3z", ">":"L=", ",":"N3", "/":"NA", "?":"L#", "!":"Pz", ":":"JC", ";":"Rx", "{":"H", "}":"Tv", "[":"Ff",
 "]":"Vt", "|":"D_", ")":"?G", "*":"Z$", "&":"91", "%":"qM", "$":"z3", "@":"sR", "#":"75", "~":"u?", ">":"x7", "-":"wS", "_":"5I", "+":"yQ", "=":"vc", "a":" ?",
 "b":"3,", "c":"3Q", "d":"??", "e":"V<", "f":"y:", "g":"59", "h":"w{", "i":"%7", "j":"u[", "k":"7A", "l":"s|", "m":"r3", "n":"q)", "o":"9#", "p":"oA", "q":"%Y",
 "r":"mC", "s":"@W", "t":"kE", "u":"~U", "v":"iG", "w":"-S", "x":"gI", "y":"+Q", "z":"eK", " ":"a0", " `":"cM", "'":"c0", '"':"az"
}
#This is the default dictionary for creating the dencryption
default_decryption = {}
options = ["1234", default_encryption, default_decryption, 2]
# The first object in options is a string to be used as the password.
# The second object is the varaible used to access the encryption dictionary.
# The third object is the variable used to access the decryption dictionary.

    # WARNING! The third item must be empty because the program uses it to create
    # the encryption within the program. It is recommended to not change the
    # third item.

# The last object is an integer to be used to tell the program how many characters
#the message is encrypted with
