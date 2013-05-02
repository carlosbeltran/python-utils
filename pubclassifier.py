#! /usr/bin/python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

lista = ['aa', 'ab', 'ac']
listb = ['ba', 'bb', 'bc']
listc = ['ca', 'cb', 'cc']

topiclist = ['Social Signal Processing',
        'Video Analytics',
        'Acoustic Signal Processing',
        'Sensor and Data Fusion, Mobile Sensing 3D Modeling and Analysis',
        'Machine Learning Mouse Behavior Analysis In-Vitro Neuronal Network',
        'Analysis Structural and Functional Brain Connectivity Analysis',
        'Clustering Analysis for drug discovery',
        'Other works']

mystruct = {'A':lista, 'B':listb, 'C':listc}

class MyTable(QTableWidget):
    def __init__(self, thestruct, *args):
        QTableWidget.__init__(self, *args)
        self.data = thestruct
        self.combo = QComboBox()

        for topic in topiclist:
            self.combo.addItem(topic)

        self.setmydata()
        
        
    def setmydata(self):
        n = 0
        for key in self.data:
            m = 0
            for item in self.data[key]:
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
                m += 1
            self.setCellWidget(m,n,self.combo)
            n += 1

def main(args):
    app = QApplication(args)
    table = MyTable(mystruct, 5, 3)
    table.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main(sys.argv)
