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
    "strength": 5,
    "health": 100.0,
    "defence": 5,
    "speed": 5,
    "Cash": random.randint(1,10)
}
print ("My stats are" , playerStats)

#how to access value from dictionary:
print ("my health is",playerStats["health"])


foe = "Default foe"


def itemDrop(enemy):
    print("The",enemy,"dropped something")


#generates a foe for combat
def EnemyGenerator(enemiesList):
    foe = random.choice(enemiesList)
    print ("your foe is", foe)
    return foe



location = "The Northen Line"
def Encounter(location):
    print("you're current location is", location)
    encounterNum = random.randint(1,1)
    if encounterNum == 1:#encounter 1
        print("The train stops and some people get on.")
        foeList = ["Liberal", "Poser", "Tory", "Cop", "Crackhead"]
        foe = EnemyGenerator(foeList)
        print("A", foe, "gets on the train and looks at you funny")
        choiceMade = False
        while choiceMade == False:
            print("Your actions are: Attack:1, Argue:2, Ignore:3")
            action = input("what do you do?")
            if action == "1":

                #-Random attack
                randomAttackList = ["punch", "slap", "poke", "kick", "kiss", "bite","insult", "karate chop","stomp"]
                randomWoundList = ["face", "leg", "groin","arm","nose", "eye","tit","feelings","brand new shoes","dick"]
                print("you", random.choice(randomAttackList), "them in the", random.choice(randomWoundList))


Encounter(location=location)
                
    


foeList = ["Liberal", "Poser", "Tory", "Cop", "Crackhead"]
foe = EnemyGenerator(foeList)


#defines what happens when you enter combat
def Combat(enemy):
    inCombat = True
    print ("The",enemy ," attacks")
    while (inCombat == True):
        print("*Chuckles* I'm in danger")#add combat here
        inCombat = False

Combat(enemy=foe)




