print ("tool opened")
from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *


##-----------------------Notes-----------------------
'''
imageVarName.Image.thumbnail((256,256)) #resizes an image -> PIL function


#default paths: 
#Output Path ./Channel_Packing_Tool/default_output/FILENAME.png
#Input Path

'''
##-----------------------testing zone-----------------------

DEBUG = True
if DEBUG:
    pass

def DBGprint(text):
    if DEBUG:
        print(text)
#import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))

#RGBA = Image.open("X:\myDocuments\Coding\Git\Python\Channel_Packing_Tool\channels_tester.png")
#Rchan = Image.open("channels_tester.png")
#Gchan = Image.open("channels_tester.png")
#Bchan = Image.open("channels_tester.png")
#Achan = Image.open("channels_tester.png")

#Image._show(RGBA)

##-----------------------Open Images-----------------------


def openImg(text,fileName):
    print(text)
    extensions = [".png","jpg"] #add filetypes to filedialog: filetypes= need to figure this shit out
    defaultPath = str("./Channel_Packing_Tool/default_output/"+fileName)
    filePath = filedialog.askopenfilename(title=text,defaultextension=".png",initialfile=fileName)#opens a window to grab a file
    print ("so you have chosen:" ,filePath)
    file = PIL.Image.open(filePath)#opens the file from the path
    return file

    #(backup path("../default_assets/backup.png"))

#RGBA = openImg(text="test")
#PIL.Image.show(RGBA)

'''
def grabPath():
    filePath = filedialog.askopenfilename()
    print ("so you have chosen:" ,filePath)
    return filePath

RGBA = PIL.Image.open(grabPath())
PIL.Image._show(RGBA)
'''
#Rchan = openImg()
#Gchan = openImg()
#Bchan = openImg()
#Achan = openImg()

#print (RGBA)
#print ("hopefully that printed RGBA")

##-----------------------Seperate Channels-----------------------



##-----------------------Combine Channels-----------------------



##-----------------------Export Images-----------------------
'''
def savImg(export):
    filePath = filedialog.asksaveasfile()
    #filePath.write (export)
    PIL.Image.write(export)

savImg(RGBA)
'''

def savImg(export,text,defaultName):
    #exportQuality = 90
    #filePath = filedialog.asksaveasfile()
    defaultPath = str("./Channel_Packing_Tool/default_output/"+defaultName)
    filePath = filedialog.asksaveasfilename(defaultextension=".png",title=text,initialfile="Occlusion_Roughness_Metalic") or defaultPath
    
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


##-----------------------GUI-----------------------



##-----------------------Logic Maths etc-----------------------
running = True
while running:

    #Import RGBA channels

    Rchan = openImg(text="open Red channel texture, usually Ambient Occlusion",fileName="Occlusion.png")
    print ("here are the details for the Red channel:", Rchan)
    #PIL.Image._show(Rchan)#for debug opens the image in external
    
    #Gchan = openImg(text="open Green channel texture, usually Roughness",fileName="Roughness.png")
    #print ("here are the details for the Green channel:", Gchan)
    #PIL.Image._show(Gchan)

    #Bchan = openImg(text="open Blue channel texture, usually Metalic",fileName="Metalic.png")
    #print ("here are the details for the Blue channel:", Bchan)
    #PIL.Image._show(Bchan)

    #Achan = openImg(text="open Alpha channel texture, usually reserved for Mask",fileName="Alpha_Mask.png")
    #print ("here are the details for the Alpha channel:", Achan)
    #PIL.Image._show(Achan)
    

    savImg(export=Rchan,text="save output file as",defaultName="ORMA.png")#change Rchan to RGBA when files are packed

    #Export packed file
    #filePath = filedialog.asksaveasfile()
    #Rchan.save(fp=str(filePath), format="png")

    q = input ("press enter to run again or type quit to end")
    if q == ("quit"):
        running = False
    