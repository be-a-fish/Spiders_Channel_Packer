print ("tool opened")

from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
#from tkinter import * #breaks image from PIL, don't use unless essential
#import tkinter as tk

print("librarys loaded")

##-----------------------Notes-----------------------
'''
imageVarName.Image.thumbnail((256,256)) #resizes an image -> PIL function


#default paths: 
    #Output Path ./Channel_Packing_Tool/default_output/FILENAME.png
    #Input Path ./Channel_Packing_Tool/default_assets/FILENAME.png

#default asset names:
    Red=Occlusion.png
    Green=Roughness.png
    Blue=Metalic.png
    Alpha=Alpha_Mask.png

    Packed=ORMA

'''
##-----------------------testing zone-----------------------

DEBUG = True

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

#plt.gray()#grayscale
#Image.convert('RGBA')

##-----------------------Open and Export Images-----------------------
#to do: 
# batch import
# batch export

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


#RGBA = openImg(text="test")
#PIL.Image.Image.show(RGBA)

'''
RGBA = PIL.Image.open(grabPath())
PIL.Image._show(RGBA)
'''


##-----------------------Pack and Unpack Channels-----------------------
'''
def RGBAtoSingleChannel(RGBA):
    ImgArray = np.asarray(RGBA)#converts immage to array format: ImgArray[red,green,blue,alpha]
    DBGprint(text=ImgArray)
    pass
'''

'''
def PackToRGBA(red,green,blue,alpha,resolution):# return RGBA
    #setup resolution as resolution = [1024,1024]
    #                                   ^     ^
    #                                   |     |
    #                                 Width,height
    
    #RArray = np.asarray(red)
    #GArray = np.asarray(green)
    #BArray = np.asarray(blue)
    #AArray = np.asarray(alpha)

    RArray = np.asarray(red)
    GArray = np.asarray(green)
    BArray = np.asarray(blue)
    AArray = np.asarray(alpha)

    PackedArray = np.array([RArray[0],GArray[0],BArray[0],AArray[0]])

    DBGprint(PackedArray)

    #       Height and width are switched in numpy for some reason
    #                     Height       Width
    #                       V            V
    data = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)

    #PackedArray = np.zeros((5,5))
    DBGprint(PackedArray)

    RGBA = PIL.Image.fromarray(PackedArray)
    DBGprint(RGBA)
    PIL.Image._show(RGBA)#for debug opens the image in external

    #RGBA = Image.fromarray(data, 'RGB')
    return RGBA
'''

def packRGBA(red,green,blue,alpha,resolution):

    #---Make linear/grayscale images
    '''
    redLin = Image.Image.getchannel(channel=0,self=red)
    DBGprint(red)
    greenLin = Image.Image.getchannel(channel=0,self=green)
    DBGprint(green)
    blueLin = Image.Image.getchannel(channel=0,self=blue)
    DBGprint(blue)
    alphaLin = Image.Image.getchannel(channel=0,self=alpha)
    DBGprint(alpha)
    '''
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


##-----------------------GUI-----------------------

#---->button class:
#location
#funcion
#colour/texture
#animation
    #---->slider subclass
    #size
    #values
    #textures

#---->window class:
#size
#buttons (childeren)
#colour/texture



##-----------------------Logic Maths etc-----------------------


running = True
while running:

    unpack = True
    
    if unpack:#if unpack mode is true
        #import packed
        RGBA = openImg(text="Open channel packed image",fileName="ORMA.png")

        #unpacks imported image
        Rchan,Gchan,Bchan,Achan = unpackRGBA(RGBA)

        #exports images
        savImg(export=Rchan,text="save Red channel texture, usually Ambient Occlusion",defaultName="Occlusion.png")

        savImg(export=Gchan,text="save Green channel texture, usually Roughness",defaultName="Roughness.png")

        savImg(export=Bchan,text="save Blue channel texture, usually Metalic",defaultName="Metalic.png")

        savImg(export=Achan,text="save Alpha channel texture, usually reserved for Mask",defaultName="Alpha_Mask.png")

    else:#if unpack mode is false
        #Import RGBA channels

        Rchan = openImg(text="open Red channel texture, usually Ambient Occlusion",fileName="Occlusion.png")
        print ("here are the details for the Red channel:", Rchan)
        #PIL.Image._show(Rchan)#for debug opens the image in external
        
        Gchan = openImg(text="open Green channel texture, usually Roughness",fileName="Roughness.png")
        print ("here are the details for the Green channel:", Gchan)
        #PIL.Image._show(Gchan)

        Bchan = openImg(text="open Blue channel texture, usually Metalic",fileName="Metalic.png")
        print ("here are the details for the Blue channel:", Bchan)
        #PIL.Image._show(Bchan)

        Achan = openImg(text="open Alpha channel texture, usually reserved for Mask",fileName="Alpha_Mask.png")
        print ("here are the details for the Alpha channel:", Achan)
        #PIL.Image._show(Achan)

        RGBA = packRGBA(red=Rchan,green=Gchan,blue=Bchan,alpha=Achan,resolution=[1024,1024])

        savImg(export=RGBA,text="save output file as",defaultName="ORMA.png")#change Rchan to RGBA when files are packed

        #Export packed file
        #filePath = filedialog.asksaveasfile()
        #Rchan.save(fp=str(filePath), format="png")
    

    q = input ("press enter to run again or type quit to end")
    if q == ("quit") or q == ("q"):
        running = False
    