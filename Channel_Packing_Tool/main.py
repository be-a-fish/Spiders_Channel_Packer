import sys
import random #super very important for the code and not just fun easter eggs I wanna impliment when it's 4am and I havent slept in 48 hours

from PySide6.QtWidgets import (QApplication, QHBoxLayout,
                               QVBoxLayout, QPushButton,
                               QWidget, QCheckBox, QLabel,
                               QLineEdit)
from PySide6 import QtGui, QtCore

from functools import partial#for sending variables through button inputs

from PIL import Image
import PIL
from PIL import ImageQt

from tkinter import filedialog#file dialogue boxes. Literally don't use tkinter for anything else

##-----------------------testing zone-----------------------

DEBUG = False

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

        def OpenImg(text,fileName):#📂
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

        def SavImg(export,text,defaultName):#💾
            #exportQuality = 90
            #filePath = filedialog.asksaveasfile()
            defaultPath = str("./Channel_Packing_Tool/default_output/"+defaultName)
            filePath = filedialog.asksaveasfilename(defaultextension=".png",title=text,initialfile=defaultName) or defaultPath
            
            #filePath = str("./default_output/",defaultName)
            #print("didn't manage to get that dictionary. defaulting to ",filePath)
            print ("file path for save is",filePath)
            if Packer.useAlpha:
                print("exporting with alpha")
            else:
                export = Image.Image.convert(self=export, mode='RGB')
                print("exporting without alpha")
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
        def DefLoad(fileName):#📁Def
            defaultPath = str("./Channel_Packing_Tool/default_assets/"+fileName)
            file = PIL.Image.open(defaultPath)#opens the file from the path
            return file
        

        def OpenImgBatch():#📁📁📁📁
            print("This functionality hasn't been made yet")

            defPath = str("./Channel_Packing_Tool/default_output/")
            filePath = (filedialog.askdirectory(title="Select output folder for batch export")+"/") or defPath
            print ("file path for import is",filePath)

            Packer.RChan = PIL.Image.open(str(filePath+Packer.DefNames["red"]))#opens the file from the path
            Packer.GChan = PIL.Image.open(str(filePath+Packer.DefNames["green"]))
            Packer.BChan = PIL.Image.open(str(filePath+Packer.DefNames["blue"]))
            if Packer.useAlpha:
                Packer.AChan = PIL.Image.open(str(filePath+Packer.DefNames["alpha"]))




        def SavImgBatch():#💾💾💾💾

            defPath = str("./Channel_Packing_Tool/default_output/")
            filePath = (filedialog.askdirectory(title="Select output folder for batch export")+"/") or defPath
            print ("file path for save is",filePath)
            #expImg = Packer.RChan
            Packer.RChan.save(fp=str(filePath+Packer.DefNames["red"]))
            Packer.GChan.save(fp=str(filePath+Packer.DefNames["green"]))
            Packer.BChan.save(fp=str(filePath+Packer.DefNames["blue"]))
            if Packer.useAlpha:#only export alpha if alpha toggle is true
                Packer.AChan.save(fp=str(filePath+Packer.DefNames["alpha"]))


            '''
            expList = [Packer.RChan, Packer.GChan, Packer.BChan]
            expListNames = [Packer.DefNames["red"],Packer.DefNames["green"],Packer.DefNames["blue"],Packer.DefNames["alpha"],]
            if Packer.useAlpha:
                expList.append(Packer.AChan)
            for i in expList:
                #expImg = expList[i]
                Path = str("./Channel_Packing_Tool/default_output/"+expListNames[i])
                print(Path)
                #print(expImg)
            '''
                

        
        
    ##-----------------------Packer Variables Load Defaults and update Vars-----------------------
    
    #Pillow RGBA
    RGBA = ImRW.DefLoad(fileName="ORMA.png")
    #Pillow channels
    RChan, GChan, BChan, AChan = Image.Image.split(RGBA)#need to define before function so can't use unpacker


    #makes a list from PIL channels in Qt image format
    QtChans = []#needs to be empty at first because PILtoQtUpdate function gives its values
    #Order: RChan,GChan,BChan,AChan,RGBA

    def PILtoQtUpdate():
        Packer.QtChans = []
        for i in [Packer.RChan, Packer.GChan, Packer.BChan, Packer.AChan, Packer.RGBA]:
            QtChan = ImageQt.ImageQt(i)#converts into Qt image format
            print(QtChan)
            Packer.QtChans.append(QtChan)
            #Order: RChan,GChan,BChan,AChan,RGBA
    
    #PILtoQtUpdate()#calls the function once to set defaults

    '''
    for i in [RChan, GChan, BChan, AChan, RGBA]:
        QtChan = ImageQt.ImageQt(i)
        print(QtChan)
        QtChans.append(QtChan)
    '''

    DefNames = {
        "red" : "Occlusion.png",
        "green" : "Roughness.png",
        "blue" : "Metallic.png",
        "alpha" : "Alpha_Mask.png",
        "RGBA" : "ORMA.png"
    }
    #all functional for now :)
    #thats probably a lie lol

    


    ##-----------------------Pack and Unpack Channels-----------------------

    #    _______
    #   |       |                       _______________
    #   |   R   |___                   |               |
    #   |_______|   |      <------     |               |
    #       |   G   |___   ------>     |     RGBA      |
    #       |_______|   |              |               |
    #           |   B   |              |               |
    #           |_______|              |_______________|
    #

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
#but dont do this now cos I've added a controller class to clean things up

