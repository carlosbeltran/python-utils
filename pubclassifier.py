#! /usr/bin/python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#lista = ['aa', 'ab', 'ac']
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

class MyTable(QTableWidget):
    def __init__(self, *args):
        QTableWidget.__init__(self, *args)
        self.buildtablestruct()
        self.verticalHeader().setDefaultSectionSize(100)
        self.horizontalHeader().setDefaultSectionSize(500)
        self.resize(1000,500*2)

    def buildtablestruct(self):
        for i in range(len(lista)):
            newitem = QTableWidgetItem(lista[i])
    
            combo = QComboBox()
            for topic in topiclist:
                combo.addItem(topic)

            self.setItem(i,0,newitem)
            self.setCellWidget(i,1,combo)

def main(args):
    app = QApplication(args)
    table = MyTable(len(lista), 2)
    table.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main(sys.argv)
