#! /usr/bin/python

import os
import random
import optparse

parser = optparse.OptionParser()

parser.add_option("-d", "--directory", dest="path",
        help="directory where to search for files",metavar="PATH")


(opts,args) = parser.parse_args()
filescount = 10 
print opts.path

os.chdir(opts.path)
dirs = filter(os.path.isdir, os.listdir("."))

print dirs

for dir in dirs:
    dirpath = os.path.abspath(os.path.join(opts.path,dir))
    print "Processing", dirpath
    dirList = os.listdir(dir)
    randomFiles = random.sample(dirList,filescount)

    for file in sorted(randomFiles):
       print dirpath + "/" + file
