#spams the directory with text files

import os

max = 100
i = 1

def spam():
    f = open("asdf" + str(i) + ".txt", "a")
    for x in range(2000):
        f.write("spam\n")
    print("Created " + "asdf" + str(i) + ".txt")
    f.close()

def unspam():
    os.remove("asdf" + str(i) + ".txt")
    print("Deleted " + "asdf" + str(i) + ".txt")

while(i <= max):
    spam()
    unspam()
    i += 1

