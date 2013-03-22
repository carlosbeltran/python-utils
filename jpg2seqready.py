#! /usr/bin/python

import os
import optparse
import fnmatch
import shutil

path = "."
counter = 0

files = filter(os.path.isfile, os.listdir(path))
files = sorted ([f for f in files if fnmatch.fnmatch(f,'*.jpg')])

for file in files:
    newname = "I%.3d.jpg" % counter;
    counter += 1
    shutil.copyfile(file,newname)
    print file + " --->  " + newname

#print files 
#files = sorted(files)
#for file in files:
#    if fnmatch.fnmatch(file, '*.jpg'):
#        print file

