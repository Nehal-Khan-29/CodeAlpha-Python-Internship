# Modules ===================================================================================================================

from random_word import RandomWords
import os

# Variables =================================================================================================================

error_limit = 4
error_count = 0
random_word = RandomWords().get_random_word()
answer=[]
string = ""

x0="""
         _____
         |   |
         O   |
        /    |
             |
             |
        _____|   """
x1="""
         _____
         |   |
         O   |
        /|   |
             |
             |
        _____|   """
        
x2="""
         _____
         |   |
         O   |
        /|\  |
             |
             |
        _____|    """
x3="""
         _____
         |   |
         O   |
        /|\  |
        /    |
             |
        _____|    """
x4="""
         _____
         |   |
         O   |
        /|\  |
        / \  |
             |
        _____|    """

# Game =================================================================================================================

for i in range(len(random_word)):
    answer.append("_")
    string+="_"
    
while error_count < error_limit:
    os.system('cls')
    print("\nThe Error limit: 4")
    print("Your Error count: ", error_count)
    #print(random_word)
    print(x0)
    print("\n",string)
    enter_letter = input("\n\nEnter a letter: ")
    
    if enter_letter in random_word:
        for i,j in enumerate(random_word):
            if enter_letter == j:
                answer[i] = j
        
        string = ""   
        for i in answer: 
            string+=i
        
    else:
        error_count+=1
        if error_count == 1:
            x0=x1
        elif error_count == 2:
            x0=x2
        elif error_count == 3:
            x0=x3
        elif error_count == 4:
            x0=x4
            os.system('cls')
            print('\033[31m' + x0 + '\033[0m')
            print("\n",string)
            print("\n",'\033[34m' + random_word + '\033[0m')
            print('\033[31m'+"\nYou Lose !!! You failed Him"+ '\033[0m')
    
    if string == random_word:
        os.system('cls')
        print("\nThe Error limit: 4")
        print("Your Error count: ", error_count)
        print('\033[32m' + x0+'\033[0m')
        print("\n",'\033[34m' + string+'\033[0m')
        print('\033[32m'+"\nYou win !!! You saved Him\n"+ '\033[0m')
        break
    
