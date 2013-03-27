#! /usr/bin/python

import os
import optparse
import fnmatch
import shutil
import sys
import pygame
import time


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
    locations = []
    for line in f.readlines()[1:]:
        locations.append(line.strip().split()[:5])
    return locations

if __name__ == '__main__':

    parser = optparse.OptionParser()
    
    parser.add_option("-i", "--imagesdirectory", dest="imagespath",
            help="directory where to search for images files",metavar="IMGPATH")
    
    parser.add_option("-t", "--textsdirectory", dest="txtspath",
            help ="directory where to search for txt files (Dollar format)", 
            metavar="TXTPATH")
    
    (opts,args) = parser.parse_args()
    
    pygame.init()
    w = 1260
    h = 960
    size = (w,h)
    screen = pygame.display.set_mode(size)
    c = pygame.time.Clock()

    txtfiles = getfileslist(opts.txtspath, "*.txt")
    imgfiles = getfileslist(opts.imagespath,"*.jpg")
    
    for img,txt in zip(imgfiles,txtfiles):
        #print opts.imagespath + file 
        theimg = pygame.image.load(opts.imagespath+img)
        print img + " --> " + txt
        boundingboxes = getbbfromfile(opts.txtspath+txt)
        for bb in boundingboxes:
            print bb
            print "----> " + bb[1] + " " + bb[2] + " " + bb[3] + " " + bb[4]
            pygame.draw.rect(theimg, pygame.Color(255,0,0), pygame.Rect(int(bb[1]),int(bb[2]),int(bb[3]),int(bb[4])),2)
        screen.blit(theimg,(0,0))
        pygame.display.flip()

