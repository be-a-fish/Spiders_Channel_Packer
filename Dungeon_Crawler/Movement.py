import random




layer1 = ["#","#","=","#","#","#","=","#","#","#","#","=","#","#","#","=","#","#",]
layer2 = ["#"," "," "," "," "," "," "," ","#","#"," "," "," "," "," "," "," ","#",]
layer3 = ["="," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","=",]
layer4 = ["#"," "," "," "," "," "," "," ","#","#"," "," "," "," "," "," "," ","#",]
layer5 = ["#","#","=","#","#","#","=","#","#","#","#","=","#","#","#","=","#","#",]

#define tiles for collision etc
collision = ("#")
empty = (" ")
door = ("=")
encounter = ("𓁆")
playerIcon = ("웃")
#other people to use 𓁌 𓀠 𓁋 𓁆 𓁇 𓀒 𓀗 𓀡 𓁲

##------------------------PLAYER-SPAWN-LOCATION---------------------------------
playerCoords = {
    "x":2,
    "y":3
}

def playerSpawn():
    layer3[2] = playerIcon
    playerCoords["x"] = 2
    playerCoords["y"] = 3

def playerMove():
    input()


##------------------------MAP-ENCOUNTERS---------------------------------

def addEncounters(layer,encounterRate): #randomly adds 𓁆 this guy into the area
    iterate = 0
    for i in layer:
        

        #lower the encounter rate the higher chance of an encounter
        #use 10-level to determine enconter rate
        if layer[iterate] == (empty): #checks for no collsion

            if random.randint(1,encounterRate) == 1: 
                layer[iterate] = (encounter)

        iterate = (iterate+1)

##------------------------MAP-CREATION---------------------------------------

def clearMap():
    layer1 = ["#","#","=","#","#","#","=","#","#","#","#","=","#","#","#","=","#","#",]
    layer2 = ["#"," "," "," "," "," "," "," ","#","#"," "," "," "," "," "," "," ","#",]
    layer3 = ["="," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","=",]
    layer4 = ["#"," "," "," "," "," "," "," ","#","#"," "," "," "," "," "," "," ","#",]
    layer5 = ["#","#","=","#","#","#","=","#","#","#","#","=","#","#","#","=","#","#",]

def createMap():
    playerSpawn()
    addEncounters(layer2,3)
    addEncounters(layer3,5)
    addEncounters(layer4,3)

##--------------------------------------------------------------------

##----------------------CONTROLLER----------------------------------------------

def moveController():
    pass

##--------------------------------------------------------------------

##----------------------RENDER-ENGINE----------------------------------------------

def frameRender():
    print ()
    print (layer1)
    print (layer2)
    print (layer3)
    print (layer4)
    print (layer5)
    print ()
    print ("carage 1, Northern Line")

##--------------------------------------------------------------------

##---------------------------MAIN-GAME-LOOP-----------------------------------------

gameRunning = True

while gameRunning == True:
    print("you enter train carage 1")

    frameRender()
    input ("Press enter to continue")

