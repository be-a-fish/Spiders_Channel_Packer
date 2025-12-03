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
moveToCoords = playerCoords

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

#notes:
#
# layer = playerCoords y
# layer1 = y1
# layer5 = y5
#
# playerCoords x is the value in the list

'''
def checkLocation(y, x): #y=layer x=list value
    print ("checking location")

    if y[x] == (collision):
        print ("thats a fucking wall you fuckwit")
        return (False)
    
    if y[x] == (empty):
        playerCoords = moveToCoords
        if y == layer1:
            layer1 [x] = (playerIcon)
        elif y ==
        return (True) #return true if movement possible

    elif y[x] == (door):
        return (True)
'''

def moveController(wasd):
    while wasd != ("w")  or wasd != ("s") or wasd != ("a") or wasd != ("d"):
        
        moveToCoords = playerCoords # so we have 2 positions to check if movement is possible
        y = ("layer"+str(moveToCoords ["y"]))
        print ("wasd is set to", wasd)
        print ("y move to =", y)
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
            if playerCoords ["y"] > 1:#y minimum
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
            if playerCoords ["x"] < 17:#x maximum
                moveToCoords ["x"] = (playerCoords ["x"] + 1)
                print ("player x coords is",playerCoords ["x"])
                
            else: 
                print ("can't move further north")
            
            
        
        #teleport script
        if wasd == ("w") or wasd == ("s") or wasd == ("a") or wasd == ("d"):
            print ("player will move when this script is finished")
            checkSpot = ("#")

            if y == ("layer1"):
                if layer1[moveToCoords] == (collision):
                    print ("thats a fucking wall you fuckwit")
                else:
                    layer2 = [x.replace(playerIcon, " ") for x in layer2]
                    layer1[moveToCoords] = (playerIcon)
            
            if y == ("layer2"):
                if layer2[moveToCoords] == (collision):
                    print ("thats a fucking wall you fuckwit")
                else:
                    layer3 = [x.replace(playerIcon, " ") for x in layer3]
                    layer1 = [x.replace(playerIcon, " ") for x in layer1]
                    layer2[moveToCoords] = (playerIcon)
            if y == ("layer3"):
                if layer3[moveToCoords] == (collision):
                    print ("thats a fucking wall you fuckwit")
                else:
                    layer4 = [x.replace(playerIcon, " ") for x in layer4]
                    layer2 = [x.replace(playerIcon, " ") for x in layer2]
                    layer3[moveToCoords] = (playerIcon)
            if y == ("layer4"):
                if layer4[moveToCoords] == (collision):
                    print ("thats a fucking wall you fuckwit")
                else:
                    layer5 = [x.replace(playerIcon, " ") for x in layer5]
                    layer3 = [x.replace(playerIcon, " ") for x in layer3]
                    layer4[moveToCoords] = (playerIcon)
            if y == ("layer5"):
                if layer5[moveToCoords] == (collision):
                    print ("thats a fucking wall you fuckwit")
                else:
                    layer4 = [x.replace(playerIcon, " ") for x in layer4]
                    layer5[moveToCoords] = (playerIcon)
                    

            print ("checking location")
            break

            '''
            if y[x] == (collision):
                print ("thats a fucking wall you fuckwit")
                return (False)
            
            if y[x] == (empty):
                playerCoords = moveToCoords
                if y == layer1:
                    layer1 [x] = (playerIcon)
                elif y == 
                return (True) #return true if movement possible

            elif y[x] == (door):
                return (True)
            '''

            
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
    

