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

from tkinter import filedialog

##-----------------------testing zone-----------------------

DEBUG = True

def DBGprint(text):
    if DEBUG:
        print(text)








##-----------------------Open and Export Images-----------------------
#to do: 
# batch import
# batch export


class Packer():
    
    useAlpha = True
    def alphaToggle():#might be more eligant way of doing this. worth asking if I have time
        if Packer.useAlpha:
            Packer.useAlpha = False
        else:
            Packer.useAlpha = True
        print("use Alpha set to",Packer.useAlpha)

    class ImRW():
        #oppening and closing images

        def OpenImg(text,fileName):
            DBGprint(text=text)
            extensions = [".png","jpg"] #add filetypes to filedialog: filetypes= need to figure this shit out
            defaultPath = str("./Channel_Packing_Tool/default_assets/"+fileName)
            filePath = filedialog.askopenfilename(title=text,defaultextension=".png",initialfile=fileName) or defaultPath #opens a window to grab a file. if window is closed sets to default path

            print ("so you have chosen:" ,filePath)
            file = PIL.Image.open(filePath)#opens the file from the path
            fileConv = Image.Image.convert(self=file, mode='RGBA')#converts to RGBA
            DBGprint(fileConv)
            return fileConv

            #(backup path("../default_assets/backup.png"))

        def SavImg(export,text,defaultName):
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
        


        #opens file without a file dialogue
        #use in batch open
        def DefLoad(fileName):
            defaultPath = str("./Channel_Packing_Tool/default_assets/"+fileName)
            file = PIL.Image.open(defaultPath)#opens the file from the path
            return file
        

        def OpenImgBatch():
            print("This functionality hasn't been made yet")

        def SavImgBatch():
            print("This functionality hasn't been made yet")
        
        
    ##-----------------------Load Defaults-----------------------

    RGBA = ImRW.DefLoad(fileName="ORMA.png")

    RChan, GChan, BChan, AChan = Image.Image.split(RGBA)#need to define before function so can't use unpacker

    #all functional for now :)
    #thats probably a lie lol


    ##-----------------------Pack and Unpack Channels-----------------------

    class ImPack():
        #image packing class

            
        def PackRGBA(red,green,blue,alpha,resolution):

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

            
            #PIL.Image.Image.show(RGBA)
            if Packer.useAlpha:
                RGBA = Image.merge('RGBA', (redLin,greenLin,blueLin,alphaLin))
                DBGprint("using alpha channel")
            else:
                RGBA = Image.merge('RGB', (redLin,greenLin,blueLin))
                RGBA = Image.Image.convert(self=RGBA, mode='RGBA')#converts to RGBA with blank alpha channel to avoid issues
                DBGprint("not using alpha but in RGBA mode to avoid errors")
            
            DBGprint(RGBA)
            DBGprint(resolution)
            #Packer.RGBA = RGBA
            return RGBA

        def UnpackRGBA(RGBA):
            DBGprint("attempting to unpack RGBA")
            
            #Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan = Image.Image.split(RGBA)
            #wanted to use Packer Variables rather than return value because button inputs dont support return values
            #unnessisary due to controller class
            
            red,green,blue,alpha = Image.Image.split(RGBA)
            
            RGBAList = [red,green,blue,alpha]
            return RGBAList
            
    


#format examples:
#Packer.ImPack.PackRGBA(red,green,blue,alpha,resolution)
#Packer.ImRW.OpenImg(text,fileName)

#for buttons:
#Button_Name.clicked.connect(partial(Packer.ImPack.UnpackRGBA,RGBA))

#-----------------Controller-----------------
#nessiccary to return values from functions. Also makes things more organised and readable
#also allows multiple functions to activate when button pressed

