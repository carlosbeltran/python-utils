#! /usr/bin/python

import os
import optparse
import fnmatch
import shutil

own = ''

parser = optparse.OptionParser()

parser.add_option("-d", "--directory", dest="path",
        help="directory where to search for files",metavar="PATH")

(opts,args) = parser.parse_args()

counter = 0

if (opts.path):
   #record original dir
   own = os.getcwd()
   #go to the new dir
   os.chdir(opts.path)
   print opts.path

files = filter(os.path.isfile, os.listdir("."))
files = sorted ([f for f in files if fnmatch.fnmatch(f,'*.jpg')])

for file in files:
    newname = "I%.3d.jpg" % counter;
    counter += 1
    shutil.copyfile(file,newname)
    print file + " --->  " + newname

#go back to original dir
os.chdir(own)

