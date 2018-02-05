# -*- coding: utf-8 -*-
import os


def mkmydr(_path):
    try:
        if not os.path.exists(_path):
            os.mkdir(_path)
    except:
        print "error in FileIO.mkdir" + _path


def read(path):
    try:
        open(path, 'r').read().strip()
    except:
        print "error in FileIO.read(" + path + ")"


def write(path, Str):
    open(path, 'w').write(Str)


# try:
# open(path,'w').write(Str)
# except:
# print "error in FileIO.write("+path+")"
def append(path, Str):
    open(path, 'a').write(Str)


# try:
# open(path,'a').write(Str)
# except:
# print "error in FileIO.append("+path+")"
if __name__ == "__main__":
    # print read("FileIO.py")
    append("data/id_profile.txt", "123")
# print read("FileIO1.py")
