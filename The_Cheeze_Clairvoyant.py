#################################################
#           THE CHEEZE CLAIRVOYANT              #
#################################################
#                                               #
#      Coded by JonnyBanana from Scratch        #
#        https://github.com/JonnyBanana         #
#    http://www.youtube.com/c/HowToHackItalia   #
#                                               #
#################################################
#                                               #
#            Simple Python Algorithm            #
#            to Make  Random Battles            #
#                                               #
#################################################

import random
import os

os.system("color E0")
os.system("mode con:cols=70 lines=55")

def elements():
    elements=['FIRE', 'WATER', 'WIND']
    elemental_attack=random.randint(0,2)
    print ("\n\n YOUR FIRST ELEMENTAL ATTACK IS: \n")
    print(elements[elemental_attack] + "\n",  file = open("temp\choice.txt",'w'))
    f = open('temp\choice.txt', 'r') 
    data = f.read()      
    f.close()              
    print (" " + data)         
    os.system("pause")
    
    elemental_attack=random.randint(0,2)
    print ("\n\n YOUR SECOND ELEMENTAL ATTACK IS: \n")
    print(elements[elemental_attack] + "\n",  file = open("temp\choice.txt",'w'))
    f = open('temp\choice.txt', 'r') 
    data = f.read()      
    f.close()              
    print (" " + data)         
    os.system("pause")

    elemental_attack=random.randint(0,2)
    print ("\n\n YOUR THIRD ELEMENTAL ATTACK IS: \n")
    print(elements[elemental_attack] + "\n",  file = open("temp\choice.txt",'w'))
    f = open('temp\choice.txt', 'r') 
    data = f.read()      
    f.close()              
    print (" " + data)         
    os.system("pause")

    elemental_attack=random.randint(0,2)
    print ("\n\n YOUR FOURTH ELEMENTAL ATTACK IS: \n")
    print(elements[elemental_attack] + "\n",  file = open("temp\choice.txt",'w'))
    f = open('temp\choice.txt', 'r') 
    data = f.read()      
    f.close()              
    print (" " + data)         
    os.system("pause")

    elemental_attack=random.randint(0,2)
    print ("\n\n YOUR FIFTH ELEMENTAL ATTACK IS: \n")
    print(elements[elemental_attack] + "\n",  file = open("temp\choice.txt",'w'))
    f = open('temp\choice.txt', 'r') 
    data = f.read()      
    f.close()              
    print (" " + data)         
    os.system("pause")
    print("\n\n THAT'S ALL WIZARD! \n")
    os.system("pause")
    os.system("cls")
    os.system("del temp\choice.txt")

while True:
    print ("")
    print ("         ________ ______  _______ ______________  ____ ")            
    print ("        /_  __/ // / __/ / ___/ // / __/ __/_  / / __/  ")           
    print ("         / / / _  / _/  / /__/ _  / _// _/  / /_/ _/     ")          
    print ("        /_/_/_//_/___/_ \___/_//_/___/___/_/___/___/")
    print ("")
    print ("                           /\ ")
    print ("                          /  \  ")
    print ("                         /   (_")
    print ("                        /.-''-.\ ")
    print ("                       /< (()) >\  ")
    print ("                      /  `-..-'  \ ")
    print ("                     /   _        \ ")
    print ("                    /   (_)   _    \ ")
    print ("                   _)        (_)    \ ")
    print ("                  /   _              \ ")
    print ("                 /   (_)             (_")
    print ("                /______________________\ ")
    print ("")
    print ("   _______   ___   _________   ________  _____   _  ________ ")
    print ("  / ___/ /  / _ | /  _/ _ \ | / / __ \ \/ / _ | / |/ /_  __/")
    print (" / /__/ /__/ __ |_/ // , _/ |/ / /_/ /\  / __ |/    / / /   ")
    print (" \___/____/_/ |_/___/_/|_||___/\____/ /_/_/ |_/_/|_/ /_/    ")
    print ("\n\n PRESS ENTER TO KNOW WHAT I SAW IN THE SPHERE ... \n")
    os.system("pause")
    elements()