class Controller():

    #----Buttons:

    def BtnExport(Img,name,filename):
        DBGprint("button export pressed")
        
        #identify channel by name
        if name == "packed":
            Img = Packer.RGBA
        elif name == "red":
            Img = Packer.RChan
        elif name == "green":
            Img = Packer.GChan
        elif name == "blue":
            Img = Packer.BChan
        elif name == "alpha":
            Img = Packer.AChan
        else:
            print(name," isn't a valid name")

        Packer.ImRW.SavImg(export=Img,text="save "+name+" channel texture, usually "+filename,defaultName=filename+".png")

    def BtnImport(name, filename):
        DBGprint("button import pressed")
        chan = Packer.ImRW.OpenImg(text="open "+name+" texture, usually "+filename,fileName=filename+".png")
        
        #identify channel by name
        if name == "packed":
            Packer.RGBA = chan
        elif name == "red":
            Packer.RChan = chan
        elif name == "green":
            Packer.GChan = chan
        elif name == "blue":
            Packer.BChan = chan
        elif name == "alpha":
            Packer.AChan = chan
        else:
            print(name," isn't a valid name")
        
        DBGprint("successfully imported texture")
        

    def BtnBatchExp():
        DBGprint("button batch export pressed")

    def BtnBatchImp():
        DBGprint("button batch import pressed")

    def BtnPacking():
        DBGprint("button pack pressed")

    def BtnUnpacking():
        DBGprint("button unpack pressed")
        Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan = Packer.ImPack.UnpackRGBA(Packer.RGBA)
        #also add update GUI function when implimented

    def BtnDBG():
        DBGprint("OK what's broken now?")
        print("Rchan details: ",Packer.RChan)
        print("Gchan details: ",Packer.GChan)
        print("Bchan details: ",Packer.BChan)
        print("Achan details: ",Packer.AChan)
        print("RGBA details: ",Packer.RGBA)


    #----Tickboxes

    def TckBoxToBool():
        DBGprint("Toggling Tick Box")

    #----Textboxes

    def TxtBoxToVar():
        DBGprint("Update Text Box")

    







#-----------------GUI-----------------

