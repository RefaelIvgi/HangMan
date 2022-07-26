print("Code By Refael Ivgi - Enjoy!")

import random
print("""
      
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
   
      """)

def is_valid_input(letter_guessed , old_letters):
    if (letter_guessed in check or len(letter_guessed)>1 or letter_guessed in old_letters) :
        return False
    else:
        old_letters += [letter_guessed]
        return True
 
def check_win(secret_word, old_letters,):
    count=0
    for i in range(len(secret_word)):
        for j in range(len(secret_word[i])):
            if(secret_word[i] in old_letters):
              count+=1
              
    if(count == len(secret_word)):
        return True
    else:
        return False
    
def check_wrong(secret_word, old_letters,wrong):
    flag = True
    if(old_letters[-1] in secret_word):
            return False
    else:
            return True
    

def show_hidden_word(secret_word, old_letters):
    newstring=""
    for i in range(len(secret_word)):
        for j in range(len(secret_word[i])):
            if(secret_word[i] in old_letters):
              newstring+= secret_word[i][j]
            else:
                newstring += "_"
            
    return newstring

def print_hangman(num_of_tries):
        if(num_of_tries==0):
            return """
                    WELL DONE - YOU SAVE THE MAN!
                    """
        
        if(num_of_tries==1):
            return """
                 x-------x
                 |
                 |
                 |
                 |
                 |
                   """
        if(num_of_tries==2):
                return """
              
            x-------x
            |       |
            |       0
            |
            |
            |
              
              """   
         
        if(num_of_tries==3):
            return """
                  
                x-------x
                |       |
                |       0
                |       |
                |
                |
                  
                  """
        if(num_of_tries==4):
                    return """
              
            x-------x
            |       |
            |       0
            |     (/|\)
            |
            |
            
              """ 
        if(num_of_tries==5):
            return """
              
            x-------x
            |       |
            |       0
            |     (/|\)
            |     (/  )
            |
            
              """
        if(num_of_tries==6):
                return """
                  
                x-------x
                |       |
                |       0
                |     (/|\)
                |     (/ \)
                |
                  
                  
                  
                  """

print("""
      FIRST STATE
            x-------x
      """)
MAX_TRIES=6
mistakes=0
words = ['one','two','three','four','five','six','seven']
check="!@#$%^&*()12345678900"
secret_word=random.choice(words)

old_letters = []

print("BOARD:"+" "+show_hidden_word(secret_word,old_letters))

while MAX_TRIES > 0 :
    str2=input("enter a letter:",)
    if (is_valid_input(str2,old_letters)==True):
        print(old_letters)
        print("BOARD:"+" "+show_hidden_word(secret_word,old_letters))
        
        
        if(check_wrong(secret_word, old_letters,mistakes)==True):
            mistakes+=1
            print(print_hangman(mistakes))
            
        else:
             print(print_hangman(mistakes))
                
                
                
        
        MAX_TRIES -=1
        if(check_win(secret_word, old_letters)==True):
            print("WIN")
            MAX_TRIES = 0
    else:
        str2=input("enter again letter:",)
        if (is_valid_input(str2,old_letters)==True):
            print(old_letters)
            print("BOARD:"+" "+show_hidden_word(secret_word,old_letters))
            
            
            if(check_wrong(secret_word, old_letters,mistakes)==True):
                    mistakes+=1
                    print(print_hangman(mistakes))
            else:
                print(print_hangman(mistakes))
                
                
                
                
            MAX_TRIES -=1
            if(check_win(secret_word, old_letters)==True):
                print("WIN")
                MAX_TRIES = 0
             

    

print("GAME OVER ! THE WORD WAS ->" + " " + secret_word)
