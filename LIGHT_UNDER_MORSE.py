# IGNACIO QUIRALTE PEREZ
# LIGHT UNDER THE MORSE
# TRANSLATE STRING TO MORSE CODE VIA LIGHT ( it can be modify to other vias as audio)

from gpiozero import LED
from time import sleep

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

# Initialize LED
led = LED(17)

# Morse code timing
dot_duration = 0.5
dash_duration = 1.5
letter_space_duration = 1.0
word_space_duration = 2.0

def translate_to_morse(letter):
    return morse_code.get(letter.upper(), '')

def blink(symbol):
    if symbol == '.':
        led.on()
        sleep(dot_duration)
    elif symbol == '-':
        led.on()
        sleep(dash_duration)
    led.off()
    sleep(dot_duration)

def translate_word(word):
    for letter in word:
        code = translate_to_morse(letter)
        if code:
            for symbol in code:
                blink(symbol)
            sleep(letter_space_duration)
        else:
            print(f"Error: '{letter}' cannot be translated to Morse code.")

def main():
    print("WELCOME TO LIGHT UNDER THE MORSE\n")
    word = input("ENTER A WORD TO TRANSLATE TO MORSE CODE\n>").upper()
    translate_word(word)
    print("\nCOMPLETE\nTHANK YOU!")

if __name__ == "__main__":
    main()
