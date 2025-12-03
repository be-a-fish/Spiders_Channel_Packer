print ("tool opened")
#from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plot
from tkinter import filedialog
from tkinter import *

##-----------------------testing zone-----------------------

#RGBA = Image.open("X:\myDocuments\Coding\Git\Python\Channel_Packing_Tool\channels_tester.png")
#Rchan = Image.open("channels_tester.png")
#Gchan = Image.open("channels_tester.png")
#Bchan = Image.open("channels_tester.png")
#Achan = Image.open("channels_tester.png")

#Image._show(RGBA)

##-----------------------Open Images-----------------------


def openImg(text):
    print(text)
    filePath = filedialog.askopenfilename()#opens a window to grab a file
    print ("so you have chosen:" ,filePath)
    file = PIL.Image.open(filePath)#opens the file from the path
    return file

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
##-----------------------GUI-----------------------



##-----------------------Logic Maths etc-----------------------
running = True
while running == True:
    Rchan = openImg("open Red channel texture, usually Occlusion")
    print ("here are the details for the Red channel:", Rchan)
    Gchan = openImg("open Green channel texture, usually Roughness")
    print ("here are the details for the Green channel:", Gchan)
    Bchan = openImg("open Blue channel texture, usually Metalic")
    print ("here are the details for the Blue channel:", Bchan)
    Achan = openImg("open Alpha channel texture, usually reserved for Mask")
    print ("here are the details for the Alpha channel:", Achan)

    input ("press enter to run again")