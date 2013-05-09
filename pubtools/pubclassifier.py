#! /usr/bin/python

import cPickle
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

topiclist = ['Social Signal Processing',
        'Video Analytics',
        'Acoustic Signal Processing',
        'Sensor and Data Fusion, Mobile Sensing',
        '3D Modeling and Analysis',
        'Machine Learning',
        'Mouse Behavior Analysis',
        'In-Vitro Neuronal Network Analysis',
        'Structural and Functional Brain Connectivity Analysis',
        'Clustering Analysis for drug discovery',
        'Other works']

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setuptable()
        self.initUI()

    def initUI(self):
        #exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction('Save',self)
        saveAction.setShortcut('Ctrl-S')
        saveAction.setStatusTip('Save current table')
        saveAction.triggered.connect(self.savetable)

        loadAction = QAction('Load',self)
        loadAction.setShortcut('Ctrl-S')
        loadAction.setStatusTip('Load a pickle table')
        loadAction.triggered.connect(self.loadtable)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)

        self.statusBar().showMessage('Ready')
        self.setGeometry(300,500,1000,500)
        self.setWindowTitle('Statusbar')

    def setuptable(self):
        f = open("final.txt",'r')
        lista = f.readlines()
        
        self.table = MyTable(lista,topiclist,len(lista), 2)
        self.setCentralWidget(self.table)

    def savetable(self):
        print "Saving..."
        self.table.pickledump()

    def loadtable(self):
        print "Load..."
        self.table.pickleload()

class MyTable(QTableWidget):
    def __init__(self, list1,list2,*args):
        QTableWidget.__init__(self, *args)
        self.verticalHeader().setDefaultSectionSize(100)
        self.horizontalHeader().setDefaultSectionSize(500)
        self.resize(1000,500*2)
        self.buildtablestruct(list1,list2)

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
        return content

    def pickledump(self):
        outfile = open("data.txt","wb")
        completelist = self.table2list()
        cPickle.dump(completelist,outfile)
        outfile.close()

    def pickleload(self):
        lista = []
        savedtopiclist = []
        infile = open("data.txt","rb")
        completelist = cPickle.load(infile)
        infile.close()
        for item in completelist:
            lista.append(item[0])
            savedtopiclist.append(item[1])
        self.buildtablestruct(lista,topiclist)
        #recover saved combobox selections
        for row in range(self.rowCount()):
            index = self.cellWidget(row,1).findText(savedtopiclist[row])
            self.cellWidget(row,1).setCurrentIndex(index)


def main(args):
    app = QApplication(args)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main(sys.argv)
