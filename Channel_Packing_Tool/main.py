import sys
import random

from PySide6.QtWidgets import (QApplication, QHBoxLayout,
                               QVBoxLayout, QPushButton,
                               QWidget, QCheckBox, QLabel,
                               QLineEdit)
from PySide6 import QtGui, QtCore

from functools import partial

from PIL import Image
import PIL

import matplotlib.pyplot as plt
from tkinter import filedialog

##-----------------------testing zone-----------------------

DEBUG = True

def DBGprint(text):
    if DEBUG:
        print(text)

def button_click_test():
    print("stop clicking me >:(")

class Buttons():
    def PressImport(text):
        print("importing")
        print("your passed variable is",text)

    def PressExport(text):
        print("exporting")
        print("your passed variable is",text)
    
    def PressUnused(text):
        print("this feature isn't implimented yet\nsorry")
        print("your passed variable is",text)



















##-----------------------Open and Export Images-----------------------
#to do: 
# batch import
# batch export
# make this all a class

def openImg(text,fileName):
    DBGprint(text=text)
    extensions = [".png","jpg"] #add filetypes to filedialog: filetypes= need to figure this shit out
    defaultPath = str("./Channel_Packing_Tool/default_assets/"+fileName)
    filePath = filedialog.askopenfilename(title=text,defaultextension=".png",initialfile=fileName) or defaultPath #opens a window to grab a file. if window is closed sets to default path

    print ("so you have chosen:" ,filePath)
    file = PIL.Image.open(filePath)#opens the file from the path
    return file

    #(backup path("../default_assets/backup.png"))

def savImg(export,text,defaultName):
    #exportQuality = 90
    #filePath = filedialog.asksaveasfile()
    defaultPath = str("./Channel_Packing_Tool/default_output/"+defaultName)
    filePath = filedialog.asksaveasfilename(defaultextension=".png",title=text,initialfile=defaultName) or defaultPath
    
    #filePath = str("./default_output/",defaultName)
    #print("didn't manage to get that dictionary. defaulting to ",filePath)
    print ("file path for save is",filePath)
    try:
        export = export.save(fp=str(filePath))
    except ValueError as E:
        print("there was an error while attempting to export")
        print("the file path is ",filePath)
        print("the export details are ",export)
        DBGprint(text=str("EXPORT ERROR"+filePath+export))
        
    print ("attempted to save as: "+ str(filePath))
    #format    (fp=file path, format=png, parameters left unused) fp string: fp=str(filePath)
























##-----------------------Pack and Unpack Channels-----------------------


def packRGBA(red,green,blue,alpha,resolution):

    #---Make linear/grayscale images
    redLin = Image.Image.convert(self=red, mode='L') #makes image format liniar
    DBGprint(red)
    greenLin = Image.Image.convert(self=green, mode='L')
    DBGprint(green)
    blueLin = Image.Image.convert(self=blue, mode='L')
    DBGprint(blue)
    alphaLin = Image.Image.convert(self=alpha, mode='L')
    DBGprint(alpha)

    #Image.Image.show(redLin)
    #Image.Image.show(alpha)
    #---Combine into single image

    RGBA = Image.merge('RGBA', (redLin,greenLin,blueLin,alphaLin))
    #PIL.Image.Image.show(RGBA)
    DBGprint(RGBA)
    DBGprint(resolution)
    return RGBA

def unpackRGBA(RGBA):

    red,green,blue,alpha = Image.Image.split(RGBA)

    RGBAList = [red,green,blue,alpha]
    return RGBAList


















