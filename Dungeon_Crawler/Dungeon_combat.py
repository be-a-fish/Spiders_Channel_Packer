print ("Game Start")

import random

##playerName = input("What is the players name? ")
##print("The player name is", playerName)

'''
class Charicter():
    def __init__(self, in_name, in_str, in_def, in_health = 100):
        self.name = in_name
        self.strength = in_str
        self.defence = in_def
        self.current_health = in_health
        self.max_health = in_health
'''


##define player default stats using dictionary
playerStats = {
    "name": input("What is the players name? "),
    "weapon": "unarmed",
    "strength": 5,
    "health": 100.0,
    "clothes": "band shirt",
    "defence": 2,
    "diyMaterials": 5,
    "cash": random.randint(1,10)
}
print ("My stats are" , playerStats)

#how to access value from dictionary:
print ("my health is",playerStats["health"])


foe = "Default foe"

#generates dropped item

def itemDrop(enemy,level):
    
    drop = random.choice(["some change","some shit","a weapon","some clothing"])
    print("The",enemy,"dropped",drop)
    itemGain = random.randint(level,level*10)

    #add moneys
    if drop == "some change":
        playerStats["cash"] = playerStats["cash"] + itemGain
        print("You now have",playerStats["cash"], "quid")
    
    #add DIY materials
    elif drop == "some shit":
        playerStats["diyMaterials"] = playerStats["diyMaterials"] + itemGain
        diyRandDrop = random.choice(["jacket spikes","fabric scraps", "bottle caps", "beer tabs", "spools of thread", "damaged chain links", "human teeth", "crayons"])

        print("You put", itemGain, diyRandDrop, "in your pocket")
        print("You now have",playerStats["diyMaterials"], "DIY materials")
    
    #add weapons
    elif drop == "a weapon":
        weapon = random.choice(["tazer","set of knuckle dusters", "broken bottle", "pride flag", "reporposed umbrella", "spikey bat", "toothbrush shank", "cheap knife", "nerf gun", "spikey glove","sword for some reason"])
        playerStats["strength"] = playerStats["strength"] + itemGain
        playerStats["weapon"] = weapon
        print("You find a level", itemGain, weapon)
    #add aromour
    elif drop == "some clothing":
        clothes = random.choice(["pair of Knockoff Doc Martens", "pink socks", "spikey jacket", "shark tooth necklace", "offensive shirt", "glasses", "skate helmet","fancy suit"])
        playerStats["defence"] = playerStats["defence"] + itemGain
        playerStats["clothes"] = clothes
        print("You find a level", itemGain, clothes)
    



#generates a foe for combat
def EnemyGenerator(enemiesList):
    foe = random.choice(enemiesList)
    #print ("your foe is", foe)
    return foe

#defines what happens when you enter combat
def Combat(enemy,enemyHP, enemyAttack, level):
    inCombat = True
    print ("The",enemy, "poised for battle")
    input ("press enter to continue")
    while (inCombat == True):
        #combat here
        playerDamage = random.randint (1, playerStats["strength"])
        enemyHP = enemyHP - playerDamage
        
        randomAttackList = ["punch", "slap", "poke", "kick", "kiss", "bite", "insult", "karate chop", "stomp", "spit at", "stab", "throw a rock at", "dropkick"]
        randomWoundList = ["face", "head", "leg", "groin","arm","nose", "teeth", "spleen", "knee", "stomach", "elbow", "eye","tit","feelings","brand new shoes","dick","pancreas", "browser history"]
        print("you", random.choice(randomAttackList), "them in the", random.choice(randomWoundList), "dealing",playerDamage, "HP")
        print("their health is now", enemyHP)

        action = input("press enter to continue")
        

        if enemyHP <= 0: #end combat if enemy is dead
            randomFleeList = ["fees","fucks off","falls in battle","is sent to Jesus","is sent to Vallhalla","suddenly had an important doctors appointment" ,"begs for their life", "fucking dies","doesn't seem to be breathing", "spontaniously combusts","runs for the bathroom","starts moaning and you feel uncomfortable","makes some excuse to leave"]
            print("the",enemy,random.choice(randomFleeList))

            itemDrop(enemy=enemy, level=level)

            inCombat = False
        
        else: #player takes damage
            enemyDamage = random.randint(1,enemyAttack) - random.randint(0,playerStats["defence"])
            if enemyDamage <= 0:
                enemyDamage = 1
            playerStats["health"] = playerStats["health"] - enemyDamage

            print("They", random.choice(randomAttackList), "you in the", random.choice(randomWoundList), "dealing",enemyDamage, "HP")
            print("your health is now", playerStats["health"])

            action = input("press enter to continue")

            if playerStats["health"] <= 0: #kill when player dies
                randomDeathMsg = ["falls in battle","is sent to Jesus","is sent to Vallhalla","fucking dies","fainted","suddenly had an important doctors appointment","spontaniously combusts","doesn't seem to be breathing"]
                print(playerStats["name"],random.choice(randomDeathMsg))
                #add death here
                print("Yeah I haven't programed in a death yet")
            
            
