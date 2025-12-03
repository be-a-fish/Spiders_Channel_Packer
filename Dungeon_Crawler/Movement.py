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
playerIcon = ("Ⓐ")
#other people to use 𓁌 𓀠 𓁋 𓁆 𓁇 𓀒 𓀗 𓀡 𓁲 웃 ☠ 〠 𐇑

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


def moveController(wasd):
    while wasd != ("w")  or wasd != ("s") or wasd != ("a") or wasd != ("d"):
        moveToCoords = playerCoords # a backup if the movement fails
        print ("wasd is set to", wasd)
        wasd = input("Select movement direction (wasd)")
        #move north
        if wasd == ("w"):
            print ("moving north")
            if playerCoords ["y"] < 5:#y maximum
                moveToCoords ["y"] = (playerCoords ["y"] + 1)
                print ("player y coords is",playerCoords ["y"])
                
            else: 
                print ("can't move further north")

        #move south
        elif wasd == ("s"):
            print ("moving south")
            if playerCoords ["y"] > 0:#y minimum
                moveToCoords ["y"] = (playerCoords ["y"] - 1)
                print ("player y coords is",playerCoords ["y"])
                
            else: 
                print ("can't move further south")

        #move west
        elif wasd == ("a"):
            print ("moving west")
            if playerCoords ["x"] > 0:#x minimum
                moveToCoords ["x"] = (playerCoords ["x"] - 1)
                print ("player x coords is",playerCoords ["x"])
                
            else: 
                print ("can't move further west")
            
        #move east
        elif wasd == ("d"):
            print ("moving east")
            if playerCoords ["x"] < 5:#x maximum
                moveToCoords ["x"] = (playerCoords ["x"] + 1)
                print ("player x coords is",playerCoords ["x"])
                
            else: 
                print ("can't move further north")
            
            
        
        #teleport script
        if wasd == ("w") or wasd == ("s") or wasd == ("a") or wasd == ("d"):
            print ("player will move when this script is finished")
            break
        else:
            print("that's not a valid input moron. press w, s, a or d then enter you fucking lemon")
            


##--------------------------------------------------------------------

##----------------------RENDER-ENGINE----------------------------------------------

def frameRender():# * prints list as string
    print ()
    print (*layer1)
    print (*layer2)
    print (*layer3)
    print (*layer4)
    print (*layer5)
    print ()
    print ("carage 1, Northern Line")

##--------------------------------------------------------------------

##---------------------------MAIN-GAME-LOOP-----------------------------------------

gameRunning = True
newArea = True

while gameRunning == True:
    if newArea == True:
        createMap()
        newArea = False
        print("you enter train carage 1")

    frameRender()
    moveController(wasd = "x")
    

