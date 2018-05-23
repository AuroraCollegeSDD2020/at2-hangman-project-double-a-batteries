import random
import time

wordsList = open("word.txt", "r")
wordsList = wordsList.readlines()
word = random.choice(wordsList)
word = str(word)
word = list(word)
del word[-1]
print(word)
lives = 11
notGuessed = len(word)
yesOrNo = False
print(notGuessed)
type1 = """
  ---------
   |      o
   |     -|-
   |      ^
   |     / \\
--------
"""
type2 = """
  ---------
   |      o
   |     -|-
   |      ^
   |     / 
--------
"""
type3 = """
  ---------
   |      o
   |     -|-
   |      ^
   |     
--------
"""
type4 = """
  ---------
   |      o
   |     -|-
   |      
   |     
--------
"""
type5 = """
  ---------
   |      o
   |     -|
   |      
   |     
--------
"""
type6 = """
  ---------
   |      o
   |      |
   |      
   |     
--------
"""
type7 = """
  ---------
   |      o
   |     
   |      
   |     
--------
"""
type8 = """
  ---------
   |      
   |    
   |      
   |     
--------
"""
type9 = """
  
   |      
   |     
   |      
   |     
--------
"""
type10 = """

        
      
         
       
--------
"""
print("""
 __      __       .__                                  __           .__                                                 
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   |  |__ _____    ____    ____   _____ _____    ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  |  |  \\\\__  \  /    \  / ___\ /     \\\\__  \  /    \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> ) |   Y  \/ __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \\
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/  |___|  (____  /___|  /\___  /|__|_|  (____  /___|  /
       \/       \/          \/            \/     \/                      \/     \/     \//_____/       \/     \/     \/ """)

time.sleep(2)
print("Please enter your name")
time.sleep(1)
name = input("YOUR NAME HERE :>> ")
print("\n"*50)
time.sleep(1)
while True:
    if lives == 10:
        print(type10)
    elif lives == 9:
        print(type9)
    elif lives == 8:
        print(type8)
    elif lives == 7:
        print(type7)
    elif lives == 6:
        print(type6)
    elif lives == 5:
        print(type5)
    elif lives == 4:
        print(type4)
    elif lives == 3:
        print(type3)
    elif lives == 2:
        print(type2)
    elif lives == 1:
        print(type1)
    guess = input("GUESS LETTER HERE:>> ").lower()
    for letter in word:
        if str(letter) == guess:
            notGuessed -= 1
            yesOrNo = True
    if not yesOrNo:
        lives -= 1

    time.sleep(2)