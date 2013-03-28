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
parser.add_option("-i", "--sourcepattern", dest="sourcepattern",
        help="the original file pattern to parse",metavar="SOURCE")
parser.add_option("-o", "--destpattern", dest="destpattern",
        help="the final file pattern you want",metavar="DEST")

(opts,args) = parser.parse_args()

counter = 0

if (opts.path):
   #record original dir
   own = os.getcwd()
   #go to the new dir
   os.chdir(opts.path)
   print opts.path

files = filter(os.path.isfile, os.listdir("."))
files = sorted ([f for f in files if fnmatch.fnmatch(f,opts.sourcepattern+'*.jpg')])

for file in files:
    m = re.match('(\d\d\d\d)(\d\d\d)',file)

    newname = opts.path + "%.4d%.3d.jpg" % (int(opts.destpattern), int(m.group(2)))
    file = opts.path + file
    #counter += 1
    shutil.move(file,newname)
    print file + " --->  " + newname

#go back to original dir
os.chdir(own)