#-----------------Controller-----------------
#nessiccary to return values from functions. Also makes things more organised and readable
#also allows multiple functions to activate when button pressed
#just generally better than you in every consivable way

#   This might look stupid and unproffesional but it helps me find the controller section faster
#                   |
#         _--‾‾-----^----‾‾--_
#        / /‾‾\  _ (X) _    Y \
#      /   \__/|‾|        X   B \
#     /      [‾   ‾]  /‾‾\  A    \
#    /        ‾|_|‾   \__/        \
#   /      /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\      \
#   \_  _/                    \_  _/
#     ‾‾                        ‾‾


class Controller():

    #----Buttons:

    def BtnExport(name,filename):
        DBGprint("button export pressed")
        
        #identify channel by name
        if name == "packed":
            exp = Packer.RGBA
        elif name == "red":
            exp = Packer.RChan
        elif name == "green":
            exp = Packer.GChan
        elif name == "blue":
            exp = Packer.BChan
        elif name == "alpha":
            exp = Packer.AChan
        else:
            print(name," isn't a valid name")

        Packer.ImRW.SavImg(export=exp,text="save "+name+" channel texture, usually "+filename,defaultName=filename)

    def BtnImport(name, filename):
        DBGprint("button import pressed")
        chan = Packer.ImRW.OpenImg(text="open "+name+" texture, usually "+filename,fileName=filename)
        
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
        Packer.ImRW.SavImgBatch()

    def BtnBatchImp():
        DBGprint("button batch import pressed")

    def BtnPacking():
        DBGprint("button pack pressed")
        Packer.RGBA = Packer.ImPack.PackRGBA(Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan,"replace string with resolution when implimented")

    def BtnUnpacking():
        DBGprint("button unpack pressed")
        Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan = Packer.ImPack.UnpackRGBA(Packer.RGBA)
        #also add update GUI function when implimented

    def BtnDBG():
        DBGprint("OK what's broken now?\n ")
        print("Details on the colour channels")
        print("Rchan details: ",Packer.RChan)
        print("Gchan details: ",Packer.GChan)
        print("Bchan details: ",Packer.BChan)
        print("Achan details: ",Packer.AChan)
        print("RGBA details: ",Packer.RGBA)
        print(" \ndetails on the alpha toggle: ",Packer.useAlpha)
        print("default export names are: ",Packer.DefNames)
        Packer.PILtoQtUpdate()
        print("\nQt image format details:",Packer.QtChans)


    #----Tickboxes

    def TckBoxToBool():
        DBGprint("Toggling Tick Box")

    #----Textboxes

    def setName(text,chanName):
        DBGprint("Update Text Box")
        Packer.DefNames[chanName] = text
    
    



