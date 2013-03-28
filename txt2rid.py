#! /usr/bin/python

import os
import optparse
import fnmatch
import shutil
import sys
#import pygame
import time
from PIL import Image


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
    
    people = {}
    #pygame.init()
    #w = 1260
    #h = 960
    #size = (w,h)
    #screen = pygame.display.set_mode(size)
    #c = pygame.time.Clock()

    txtfiles = getfileslist(opts.txtspath, "*.txt")
    imgfiles = getfileslist(opts.imagespath,"*.jpg")
    
    for img,txt in zip(imgfiles,txtfiles):
        #print opts.imagespath + file 
        imgpath = opts.imagespath+img
        #theimg = pygame.image.load(imgpath)
        pilimg = Image.open(imgpath)
        print img + " --> " + txt
        boundingboxes = getbbfromfile(opts.txtspath+txt)
        for bb in boundingboxes:
            #check dic
            personid = bb[0]
            if personid in people:
                people[personid] = people[personid] + 1
            else:
                people[personid] = 1

            print bb
            print "----> " + bb[1] + " " + bb[2] + " " + bb[3] + " " + bb[4]

            #pygame.draw.rect(theimg, pygame.Color(255,0,0), pygame.Rect(int(bb[1]),int(bb[2]),int(bb[3]),int(bb[4])),2)
            box = (int(bb[1]),int(bb[2]), int(bb[1])+int(bb[3]), int(bb[2])+int(bb[4]))
            area = pilimg.crop(box)
            newimgname = personid + str(people[personid]) + ".jpg"
            area.save(opts.imagespath + newimgname,'jpeg')
        #screen.blit(theimg,(0,0))
        #pygame.display.flip()
    print people

