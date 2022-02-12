# IGNACIO QUIRALTE PEREZ
# LIGHT UNDER THE MORSE
# TRANSLATE STRING TO MORSE CODE VIA LIGHT ( it can be modify to other vias as audio)


#Importing functions from main package
from gpiozero import LED
from time import sleep

# Assign physical port from RP pi
led = LED(17)


# MAIN FUNCTIONS
def dot():
    ### Creating a function that represents a dot in Morse code ###
    led.on()
    sleep(1)
    led.off()
    sleep(0.5)
    
def dash():
    ### Creating a function that represents a slash in Morse code ###
    led.on()
    sleep(3)
    led.off()
    sleep(0.5)

def silence():
    ### Create a function that represents a silence between letters ###
    led.off()
    sleep(2)
    

# LETTERS FUNCTIONS    
def A():
    dot()
    dash()
    silence()

def B():
    dash()
    dot()
    dot()
    dot()
    silence()
    
def C():
    dash()
    dot()
    dash()
    dot()
    silence()

def D():
    dash()
    dot()
    dot()
    silence()
    
def E():
    dot()
    silence()
    
def F():
    dot()
    dot()
    dash()
    dot()
    silence()
    
def G():
    dash()
    dash()
    dot()
    silence()
    
def H():
    dot()
    dot()
    dot()
    dot()
    silence()
    
def I():
    dot()
    dot()
    silence()
    
def J():
    dot()
    dash()
    dash()
    dash()
    silence()
    
def K():
    dot()
    dash()
    dot()
    silence()
    
def L():
    dot()
    dash()
    dot()
    dot()
    silence()
    
def M():
    dash()
    dash()
    silence()
    
def N():
    dash()
    dot()
    silence()
    
def O():
    dash()
    dash()
    dash()
    silence()
    
def P():
    dot()
    dash()
    dash()
    dot()
    silence()
    
def Q():
    dash()
    dash()
    dot()
    dash()
    silence()
    
def R():
    dot()
    dash()
    dot()
    silence()
    
def S():
    dot()
    dot()
    dot()
    silence()
    
def T():
    dash()
    silence()
    
def U():
    dot()
    dot()
    dash()
    silence()
    
def V():
    dot()
    dot()
    dot()
    dash()
    silence()
    
def W():
    dot()
    dash()
    dash()
    silence()
    
def X():
    dash()
    dot()
    dot()
    dash()
    silence()
    
def Y():
    dash()
    dot()
    dash()
    dash()
    silence()
    
def Z():
    dash()
    dash()
    dot()
    dot()
    silence()
    
def ERROR():
    for i in range(10):
                led.off()
                sleep(0.1)
                led.on()
                sleep(0.1)
def FINALE():
    for i in range(5):
                led.off()
                sleep(0.1)
                led.on()
                sleep(0.1)
    
    
# TRANSLATION FUNCTION
def translation(word_to_translate:str):    
    ###  SLice the word, translate it to Morse Code ###
    
    lenght = len(word_to_translate)
    # Chop the word and using a list per character in it.
    list_letters = list(word_to_translate)
    
    # Set number to stop
    n = 0
    
    # While loop that runs for each letter in the word
    while n != (lenght - 1):
        
        # Add one to the number
        n += 1
        
        # Check for the letter
        if list_letters[n] == 'A':
            A()
        elif list_letters[n] == 'B':
            B()
        elif list_letters[n] == 'C':
            C()
        elif list_letters[n] == 'D':
            D()
        elif list_letters[n] == 'E':
            E()
        elif list_letters[n] == 'F':
            F()
        elif list_letters[n] == 'G':
            G()
        elif list_letters[n] == 'H':
            H()
        elif list_letters[n] == 'I':
            I()
        elif list_letters[n] == 'J':
            J()
        elif list_letters[n] == 'K':
            K()
        elif list_letters[n] == 'L':
            L()
        elif list_letters[n] == 'M':
            M()
        elif list_letters[n] == 'N':
            N()
        elif list_letters[n] == 'O':
            O()
        elif list_letters[n] == 'P':
            P()
        elif list_letters[n] == 'Q':
            Q()
        elif list_letters[n] == 'R':
            R()
        elif list_letters[n] == 'S':
            S()
        elif list_letters[n] == 'T':
            T()
        elif list_letters[n] == 'U':
            U()
        elif list_letters[n] == 'V':
            V()
        elif list_letters[n] == 'W':
            W()
        elif list_letters[n] == 'X':
            Y()
        elif list_letters[n] == 'Z':
            Z()
        else:
            ERROR()

            
        
# CALL FUNCTIONS AND PROGRAM

# Prompts the user with the intro
print("WELCOME TO LIGHT UNDER THE MORSE")
print("")

# Gets the user input and pass all the string to upper cases
word = input("ENTER A WORD TO TRANSLATE TO MORSE CODE\n>")
word = word.upper()

# Starts the light program
translation(word)

# Prompts the user with a complete and bye message
print("COMPLETE\nTHANK YOU!")
FINALE()