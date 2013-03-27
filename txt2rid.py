#! /usr/bin/python

import os
import optparse
import fnmatch
import shutil


def getfileslist(path, extfilter):
   #record original dir
   own = os.getcwd()
   #go to the new dir
   os.chdir(path)
   print path
   
   files = filter(os.path.isfile, os.listdir("."))
   files = sorted ([f for f in files if fnmatch.fnmatch(f,extfilter)])
   os.chdir(own)
   return files

parser = optparse.OptionParser()

parser.add_option("-i", "--imagesdirectory", dest="imagespath",
        help="directory where to search for files",metavar="IMGPATH")

(opts,args) = parser.parse_args()

counter = 0

imgfiles = getfileslist(opts.imagespath,"*.jpg")

for file in imgfiles:
    #newname = "I%.3d.jpg" % counter;
    #counter += 1
    #shutil.copyfile(file,newname)
    print opts.imagespath + file 

#go back to original dir