class Window(QWidget):
    def __init__(self):
        super().__init__()


        #-----------------Theme and Titlebar-----------------

        #randomly picks a title for the window from the list
        titleList = ["Spider's Channel Packing Tool",
                     "Some sketchy software I found online",
                     "Totally not a virus.exe",
                     "At least this isn't Adobe",
                     "Über Hacker Tool",
                     "Cos I can't be asked to pirate photoshop",
                     "ya like jazz?",
                     "Nerds of the world Unite, we have nothing to loose but our dice 🎲",
                     "☭Eat the richⒶ... or like, maybe a sandwitch if you're feeling lazy",
                     "5318008",
                     "but can it run DOOM?",
                     "this is what programmers do when they haven't had enough sleep",
                     "AI can eat a bag of CONTENT NOT AVAILABLE WITHOUT AGE VERIFICATION",
                     "And my parents still aren't proud of me"]
        title = random.choice(titleList)

        self.setWindowTitle(title)

        #sets the icon to premade icon file
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Channel_Packing_Tool/GUI/icon.png"))
        self.setWindowIcon(icon)

        #dark mode stuff:
        self.setStyleSheet("QToolBar { background: #2a2841; } QWidget {background-color: #222034; color:darkgray; border: none} QLineEdit {background-color: #373165; color yellow; border: 3px solid #373165} QPushButton {background-color: #2a2841; color yellow; border: 3px solid #373165} QPushButton::pressed {background-color: #373165; color yellow; border: 3px solid #373165}")
        #self.setStyleSheet("QToolBar { background: #2a2841; } QWidget {background-color: #222034; color:yellow; border: 3px solid yellow} QPushButton {background-color: #2a2841; color yellow; border: 3px solid #373165} QPushButton::pressed {background-color: #373165; color yellow; border: 3px solid #373165}")
        #Debug disable later ^
        

        #-----------------Layout-----------------

        seperateChans = QVBoxLayout()
        packedChans = QVBoxLayout()#contains Packed RGBA
        seperateChans1 = QVBoxLayout()#contains 2 channels - Red Green
        seperateChans2 = QVBoxLayout()#contains 2 channels - Blue Alpha

        #makes the RGBA channels as boxes
        def MakeChannel(name,imgPath,filename,Img):
            channel = QVBoxLayout()

            #---------Image Label-----------
            #to do: maintain aspect ratio
            label = QLabel()
            imgGUI = QtGui.QPixmap(imgPath)
            imgGUI.scaled(100,100,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            
            
            label.setPixmap(imgGUI)
            label.setScaledContents(200)
            #label.setMaximumSize(500,500)
            label.setMinimumSize(100,100)
            label.setBaseSize(200,200)
            channel.addWidget(label,0)
            

            imp = QPushButton("📁 import "+name+" texture")
            #-------🎮
            imp.clicked.connect(partial(Controller.BtnImport,name=name,filename=filename))
            #connect to button import on controller
            #imp.clicked.connect(partial(Packer.ImRW.OpenImg,text="open "+name+" channel texture, usually "+filename,fileName=filename+".png"))
            exp = QPushButton("💾 export "+name+" texture")
            #-------🎮
            #exp.clicked.connect(partial(Packer.ImRW.SavImg,export=Img,text="save "+name+" channel texture, usually "+filename,defaultName=filename+".png"))
            exp.clicked.connect(partial(Controller.BtnExport,Img=Img,name=name,filename=filename))

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
        redCont = MakeChannel(name="red", imgPath="./Channel_Packing_Tool/default_assets/Occlusion.png", filename="Occlusion",Img=Packer.RChan)
        greenCont = MakeChannel(name="green", imgPath="./Channel_Packing_Tool/default_assets/Roughness.png", filename="Roughness",Img=Packer.GChan)
        blueCont = MakeChannel(name="blue", imgPath="./Channel_Packing_Tool/default_assets/Metalic.png", filename="Metalic",Img=Packer.BChan)
        alphaCont = MakeChannel(name="alpha", imgPath="./Channel_Packing_Tool/default_assets/Alpha_Mask.png", filename="Alpha_Mask",Img=Packer.AChan)

        #Add containers to Vertical layout
        seperateChans1.addWidget(redCont)
        seperateChans1.addWidget(greenCont)
        seperateChans2.addWidget(blueCont)
        seperateChans2.addWidget(alphaCont)

        
        batchImp = QPushButton("📁 batch import channels")
        #-------🎮 NEEDS ADDING TO CONROLLER
        batchImp.clicked.connect(partial(Packer.ImRW.OpenImgBatch))
        seperateChans1.addWidget(batchImp)#.clicked.connect(button_click_test)#dont connect arguments NO BRACKETS

        batchExp = QPushButton("💾 batch export channels")
        #-------🎮 NEEDS ADDING TO CONROLLER
        batchExp.clicked.connect(partial(Packer.ImRW.SavImgBatch))
        seperateChans2.addWidget(batchExp)

        #---------------------^-Seperate Channels-^------------------------

        #----------------------v-PACKED Channels-v-------------------------

        #RGBA as containers
        RGBACont = MakeChannel(name="packed", imgPath="./Channel_Packing_Tool/default_assets/ORMA.png", filename="ORMA",Img=Packer.RGBA)

        #Add containers to Vertical layout
        packedChans.addWidget(RGBACont)

        #----------------------^-PACKED Channels-^-------------------------

        #-------------------------v-Settings-v----------------------------

        settings = QVBoxLayout()
        settings.addWidget(QLabel("⚙ Settings: "),1,alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
        
        #---Pack Button
        pack = QPushButton("Pack Textures\n --> ")
        #-------🎮 NEEDS ADDING TO CONROLLER
        pack.clicked.connect(partial(Packer.ImPack.PackRGBA,Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan,"replace with resolution when implimented"))#change to pack
        
        #---Unpack Button
        settings.addWidget(pack,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        unpack = QPushButton("Unpack Textures\n <-- ")
        #unpack.clicked.connect(partial(Packer.ImPack.UnpackRGBA,Packer.RGBA))
        unpack.clicked.connect(Controller.BtnUnpacking)
        settings.addWidget(unpack,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        #---Alpha Checkbox
        useAlphaCB = QCheckBox("Use Alpha")
        useAlphaCB.setChecked(Packer.useAlpha)
        #-------🎮 NEEDS ADDING TO CONROLLER
        useAlphaCB.clicked.connect(Packer.alphaToggle)
        settings.addWidget(useAlphaCB,1,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        if DEBUG:
            DBGButton = QPushButton("DEBUG BUTTON\nASSIGN ME STUFF TO TEST")
            DBGButton.clicked.connect(Controller.BtnDBG)
            settings.addWidget(DBGButton,1,alignment=QtCore.Qt.AlignmentFlag.AlignBottom)


        #-------------------------^-Settings-^----------------------------

        #---collums
        col0 =QWidget()
        col0.setLayout(seperateChans1)#seperate channels

        col1 = QWidget()
        col1.setLayout(seperateChans2)#seperate channels

        col2 = QWidget()
        col2.setLayout(settings)#settings collum

        col3 = QWidget()
        col3.setLayout(packedChans)#packed texture

        #---master layout
        Mlayout = QHBoxLayout()
        Mlayout.addWidget(col0,1)
        Mlayout.addWidget(col1,1)#numbers represent importance for scaling
        Mlayout.addWidget(col2,0)
        Mlayout.addWidget(col3,2)#scale this guy most important
        #Mlayout.maximumSize()
        

        self.setLayout(Mlayout)
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
