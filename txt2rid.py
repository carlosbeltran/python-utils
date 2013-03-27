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

def getbbfromfile(file):
    f = open(file,'r');
    for line in f.readlines()[1:]:
        print line.strip().split()[:5]

parser = optparse.OptionParser()

parser.add_option("-i", "--imagesdirectory", dest="imagespath",
        help="directory where to search for images files",metavar="IMGPATH")

parser.add_option("-t", "--textsdirectory", dest="txtspath",
        help ="directory where to search for txt files (Dollar format)", 
        metavar="TXTPATH")

(opts,args) = parser.parse_args()

counter = 0

txtfiles = getfileslist(opts.txtspath, "*.txt")
imgfiles = getfileslist(opts.imagespath,"*.jpg")

for img,txt in zip(imgfiles,txtfiles):
    #print opts.imagespath + file 
    print img + " --> " + txt
    getbbfromfile(opts.txtspath+txt)

#go back to original dir

