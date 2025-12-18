import sys
import random #super very important for the code and not just fun easter eggs I wanna impliment when it's 4am and I havent slept in 48 hours

from PySide6.QtWidgets import (QApplication, QHBoxLayout,
                               QVBoxLayout, QPushButton,
                               QWidget, QCheckBox, QLabel,
                               QLineEdit, QSizePolicy, QToolTip)
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
# region Imp Exp


class Packer():
    useAlpha = False
    def alphaToggle():#might be more eligant way of doing this. worth asking if I have time
        if Packer.useAlpha:
            Packer.useAlpha = False
        else:
            Packer.useAlpha = True
        print("use Alpha set to",Packer.useAlpha)

    AutoPack = False
    def AutoPackToggle():#another toggle
        if Packer.AutoPack:
            Packer.AutoPack = False
        else:
            Packer.AutoPack = True
        print("autopack set to",Packer.AutoPack)

    class ImRW():
        #oppening and closing images

        def OpenImg(text,fileName):#📂
            DBGprint(text=text)
            extensions = [".png","jpg"] #add filetypes to filedialog: filetypes= need to figure this shit out
            defaultPath = str("./Channel_Packing_Tool/default_assets/"+Packer.DefNames["prefix"]+fileName)
            filePath = filedialog.askopenfilename(title=text,defaultextension=".png",initialfile=Packer.DefNames["prefix"]+fileName) or defaultPath #opens a window to grab a file. if window is closed sets to default path

            print ("so you have chosen:" ,filePath)
            file = PIL.Image.open(filePath)#opens the file from the path
            fileConv = Image.Image.convert(self=file, mode='RGBA')#converts to RGBA
            DBGprint(fileConv)
            return fileConv

            #(backup path("../default_assets/backup.png"))

        def SavImg(export,text,defaultName):#💾
            #exportQuality = 90
            #filePath = filedialog.asksaveasfile()
            defaultPath = str("./Channel_Packing_Tool/default_output/"+Packer.DefNames["prefix"]+defaultName)
            filePath = filedialog.asksaveasfilename(defaultextension=".png",title=text,initialfile=Packer.DefNames["prefix"]+defaultName) or defaultPath
            
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

            Packer.RChan = PIL.Image.open(str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["red"]))#opens the file from the path
            Packer.GChan = PIL.Image.open(str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["green"]))
            Packer.BChan = PIL.Image.open(str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["blue"]))
            if Packer.useAlpha:
                Packer.AChan = PIL.Image.open(str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["alpha"]))




        def SavImgBatch():#💾💾💾💾

            defPath = str("./Channel_Packing_Tool/default_output/")
            filePath = (filedialog.askdirectory(title="Select output folder for batch export")+"/") or defPath
            print ("file path for save is",filePath)
            #expImg = Packer.RChan
            Packer.RChan.save(fp=str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["red"]))
            Packer.GChan.save(fp=str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["green"]))
            Packer.BChan.save(fp=str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["blue"]))
            if Packer.useAlpha:#only export alpha if alpha toggle is true
                Packer.AChan.save(fp=str(filePath+Packer.DefNames["prefix"]+Packer.DefNames["alpha"]))


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
    # region Upd Vars

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
        "red" : "_Occlusion.png",
        "green" : "_Roughness.png",
        "blue" : "_Metallic.png",
        "alpha" : "_Alpha_Mask.png",
        "RGBA" : "_ORMA.png",
        "prefix" : "DefaultMaterial"
    }
    #all functional for now :)
    #thats probably a lie lol

    


    ##-----------------------Pack and Unpack Channels-----------------------
    # region Pk Unpk

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

# region controller
#   This might look stupid and unproffesional but it helps me find the controller section faster
#                   |
#         _--‾‾-----^----‾‾--_
#        / /‾‾\ <> (X) <>   Y \
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
            if Packer.AutoPack:
                Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan = Packer.ImPack.UnpackRGBA(Packer.RGBA)
        else:
            if name == "red":
                Packer.RChan = chan
            elif name == "green":
                Packer.GChan = chan
            elif name == "blue":
                Packer.BChan = chan
            elif name == "alpha":
                Packer.AChan = chan
            
            if Packer.AutoPack:
                Packer.RGBA = Packer.ImPack.PackRGBA(Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan,"replace string with resolution when implimented")
        
        DBGprint("successfully imported texture")
        

    def BtnBatchExp():
        DBGprint("button batch export pressed")
        Packer.ImRW.SavImgBatch()

    def BtnBatchImp():
        DBGprint("button batch import pressed")
        Packer.ImRW.OpenImgBatch()

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

    def setName(unused,chanName,text="test"):
        #bit hacky but need an unused variable at the start or the partial connect spits too many values into the first slot
        DBGprint("Update Text Box")
        DBGprint(text)
        DBGprint(chanName)
        Packer.DefNames[chanName] = text
    
    



