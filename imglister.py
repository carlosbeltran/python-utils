#! /usr/bin/python

import os
import random

path = "."
filescount = 10 

#for root, dirs, files in os.walk(path):
#dirs = os.listdir(path)
dirs = filter(os.path.isdir, os.listdir(path))

for dir in dirs:
    dirpath = os.path.abspath(os.path.join(path,dir))
    print "Processing", dirpath
    dirList = os.listdir(dir)
    randomFiles = random.sample(dirList,filescount)

    for file in sorted(randomFiles):
       print dirpath + "/" + file