#-----------------GUI-----------------
# _________________________________________________
#| 🕷Spiders Channel packing tool            _[]X  |
#|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
#||‾‾‾‾‾|   |‾‾‾‾‾|             |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |
#||  R  |   |  B  |             |                | |
#||‾‾‾‾‾|   |‾‾‾‾‾|  _____      |                | |
#||‾‾‾‾‾|   |‾‾‾‾‾| | --> |     |      RGBA      | |
#| ‾‾‾‾‾     ‾‾‾‾‾   ‾‾‾‾‾      |                | |
#||‾‾‾‾‾|   |‾‾‾‾‾|  _____      |                | |
#||  G  |   |  A  | | <-- |     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |
#||‾‾‾‾‾|   |‾‾‾‾‾|  ‾‾‾‾‾      |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |
#||‾‾‾‾‾|   |‾‾‾‾‾|             |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |
#| ‾‾‾‾‾     ‾‾‾‾‾               ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  |
# ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾




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
                     "And my parents still aren't proud of me",
                     "Turns out she could say much worse than no",
                     "Did you know there are more planes in the sea than submarines in the sky",
                     "RGBTQ+ Rights",
                     "All I wanted was a Pepsi. Just one Pepsi. And she wouldn't give it to me. Just one Pepsi",
                     "This app is rated PG.13 so I get one use of the word fuck and I just wasted it",
                     "Who shot Mr Burns?",
                     "free the nipple!!!",
                     "Nuclear Ghandi did nothing wrong",
                     "The Simpsons predicted this software",
                     "Did you ever hear the tradgedy of Darth Plagueis the Wise?",
                     "Pack it up, pack it in, let me begin. I came to win, battle me, that's a sin",
                     "No AI was used in the creation of this software cos I have standards",
                     "No animals were harmed in the creation of this software",
                     "I hate London"]
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

        
        labels = [QLabel(),QLabel(),QLabel(),QLabel(),QLabel()]
        #           red     green    blue    alpha      RGBA
        
        Rlab = QLabel("red img")
        Glab = QLabel("green img")
        Blab = QLabel("blue img")
        Alab = QLabel("Alpha img")

        RGBAlab = QLabel("packed image")
        def MakeLabel(ChanNum):
            Packer.PILtoQtUpdate()

            label=QLabel()
            imgUI = QtGui.QPixmap(Packer.QtChans[ChanNum])
            imgUI.scaled(200,200,
                         aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                         mode=QtCore.Qt.TransformationMode.FastTransformation)
            
            label.setPixmap(imgUI)
            label.setScaledContents(True)
            label.setMinimumSize(100,100)
            label.setBaseSize(20,20)
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            return label
        
        Rlab = MakeLabel(0)
        Glab = MakeLabel(1)
        Blab = MakeLabel(2)
        Alab = MakeLabel(3)
        RGBAlab = MakeLabel(4)
        print("rlab is\n",Rlab)


        def UpdateLabels():
            Packer.PILtoQtUpdate()#recalculates the Qt images from the PIL images

            imgUI = QtGui.QPixmap(Packer.QtChans[0])
            Rlab.setPixmap(imgUI)
            imgUI = QtGui.QPixmap(Packer.QtChans[1])
            Glab.setPixmap(imgUI)
            imgUI = QtGui.QPixmap(Packer.QtChans[2])
            Blab.setPixmap(imgUI)
            imgUI = QtGui.QPixmap(Packer.QtChans[3])
            Alab.setPixmap(imgUI)

            imgUI = QtGui.QPixmap(Packer.QtChans[4])
            RGBAlab.setPixmap(imgUI)
        

        
        #makes the RGBA channels as boxes
        def MakeChannelButtons(name,filename):
            channel = QVBoxLayout()

            imp = QPushButton("📁 Import "+name+" texture")
            #-------🎮
            imp.clicked.connect(partial(Controller.BtnImport,name=name,filename=filename))
            imp.clicked.connect(partial(UpdateLabels))
            #connect to button import on controller
            #imp.clicked.connect(partial(Packer.ImRW.OpenImg,text="open "+name+" channel texture, usually "+filename,fileName=filename+".png"))
            exp = QPushButton("💾 Export "+name+" texture")
            #-------🎮
            #exp.clicked.connect(partial(Packer.ImRW.SavImg,export=Img,text="save "+name+" channel texture, usually "+filename,defaultName=filename+".png"))
            exp.clicked.connect(partial(Controller.BtnExport,name=name,filename=filename))
            exp.clicked.connect(partial(UpdateLabels))

            channel.addWidget(imp,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            channel.addWidget(exp,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

            channel.addWidget(QLabel(" Default file name:"),0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            txtBox = QLineEdit(filename)
            #-------🎮
            txtBox.textChanged.connect(partial(Controller.setName,chanName=name))
            channel.addWidget(txtBox,1,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            #channel.setAlignment(alignment= "")

            container = QWidget()

            container.setLayout(channel)
            

            return container#returns the created layout as a container
        

        #---------------------v-Seperate Channels-v------------------------
        #    _______
        #   |       |
        #   |   R   |___
        #   |_______|   |
        #       |   G   |___
        #       |_______|   |
        #           |   B   |
        #           |_______|
        #
        #RGBA as containers
        '''
        #------------Create and Update RGBA Image labels
        def UpdateGUI():
                Packer.PILtoQtUpdate()
                Rlab = LiveUI.MakeImgLabel(QtChanNum=0)
                Glab = LiveUI.MakeImgLabel(QtChanNum=1)
                Blab = LiveUI.MakeImgLabel(QtChanNum=2)
                Alab = LiveUI.MakeImgLabel(QtChanNum=3)

                RGBAlab = LiveUI.MakeImgLabel(QtChanNum=4)   
                labList = [Rlab,Glab,Blab,Alab,RGBAlab]
                return labList  
        
        Rlab,Glab,Blab,Alab,RGBAlab = UpdateGUI()
        '''


        Packer.PILtoQtUpdate()#updates the QtImage list just before creating the images
        #Rlab = MakeImgLabel(QtChan=Packer.QtChans[0])
        redCont = MakeChannelButtons(name="red", filename=Packer.DefNames["red"])
        #Glab = MakeImgLabel(QtChan=Packer.QtChans[1])
        greenCont = MakeChannelButtons(name="green", filename=Packer.DefNames["green"])
        #Blab = MakeImgLabel(QtChan=Packer.QtChans[2])
        blueCont = MakeChannelButtons(name="blue", filename=Packer.DefNames["blue"])
        #Alab = MakeImgLabel(QtChan=Packer.QtChans[3])
        alphaCont = MakeChannelButtons(name="alpha", filename=Packer.DefNames["alpha"])

        #Add containers to Vertical layout
        seperateChans1.addWidget(Rlab)
        seperateChans1.addWidget(redCont)

        seperateChans1.addWidget(Glab)
        seperateChans1.addWidget(greenCont)

        seperateChans2.addWidget(Blab)
        seperateChans2.addWidget(blueCont)

        seperateChans2.addWidget(Alab)
        seperateChans2.addWidget(alphaCont)

        
        batchImp = QPushButton("📁 Batch import channels")
        #-------🎮 NEEDS ADDING TO CONROLLER
        batchImp.clicked.connect(partial(Packer.ImRW.OpenImgBatch))
        batchImp.clicked.connect(partial(UpdateLabels))
        seperateChans1.addWidget(batchImp)#.clicked.connect(button_click_test)#dont connect arguments NO BRACKETS

        batchExp = QPushButton("💾 Batch export channels")
        #-------🎮 NEEDS ADDING TO CONROLLER
        batchExp.clicked.connect(partial(Packer.ImRW.SavImgBatch))
        seperateChans2.addWidget(batchExp)

        #---------------------^-Seperate Channels-^------------------------

        #----------------------v-PACKED Channels-v-------------------------

        #   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
        #   |                |
        #   |                |
        #   |      RGBA      |
        #   |                |
        #   |                |
        #   |________________|

        #RGBA as containers
        #RGBAlab = MakeImgLabel(QtChan=Packer.QtChans[4])
        RGBACont = MakeChannelButtons(name="packed", filename=Packer.DefNames["RGBA"])

        #Add containers to Vertical layout
        packedChans.addWidget(RGBAlab)
        packedChans.addWidget(RGBACont)

        #----------------------^-PACKED Channels-^-------------------------

        #-------------------------v-Settings-v----------------------------
        #
        #                ####        
        #          ###  ######  ###   
        #         ##################  
        #          #####      #####   
        #        #####          ##### 
        #       ######          ######
        #        #####         ##### 
        #          #####      ##### 
        #         ################## 
        #          ###  ######  ### 
        #                #### 

        settings = QVBoxLayout()
        settings.addWidget(QLabel("⚙ Settings: "),1,alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
        
        #---Pack Button
        pack = QPushButton("Pack Textures\n --> ")
        #-------🎮 NEEDS ADDING TO CONROLLER
        pack.clicked.connect(Controller.BtnPacking)
        pack.clicked.connect(partial(UpdateLabels))
        #pack.clicked.connect(partial(Packer.ImPack.PackRGBA,Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan,"replace with resolution when implimented"))#change to pack
        
        #---Unpack Button
        settings.addWidget(pack,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        unpack = QPushButton("Unpack Textures\n <-- ")
        #unpack.clicked.connect(partial(Packer.ImPack.UnpackRGBA,Packer.RGBA))
        #-------🎮
        unpack.clicked.connect(Controller.BtnUnpacking)
        unpack.clicked.connect(partial(UpdateLabels))
        settings.addWidget(unpack,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        #---Alpha Checkbox
        useAlphaCB = QCheckBox("Use Alpha")
        useAlphaCB.setChecked(Packer.useAlpha)
        #-------🎮 NEEDS ADDING TO CONROLLER
        useAlphaCB.clicked.connect(Packer.alphaToggle)
        settings.addWidget(useAlphaCB,1,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        #DEBUG STUFF
        
        
        if DEBUG:#adds a debug button if debug is enabled

            #DBGLabel = QLabel("Test Label")
            #settings.addWidget(DBGLabel,1,alignment=QtCore.Qt.AlignmentFlag.AlignBottom)

            
            '''
            DBGlabelImg = QLabel()
            imgGUI = QtGui.QPixmap(Packer.QtChans[4])
            imgGUI.scaled(100,100,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            DBGlabelImg.setPixmap(imgGUI)
            DBGlabelImg.setScaledContents(200)
            DBGlabelImg.setMinimumSize(100,100)
            DBGlabelImg.setBaseSize(20,20)

            settings.addWidget(DBGlabelImg)

            def UpdateGUI():
                Packer.PILtoQtUpdate()
                
                imgGUI = QtGui.QPixmap(Packer.QtChans[4])
                imgGUI.scaled(100,100,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                DBGlabelImg.setPixmap(imgGUI)
                DBGlabelImg.setScaledContents(200)
                DBGlabelImg.setMinimumSize(100,100)
                DBGlabelImg.setBaseSize(20,20)
                print("did it work?")
            '''

            DBGButton = QPushButton("DEBUG BUTTON\nASSIGN ME STUFF TO TEST")
            DBGButton.clicked.connect(Controller.BtnDBG)
            #DBGButton.clicked.connect(partial(DBGLabel.setText,"Updated Label"))
            #DBGButton.clicked.connect(partial(UpdateGUI))#need to find a way of returning the values
            DBGButton.clicked.connect(partial(UpdateLabels))
            settings.addWidget(DBGButton,1,alignment=QtCore.Qt.AlignmentFlag.AlignBottom)

            


        #-------------------------^-Settings-^----------------------------

        #---collums
        col0 = QWidget()
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