#Combat(enemy=foe, enemyHP=10, enemyAttack=3)




def Encounter(location, level):
    print("you're current location is", location)
    encounterNum = random.randint(1,1)
    #encounter 1 = hostile
    #encounter 2 = neutral
    #encounter 3 = friendly
    #encounter 4 = boss

    if encounterNum == 1:    #encounter 1 - HOSTILE
        print("The train stops and some people get on.")
        #hostile foe list
        #  |    |    |
        #  V    V    V
        foeList = ["Spineless liberal", "Poser", "Tory", "Cop", "Crackhead", "Rando", "Pedo looking mf", "Violent ex", "Podcaster", "Fucking tourist", "Skinhead", "Reform candidate"]
        foe = EnemyGenerator(foeList)
        print("A", foe, "gets on the train and looks at you funny")

        #make a choice
        choiceMade = False
        while choiceMade == False:#loops until a valid input is made
            print("Your actions are: Attack:1, Argue:2, Ignore:3")
            action = input("what do you do?")
            if action == "1" or "2" or "3":
                choiceMade = True
            else:
                print("That's not a valid choice nob head")
            

        if action == "1":
            Combat(enemy=foe, enemyHP=(10*level), enemyAttack=(5*level), level=level)
            
        elif action == "2" or "3":
            print("yeah I havent coded that yet. you'll have to pick 1 to attack")
            #-Random attack
            #randomAttackList = ["punch", "slap", "poke", "kick", "kiss", "bite","insult", "karate chop","stomp","spit at"]
            #randomWoundList = ["face", "leg", "groin","arm","nose", "eye","tit","feelings","brand new shoes","dick"]
            #print("you", random.choice(randomAttackList), "them in the", random.choice(randomWoundList))



    elif encounterNum == 2:  #encounter 2 - NEUTRAL
        pass

#---------------------------------Areas---------------------------------
Locations = {
# Difficulty level   Location
#   |                |          
    1: "The Northen Line",
    2: "The Jubilee Line",
    3: "The Waterloo & City Line",
    4: "The Piccadilly Line",
    5: "The Victoria Line",
    6: "The Distric Line",
    7: "The DLR"
}
#------------------------------------------------------------------------


print(playerStats["name"],"hops the barriers and enters the tube station")
gameRun = True
level = 1
while gameRun == True:

    line = Locations[level]
    Encounter(location=line, level=level)
    
    print ("My stats are" , playerStats)
    input ("press enter to change trainlines")

    level = level+1
    if level > 7: #if the level is larger than the max
        input("congrats, you beat the game. You conquered Londons shitty tube lines. You want a trophy? Fuck off")
        gameRun = False

                



#foeList = ["Liberal", "Poser", "Tory", "Cop", "Crackhead"]
#foe = EnemyGenerator(foeList)







