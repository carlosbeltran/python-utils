#! /usr/bin/python

import cPickle
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,500,1000,500)
        self.setWindowTitle('Statusbar')
        f = open("final.txt",'r')
        lista = f.readlines()
        
        topiclist = ['Social Signal Processing',
                'Video Analytics',
                'Acoustic Signal Processing',
                'Sensor and Data Fusion, Mobile Sensing 3D Modeling and Analysis',
                'Machine Learning Mouse Behavior Analysis In-Vitro Neuronal Network',
                'Analysis Structural and Functional Brain Connectivity Analysis',
                'Clustering Analysis for drug discovery',
                'Other works']
        self.table = MyTable(lista,topiclist,len(lista), 2)
        self.setCentralWidget(self.table)

class MyTable(QTableWidget):
    def __init__(self, list1,list2,*args):
        QTableWidget.__init__(self, *args)
        #self.buildtablestruct(list1,list2)
        self.pickleload()
        self.verticalHeader().setDefaultSectionSize(100)
        self.horizontalHeader().setDefaultSectionSize(500)
        self.resize(1000,500*2)

    def buildtablestruct(self, listapubs,topiclist):
        for i in range(len(listapubs)):
            newitem = QTableWidgetItem(listapubs[i])
    
            combo = QComboBox()
            for topic in topiclist:
                combo.addItem(topic)

            self.setItem(i,0,newitem)
            self.setCellWidget(i,1,combo)

    def table2list(self):
        content = []
        for row in range(self.rowCount()):
            content.append([str(self.item(row,0).text().toUtf8()).strip(), str(self.cellWidget(row,1).currentText())])
            #sys.stdout.write(str(row) + " " +self.cellWidget(row,1).currentText())
            #sys.stdout.write("  ")
        return content

    def pickledump(self):
        outfile = open("data.txt","wb")
        completelist = self.table2list()
        cPickle.dump(completelist,outfile)
        outfile.close()

    def pickleload(self):
        lista = []
        topiclist = []
        infile = open("data.txt","rb")
        completelist = cPickle.load(infile)
        infile.close()
        for item in completelist:
            lista.append(item[0])
            topiclist.append(item[1])
        self.buildtablestruct(lista,topiclist)

def main(args):
    app = QApplication(args)
    mainwindow = MainWindow()
    mainwindow.show()
    #table.show()
    #table.pickledump()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main(sys.argv)
