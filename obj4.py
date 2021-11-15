import pymongo
import pandas as pd
import json


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from syfx22 import *


class  dnx():
    def __init__(self):
        self.uyg=QApplication(sys.argv)
        self.penAna=QMainWindow()
        self.ui=Ui_MainWindow()

        self.ui.setupUi(self.penAna)
        self.penAna.show()


        self.myc=pymongo.MongoClient("mongodb://localhost:27017")

        self.mydb=self.myc["deneme2"]
        self.mycll= self.mydb["dn1"]
        self.ui.pushButton.clicked.connect(self.veral)
        self.sonx=self.mycll.find({},{'Countries':1})
        self.sonxx=self.mycll.find({},{'Countries':1})


        for i in self.sonx:
    #print(i['Countries'][1]['Country'])
            self.sonx1=i['Countries']

            for s in self.sonx1:      
               
        
                self.k=s.get('Country','kkkk')
        
                self.ui.comboBox.addItem(self.k)
         
        for i in self.sonxx:
    
            self.sonx11=i['Countries']
            self.c=pd.DataFrame(data=self.sonx11)       
    def veral(self):
        self.a=self.ui.comboBox.currentText()
        print(self.a)
    #a=prd[7][4]

        self.m=self.c[self.c['Country'].str.contains(self.a)]
        #y=self.m.loc[:,"TotalDeaths"]
        self.ui.tableWidget.setItem(0,1,QTableWidgetItem(str(self.m.iloc[0,1])))
        self.ui.tableWidget.setItem(0,2,QTableWidgetItem(str(self.m.iloc[0,5])))
        self.ui.tableWidget.setItem(0,3,QTableWidgetItem(str(self.m.iloc[0,7])))

            

gn=dnx()

gn
#ui.pushButton.clicked.connect(gn.veral)
#gn.veral
