#! /usr/bin/python

import os
import optparse
import fnmatch
import shutil
import re

own = ''

parser = optparse.OptionParser()

parser.add_option("-d", "--directory", dest="path",
        help="directory where to search for files",metavar="PATH")
parser.add_option("-i", "--index", dest="index",
        help="index to add to the images",metavar="INDEX")

(opts,args) = parser.parse_args()

counter = 0

if (opts.path):
   #record original dir
   own = os.getcwd()
   #go to the new dir
   os.chdir(opts.path)
   print opts.path

files = filter(os.path.isfile, os.listdir("."))
print files
#files = sorted ([f for f in files if fnmatch.fnmatch(f,opts.path+'*.jpg')])

for file in files:
    m = re.match('(\d\d\d).jpg',file)

    newname = opts.path + "%.4d%.3d.jpg" % (int(m.group(1)),int(opts.index) )
    file = opts.path + file
    shutil.move(file,newname)
    print file + " --->  " + newname

#go back to original dir
os.chdir(own)

