import PIL
from PIL import Image
import numpy as np




def PackToRGBA():# return RGBA
    #setup resolution as resolution = [1024,1024]
    #                                   ^     ^
    #                                   |     |
    #                                 Width,height
    
    red = [250,250,128]
    green = [128,250,10]
    blue = [0,0,0]
    alpha = [128,128,128]



    '''RArray = np.asarray(red)
    GArray = np.asarray(green)
    BArray = np.asarray(blue)
    AArray = np.asarray(alpha)'''

    RArray = np.asarray(red)
    GArray = np.asarray(green)
    BArray = np.asarray(blue)
    AArray = np.asarray(alpha)

    PackedArray = np.array([red[0],green[0],blue[0],alpha[0]])

    print(PackedArray)

    #       Height and width are switched in numpy for some reason
    #                     Height       Width
    #                       V            V
    #data = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)

    #PackedArray = np.zeros((5,5))
    print(PackedArray)
    '''
    RGBA = Image.fromarray(PackedArray)
    print(RGBA)
    Image._show(RGBA)#for debug opens the image in external
    '''
    #RGBA = Image.fromarray(data, 'RGB')
    #return RGBA

#PackToRGBA()

img  = PIL.Image.open("./Channel_Packing_Tool/default_assets/ORMA.png")
#a = np.asarray(img)
array = np.asarray(img)

red = array[:, :, 0]
green = array[:, :, 1]
blue = array[:, :, 2]
alpha = array[:, :, 3]

'''red = np.asarray(img)
green = np.asarray(img)
blue = np.asarray(img)
alpha = np.asarray(img)
'''

#a = np.array([red[0],green[1],blue[2],alpha[3]])

#nicked code
img = Image.open("test_image.png")
M = np.asarray(img)

red_channel = M[:, :, 0]
green_channel = M[:, :, 1]
blue_channel = M[:, :, 2]
#nicked code


#R = np.asarray(img)
a = np.zeros((1024,1024))
a[0:1023, 0:1023] = red[0:1023,0:1023,0]+red[0:1023,0:1023,1]+red[0:1023,0:1023,2]

a=red

imgRepack = Image.fromarray(a)

print("the image in array form is",a)
Image._show(imgRepack)

'''
a = np.zeros((5, 5))
im = Image.fromarray(a)
print(im)'''