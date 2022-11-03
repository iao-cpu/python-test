import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import csv
import pandas as pd

dates, value1, value2 = [], [], []

df = pd.read_csv("c:\\python\\test\\timeseries.csv", usecols=['Date','B1.IPR','B11.IPR'],parse_dates=['Date'],
                                              index_col=['Date'])

with open("c:\\python\\test\\timeseries.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:  
        #print(row)
        #a.append(row) 
        dates.append(row[0])
        value1.append(row[1])
        value2.append(row[2])
print(dates)
print(value1)
print(value2)       

num_row = csvReader.line_num

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Time series from FAME database'
        self.left = 0
        self.top = 0
        self.width = 400
        self.height = 900
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()

    a=0
    b=0
    c=0
    def createTable(self):
         #Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(num_row)
        self.tableWidget.setColumnCount(3)
        i=0
        j=0
        k=0
        while i < num_row:
            self.tableWidget.setItem(i,0, QTableWidgetItem(dates[i]))
            i = i+1
        while j < num_row:
            self.tableWidget.setItem(j, 1, QTableWidgetItem(value1[j]))
            j = j+1
        while k < num_row:
            self.tableWidget.setItem(k, 2, QTableWidgetItem(value2[k]))
            k = k+1

    
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text()) 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  