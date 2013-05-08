#! /usr/bin/python

import xlwt
import cPickle
import sys
import textwrap


lista = []
savedtopiclist = []
infile = open("data.txt","rb")
completelist = cPickle.load(infile)
infile.close()

book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
first_col = sheet1.col(0)
first_col.height = 256 * 4

#tall_style = xlwt.easyxf('font:height 720;') # 36pt

for i,item in enumerate(completelist):
    sheet1.write(i,0,textwrap.fill(str(item[0])))
    sheet1.write(i,1,str(item[1]))
    #sheet1.row(i).set_style(tall_style)

name = "random.xls"
book.save(name)

