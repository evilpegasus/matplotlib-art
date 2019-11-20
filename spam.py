#spams the directory with text files

import os

max = 500
i = 1
j = 1
file_path = "C:\\Users\\min.fon000\\Desktop\\"


def spam():
    f = open("asdf" + str(i) + ".txt", "a")
    for x in range(2000):
        f.write("spam\n")
    print("Created " + os.getcwd() + "\asdf" + str(i) + ".txt")
    f.close()

def spam_desktop():
    f = open(file_path + "asdf" + str(i) + ".txt", "a")
    for x in range(2000):
        f.write("spam\n")
    print("Created " + os.getcwd() + "\asdf" + str(i) + ".txt")
    f.close()

def unspam_desktop():
    os.remove(file_path + "asdf" + str(i) + ".txt")
    print("Deleted " + os.getcwd() + "\asdf" + str(i) + ".txt")

def unspam():
    os.remove("asdf" + str(i) + ".txt")
    print("Deleted " + os.getcwd() + "\asdf" + str(i) + ".txt")

while(j <= 10):
    while(i <= max):
        #spam()
        unspam()
        #spam_desktop()
        #unspam_desktop()
        i += 1
    os.chdir("..")
    print("Changed directory to " + os.getcwd())
    i = 1