from PyQt5 import QtWidgets
from UI import Ui_MainWindow
import sys
import os
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly as py
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import io


class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ######## create html file #######
        file = open("graph.html", "w")
        file.close()
        ############Preprocessing #################
        self.dataset1 = pd.read_csv('covid_19_clean_complete.csv')
        self.dataset2 = pd.read_csv('COVID19_line_list_data.csv')
        self.dataset1 = self.dataset1.iloc[:1000,:]
        # replacing Mainland china with just China
        self.dataset1['Country/Region'] = self.dataset1['Country/Region'].replace('Mainland China', 'China')
        # Replace missing values with a number
        self.dataset1["Province/State"].fillna("Not Found", inplace=True)
        self.dataset2["gender"].fillna("Not Found", inplace=True)
        ########Connections ############  
        list_buttons=[self.ui.comboBox,self.ui.comboBox,self.ui.comboBox,self.ui.comboBoxMap,self.ui.comboBox_lengthBar,
                    self.ui.comboBox_SortBars,self.ui.comboBox_lengthBar]
        list_fns=[self.visual_options,self.sorted_comboBox,self.map_control,self.map_control,self.comboBoxBar_control,
                self.sorted_comboBox,self.sorted_comboBox]
        for i in range(len(list_buttons)):
            list_buttons[i].currentIndexChanged.connect(list_fns[i])


    def visual_options(self):
        self.curr_index = self.ui.comboBox.currentIndex()
        if (self.curr_index==1):
            self.load_Bubble1()
            self.message("Please Wait................................")
        elif(self.curr_index ==2):
            self.map_control()
            self.message("Please Select from Map Color ComboBox only ")
        elif (self.curr_index==3):
            self.comboBoxBar_control()
            self.message("Please select from Bars Length and Bars sorting ComboBoxes only")
        elif (self.curr_index==4):
            self.Load_bubble2()
            self.message("Please Wait...................................")


    def load_Bubble1 (self):
        fig = px.scatter(self.dataset1,x="Deaths", y="Recovered",animation_frame="Date", animation_group="Province/State",
                size="Confirmed",color="Country/Region", hover_name="Province/State",log_x=True , log_y=True,size_max=500,
                range_x=[0.1,1000000000], range_y=[0.1,1000000000000000000000000000000000],title='Recovered vs Death (Log10 Scale )' )

        self.html(fig)

    def Load_bubble2(self):      
        fig = px.scatter(self.dataset2,x="age", y="case_in_country",animation_frame="reporting date",
        animation_group="gender", size="case_in_country" ,  color="country",
        hover_name="gender" ,size_max=300 ,log_x=True , log_y=True,
        range_x=[0.1,150], range_y=[0.1,10000000],
        title=' Cases vs Ages(Log10 Scale )')
        
        self.html(fig)

    
    def map_control(self):
        self.curr_main = self.ui .comboBox.currentIndex()
        self.curr_index = self.ui.comboBoxMap.currentIndex()
        self.Load_map(self.curr_main,self.curr_index)

    def Load_map(self,curr_main , curr_index):
        #self.curr_index = self.ui.comboBoxMap.currentIndex()
        if(curr_main == 2):
            if (curr_index ==1):

                fig = px.choropleth(self.dataset1 , locations="Country/Region" ,locationmode="country names", color="Confirmed" , hover_name="Country/Region" ,
                                animation_frame="Date" ,animation_group="Confirmed",color_continuous_scale="Viridis",range_color=(0, 8000),title=' Cases Of COVID19 all over the World')                      
                self.html(fig)

            elif (curr_index==2):
                fig = px.choropleth(self.dataset1 , locations="Country/Region" ,locationmode="country names", color="Deaths" , hover_name="Country/Region" ,
                                animation_frame="Date" ,animation_group="Deaths",range_color=(0, 8000),title=' Deaths Of COVID19 all over the World')                               
                self.html(fig)
    

    def comboBoxBar_control(self):
        self.curr_index1 = self.ui.comboBox_lengthBar.currentIndex()
        
        if (self.curr_index1 == 1):
            self.item("Number of Cases in each Country.")
  
        elif (self.curr_index1==2 ):
            self.item("Number of Deaths in each Country.")
        
        elif (self.curr_index1==3):
            self.item("Both # of Cases and # of Deaths in each Country.")

    def item(self,text):
        self.ui.comboBox_SortBars.clear()
        items=["Bars sorted by :",  text]
        for i in items:
            self.ui.comboBox_SortBars.addItem(i)


    def sorted_comboBox(self):
        curr_index = self.ui.comboBox.currentIndex()
        curr_index1 = self.ui.comboBox_lengthBar.currentIndex()
        curr_index2 = self.ui.comboBox_SortBars.currentIndex()
        self.Load_bar(curr_index,curr_index1,curr_index2)


    
    def Load_bar(self,curr_index,curr_index1,curr_index2):
        if (curr_index == 3):
            if (curr_index1==1 and curr_index2==1):
                self.plot(self.dataset1,"Confirmed","Sorting of Countries By Number of Cases of COVID19")
                
            elif (curr_index1==2 and  curr_index2==1):    
                self.plot(self.dataset1,"Deaths","Sorting of Countries By Number of Deaths")   
                
            elif(curr_index1==3 and curr_index2==1):
                Total = self.dataset1["Confirmed"]+self.dataset1["Deaths"]
                self.dataset1["DeathsPLUSConfirmed"] = Total
                self.plot(self.dataset1,"DeathsPLUSConfirmed","Sorting of Countries By Number of Cases and Number of Deaths of COVID19")
                
    def plot(self,dataset,y,title):
        fig = px.bar(dataset, x="Country/Region", y=y,animation_frame="Date", color="Country/Region",width=1400,
                            height=720,template='gridon', range_y=[0,50000] ,title=title)
                
        fig.update_layout(xaxis={'categoryorder':'total descending'})
        self.html(fig)
        
    def html(self,fig):
        py.io.write_html(fig,"graph.html")
        path = os.path.abspath(os.path.join(os.path.dirname(__file__),"graph.html"))
        self.ui.widget.load(QUrl.fromLocalFile(path))

    def message(self,value):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(value)  
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()