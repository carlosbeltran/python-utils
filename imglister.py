#! /usr/bin/python

import os
import random
import optparse

parser = optparse.OptionParser()

parser.add_option("-d", "--directory", dest="path",
        help="directory where to search for files",metavar="PATH")

parser.add_option("-f", "--file", dest="file",
        help="file where to save the results",metavar="FILENAME")

parser.add_option("-c", "--count", dest="count",
        help="number of images path to save by directory", default=10, metavar="NUMBER")


(opts,args) = parser.parse_args()

#how many files path to save for each subdir
filescount = int(opts.count)

#record original dir
own = os.getcwd()

#go to the new dir
os.chdir(opts.path)

#get the list of dirs in there.
dirs = filter(os.path.isdir, os.listdir("."))

# get the list of files for each dir
for dir in dirs:
    dirpath = os.path.abspath(os.path.join(opts.path,dir))
    print "Processing", dirpath
    dirList = os.listdir(dir)
    randomFiles = random.sample(dirList,filescount)

    for file in sorted(randomFiles):
       print dirpath + "/" + file

#go back to original dir
os.chdir(own)
print os.getcwd()