#-----------------GUI-----------------

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spider's Channel Packing Tool")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Channel_Packing_Tool/GUI/icon.png"))
        self.setWindowIcon(icon)

        #dark mode stuff:
        self.setStyleSheet("QToolBar { background: #2a2841; } QWidget {background-color: #222034; color:darkgray; border: none} QLineEdit {background-color: #373165; color yellow; border: 3px solid #373165} QPushButton {background-color: #2a2841; color yellow; border: 3px solid #373165} QPushButton::pressed {background-color: #373165; color yellow; border: 3px solid #373165}")
        #self.setStyleSheet("QToolBar { background: #2a2841; } QWidget {background-color: #222034; color:yellow; border: 3px solid yellow} QPushButton {background-color: #2a2841; color yellow; border: 3px solid #373165} QPushButton::pressed {background-color: #373165; color yellow; border: 3px solid #373165}")
        #Debug disable later ^
        

        #-----------------Final Layout-----------------

        seperateChans = QVBoxLayout()
        packedChans = QVBoxLayout()
        seperateChans1 = QVBoxLayout()
        seperateChans2 = QVBoxLayout()

        #makes the RGBA channels as boxes
        def MakeChannel(name,imgPath,filename):
            channel = QVBoxLayout()

            #---------Image Label-----------
            label = QLabel()
            imgGUI = QtGui.QPixmap(imgPath)#------------NEEDS FIGURING OUT!!!!
            #imgGUI.scaledToHeight(100)
            imgGUI.scaled(100,100,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            #imgGUI.scaled(100,100,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            
            
            #label.setGeometry(1, 1, 2, 2)
            label.setPixmap(imgGUI)
            label.setScaledContents(200)
            #label.setMaximumSize(500,500)
            label.setMinimumSize(100,100)
            label.setBaseSize(200,200)
            #label.resize(10, 10)
            channel.addWidget(label,0)
            #channel.addWidget(QPushButton("REPLACE ME WITH THE IMAGE\nREPLACE ME WITH THE IMAGE\nREPLACE ME WITH THE IMAGE"),1,alignment=QtCore.Qt.AlignmentFlag.AlignBottom)#need to figure out adding images above these

            imp = QPushButton("📁 import "+name+" texture")
            imp.clicked.connect(partial(Buttons.PressImport,"arg"))
            exp = QPushButton("💾 export "+name+" texture")
            channel.addWidget(imp,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            channel.addWidget(exp,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

            channel.addWidget(QLabel(" default file name:"),0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            channel.addWidget(QLineEdit(filename+".png"),1,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            #channel.setAlignment(alignment= "")

            container = QWidget()

            container.setLayout(channel)
            

            return container#returns the created layout as a container
        
        #---------------------v-Seperate Channels-v------------------------

        #RGBA as containers
        red = MakeChannel(name="red", imgPath="./Channel_Packing_Tool/default_assets/Occlusion.png", filename="Occlusion")
        green = MakeChannel(name="green", imgPath="./Channel_Packing_Tool/default_assets/Roughness.png", filename="Roughness")
        blue = MakeChannel(name="blue", imgPath="./Channel_Packing_Tool/default_assets/Metalic.png", filename="Metalic")
        alpha = MakeChannel(name="alpha", imgPath="./Channel_Packing_Tool/default_assets/Alpha_Mask.png", filename="Alpha_Mask")

        #Add containers to Vertical layout
        seperateChans1.addWidget(red)
        seperateChans1.addWidget(green)
        seperateChans2.addWidget(blue)
        seperateChans2.addWidget(alpha)

        

        seperateChans1.addWidget(QPushButton("📁 batch import channels"))#.clicked.connect(button_click_test)#dont connect arguments NO BRACKETS
        #seperateChans1.addWidget(QPushButton("batch import channels"))#.clicked.connect(button_click()))
        seperateChans2.addWidget(QPushButton("💾 batch export channels"))

        #---------------------^-Seperate Channels-^------------------------

        #----------------------v-PACKED Channels-v-------------------------

        #RGBA as containers
        RGBA = MakeChannel(name="packed", imgPath="./Channel_Packing_Tool/default_assets/ORMA.png", filename="ORMA")

        #Add containers to Vertical layout
        packedChans.addWidget(RGBA)

        #----------------------^-PACKED Channels-^-------------------------

        #-------------------------v-Settings-v----------------------------

        settings = QVBoxLayout()
        settings.addWidget(QLabel("⚙ Settings: "),1,alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
        settings.addWidget(QPushButton("Pack Textures\n --> "),0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        settings.addWidget(QPushButton("Unpack Textures\n <-- "),0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        settings.addWidget(QCheckBox("Use Alpha"),1,alignment=QtCore.Qt.AlignmentFlag.AlignTop)


        #-------------------------^-Settings-^----------------------------

        #collums
        col0 =QWidget()
        col0.setLayout(seperateChans1)

        col1 = QWidget()
        col1.setLayout(seperateChans2)#seperate channels

        col2 = QWidget()
        col2.setLayout(settings)#settings collum

        col3 = QWidget()
        col3.setLayout(packedChans)#packed texture

        #master layout
        Mlayout = QHBoxLayout()
        Mlayout.addWidget(col0,1)
        Mlayout.addWidget(col1,1)#numbers represent importance for scaling
        Mlayout.addWidget(col2,0)
        Mlayout.addWidget(col3,2)
        #Mlayout.maximumSize()
        

        self.setLayout(Mlayout)
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