#-----------------GUI-----------------
# region ↓ GUI ↓
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
        SplashText = ["Some sketchy software I found online",
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
                     "𝕯𝖎𝖊 𝖒𝖔𝖓𝖘𝖙𝖊𝖗. 𝖄𝖔𝖚 𝖉𝖔𝖓'𝖙 𝖇𝖊𝖑𝖔𝖓𝖌 𝖎𝖓 𝖙𝖍𝖎𝖘 𝖜𝖔𝖗𝖑𝖉.",
                     "𝕴𝖙 𝖜𝖆𝖘 𝖓𝖔𝖙 𝖇𝖞 𝖒𝖞 𝖍𝖆𝖓𝖉 𝕴 𝖜𝖆𝖘 𝖔𝖓𝖈𝖊 𝖆𝖌𝖆𝖎𝖓 𝖌𝖎𝖛𝖊𝖓 𝖋𝖑𝖊𝖘𝖍. 𝕴 𝖜𝖆𝖘 𝖇𝖗𝖔𝖚𝖌𝖍𝖙 𝖍𝖊𝖗𝖊 𝖇𝖞 𝖍𝖚𝖒𝖆𝖓𝖘 𝖜𝖍𝖔 𝖜𝖎𝖘𝖍 𝖙𝖔 𝖕𝖆𝖞 𝖒𝖊 𝖙𝖗𝖎𝖇𝖚𝖙𝖊",
                     "𝕿𝖗𝖎𝖇𝖚𝖙𝖊? 𝖄𝖔𝖚 𝖘𝖙𝖊𝖆𝖑 𝖒𝖊𝖓𝖘 𝖘𝖔𝖚𝖑𝖘 𝖆𝖓𝖉 𝖒𝖆𝖐𝖊 𝖙𝖍𝖊𝖒 𝖞𝖔𝖚𝖗 𝖘𝖑𝖆𝖛𝖊𝖘",
                     "𝕻𝖊𝖗𝖍𝖆𝖕𝖘 𝖙𝖍𝖊 𝖘𝖆𝖒𝖊 𝖈𝖆𝖓 𝖇𝖊 𝖘𝖆𝖎𝖉 𝖔𝖋 𝖆𝖑𝖑 𝖗𝖊𝖑𝖎𝖌𝖎𝖔𝖓𝖘?",
                     "𝖄𝖔𝖚𝖗 𝖜𝖔𝖗𝖉𝖘 𝖆𝖗𝖊 𝖆𝖘 𝖊𝖒𝖕𝖙𝖞 𝖆𝖘 𝖞𝖔𝖚𝖗 𝖘𝖔𝖚𝖑. 𝕸𝖆𝖓𝖐𝖎𝖓𝖉 𝖎𝖑𝖑 𝖓𝖊𝖊𝖉𝖘 𝖆 𝖘𝖆𝖛𝖎𝖔𝖚𝖗 𝖘𝖚𝖈𝖍 𝖆𝖘 𝖞𝖔𝖚",
                     "𝖂𝖍𝖆𝖙 𝖎𝖘 𝖆 𝖒𝖆𝖓? 𝕬 𝖒𝖎𝖘𝖊𝖗𝖆𝖇𝖑𝖊 𝖑𝖎𝖙𝖙𝖑𝖊 𝖕𝖎𝖑𝖊 𝖔𝖋 𝖘𝖊𝖈𝖗𝖊𝖙𝖘! 𝕭𝖚𝖙 𝖊𝖓𝖔𝖚𝖌𝖍 𝖙𝖆𝖑𝖐... 𝖍𝖆𝖛𝖊 𝖆𝖙 𝖞𝖔𝖚!",
                     "I like trains",
                     "𝕭𝖊𝖜𝖆𝖗𝖊; 𝖋𝖔𝖗 𝕴 𝖆𝖒 𝖋𝖊𝖆𝖗𝖑𝖊𝖘𝖘, 𝖆𝖓𝖉 𝖙𝖍𝖊𝖗𝖊𝖋𝖔𝖗𝖊 𝖕𝖔𝖜𝖊𝖗𝖋𝖚𝖑.",
                     "Who shot Mr Burns?",
                     "free the nipple!!!",
                     "Nuclear Ghandi did nothing wrong",
                     "The Simpsons predicted this software",
                     "Did you ever hear the tradgedy of Darth Plagueis the Wise?",
                     "Pack it up, pack it in, let me begin. I came to win, battle me, that's a sin",
                     "No AI was used in the creation of this software cos I have standards",
                     "No animals were harmed in the creation of this software",
                     "I hate London",
                     "Hello cruel world",
                     "I've come here to chew ass and kick bubblegum, and I'm all out of ass",
                     "There is no Heaven without Hell",
                     "Your mother was a hamster",
                     "we are no longer the knights that say ni",
                     "It can't see you if you stay perfectly still",
                     "Hello there",
                     "The fish is thinking",
                     "Jeveesus Lubs yoo... Someone has to to do it I guess",
                     "Marco                                                                                                                          Polo",
                     "Camden punks are posers",
                     "You have a face como un burro",
                     "Bring back mp3 players",
                     "Boycott RAM. You never needed it anyway",
                     "( ͡° ͜ʖ ͡°)",
                     "( ͡° ͜ʖ ͡°)╭∩╮",
                     "¯\_(ツ)_/¯",
                     "( ཀ ʖ̯ ཀ)",
                     "(｢•-•)｢ YEET"]
        
        title = ("Spider's Channel Packing Tool - "+random.choice(SplashText))

        self.setWindowTitle(title)

        #sets the icon to premade icon file
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Channel_Packing_Tool/GUI/icon.png"))
        self.setWindowIcon(icon)

        #dark mode stuff:
        self.setStyleSheet("QToolBar { background: #2a2841; } QWidget {background-color: #222034; color:darkgray; border: none} QLineEdit {background-color: #373165; color yellow; border: 3px solid #373165} QPushButton {background-color: #2a2841; color yellow; border: 3px solid #373165} QPushButton::pressed {background-color: #373165; color yellow; border: 3px solid #373165}")
        #self.setStyleSheet("QToolBar { background: #2a2841; } QWidget {background-color: #222034; color:yellow; border: 3px solid yellow} QPushButton {background-color: #2a2841; color yellow; border: 3px solid #373165} QPushButton::pressed {background-color: #373165; color yellow; border: 3px solid #373165}")
        #Debug disable later ^
        
        # region Layout
        #-----------------Layout-----------------

        seperateChans = QVBoxLayout()
        packedChans = QVBoxLayout()#contains Packed RGBA
        seperateChans1 = QVBoxLayout()#contains 2 channels - Red Green
        seperateChans2 = QVBoxLayout()#contains 2 channels - Blue Alpha

        class AspectRatioLabel(QLabel):#makes a copy of the qlabel class with height for width enabled
            #super jittery. Ask Omar if there's a cleaner way of doing this
            #tried paint stuff without any luck
            def __init__(self, aspectRatio=1.0):#needs to be a float so you can do .5 for half width etc
                super().__init__()
                self.aspectRatio = aspectRatio
                DBGprint(self.aspectRatio)
            
            def hasHeightForWidth(self):
                #probably not the cleanest way of doing this but tried litterally every other way I could think of
                return True
            
            def heightForWidth(self, width):
                #multiplies height by aspect ratio. Maybe in future make input for resizing texture?
                return int(width * self.aspectRatio)


        
        Rlab = AspectRatioLabel("red img")
        Glab = AspectRatioLabel("green img")
        Blab = AspectRatioLabel("blue img")
        Alab = AspectRatioLabel("Alpha img")

        RGBAlab = AspectRatioLabel("packed image")
        def MakeLabel(ChanNum):
            Packer.PILtoQtUpdate()
            #widg = QWidget()
            #widg.setSizePolicy()
            label=AspectRatioLabel(aspectRatio = 1.0)
            imgUI = QtGui.QPixmap(Packer.QtChans[ChanNum])
            imgUI.scaled(200,200,
                         aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                         mode=QtCore.Qt.TransformationMode.FastTransformation)
            
            label.setPixmap(imgUI)
            label.setScaledContents(True)
            

            #label.setUpdatesEnabled#dunno what this is but could be useful
            #label.setSizePolicy(QSizePolicy.setWidthForHeight)
            #label.setBaseSize(QtGui.Qt.SizeMode.RelativeSize)
            label.setMinimumSize(100,100)
            label.setBaseSize(20,20)
            label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,QSizePolicy.Policy.MinimumExpanding)
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

            #colour stuff
            colours = ["red","green","blue","white","black"]
            #label.setStyleSheet("background-color: black; border: 10px inset"+colours[ChanNum])
            label.setStyleSheet("QWidget {background-color: #222034; color:"+colours[ChanNum]+"; border: 3px solid "+colours[ChanNum]+"}")

            return label
        
        Rlab = MakeLabel(0)
        Glab = MakeLabel(1)
        Blab = MakeLabel(2)
        Alab = MakeLabel(3)
        RGBAlab = MakeLabel(4)
        
        


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
            imp.setToolTip("Imports image to the "+name+" texture slot")
            #-------🎮
            imp.clicked.connect(partial(Controller.BtnImport,name=name,filename=filename))
            imp.clicked.connect(partial(UpdateLabels))
            #connect to button import on controller
            #imp.clicked.connect(partial(Packer.ImRW.OpenImg,text="open "+name+" channel texture, usually "+filename,fileName=filename+".png"))
            exp = QPushButton("💾 Export "+name+" texture")
            exp.setToolTip("exports image from the "+name+" texture slot")
            #-------🎮
            #exp.clicked.connect(partial(Packer.ImRW.SavImg,export=Img,text="save "+name+" channel texture, usually "+filename,defaultName=filename+".png"))
            exp.clicked.connect(partial(Controller.BtnExport,name=name,filename=filename))
            exp.clicked.connect(partial(UpdateLabels))

            channel.addWidget(imp,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            channel.addWidget(exp,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

            channel.addWidget(QLabel(" Default file suffix for "+name+": "),0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            txtBox = QLineEdit(filename)
            #-------🎮
            txtBox.textChanged.connect(partial(Controller.setName,text=txtBox.text,chanName=name))
            channel.addWidget(txtBox,1,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
            #channel.setAlignment(alignment= "")

            container = QWidget()

            container.setLayout(channel)
            

            return container#returns the created layout as a container
        
        # region Chans UI
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
        redOutline = QVBoxLayout()
        seperateChans1.addWidget(Rlab)
        seperateChans1.addWidget(redCont)

        seperateChans1.addWidget(Glab)
        seperateChans1.addWidget(greenCont)

        seperateChans2.addWidget(Blab)
        seperateChans2.addWidget(blueCont)

        seperateChans2.addWidget(Alab)
        seperateChans2.addWidget(alphaCont)

        
        batchImp = QPushButton("📁 Batch import channels")
        batchImp.setToolTip("Imports images from a folder based on default name extensions")
        #-------🎮 NEEDS ADDING TO CONROLLER
        batchImp.clicked.connect(partial(Packer.ImRW.OpenImgBatch))
        batchImp.clicked.connect(partial(UpdateLabels))
        seperateChans1.addWidget(batchImp)#.clicked.connect(button_click_test)#dont connect arguments NO BRACKETS

        batchExp = QPushButton("💾 Batch export channels")
        batchExp.setToolTip("Exports images to a folder based on default name extensions")
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
        # region Settings
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
        pack.setToolTip("Takes R G B A channels and merges them into a single texture")
        #-------🎮 NEEDS ADDING TO CONROLLER
        pack.clicked.connect(Controller.BtnPacking)
        pack.clicked.connect(partial(UpdateLabels))
        #pack.clicked.connect(partial(Packer.ImPack.PackRGBA,Packer.RChan,Packer.GChan,Packer.BChan,Packer.AChan,"replace with resolution when implimented"))#change to pack
        
        #---Unpack Button
        settings.addWidget(pack,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        unpack = QPushButton("Unpack Textures\n <-- ")
        unpack.setToolTip("Takes the packed texture and unpacks the channels so you can replace or export them individually")
        #unpack.clicked.connect(partial(Packer.ImPack.UnpackRGBA,Packer.RGBA))
        #-------🎮
        unpack.clicked.connect(Controller.BtnUnpacking)
        unpack.clicked.connect(partial(UpdateLabels))
        settings.addWidget(unpack,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)



        #Name Prefix
        settings.addWidget(QLabel(" Default file prefix: "),0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        txtBox = QLineEdit(Packer.DefNames["prefix"])
        #-------🎮
        txtBox.textChanged.connect(partial(Controller.setName,text=txtBox.text,chanName="prefix"))
        settings.addWidget(txtBox,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)



        #---Alpha Checkbox
        useAlphaCB = QCheckBox("Use Alpha")
        useAlphaCB.setToolTip("Enables Alpha channel for 4 channel packing")
        useAlphaCB.setChecked(Packer.useAlpha)
        #-------🎮 NEEDS ADDING TO CONROLLER
        useAlphaCB.clicked.connect(Packer.alphaToggle)
        settings.addWidget(useAlphaCB,0,alignment=QtCore.Qt.AlignmentFlag.AlignTop)


        #---Autopacker Checkbox
        AutoPackCB = QCheckBox("Auto Packer Toggle")
        AutoPackCB.setToolTip("Automatically packs and unpacks images on import")
        AutoPackCB.setChecked(Packer.AutoPack)
        #-------🎮 NEEDS ADDING TO CONROLLER
        AutoPackCB.clicked.connect(Packer.AutoPackToggle)
        settings.addWidget(AutoPackCB,1,alignment=QtCore.Qt.AlignmentFlag.AlignTop)

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
