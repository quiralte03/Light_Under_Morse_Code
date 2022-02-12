# Light Under the Morse Code
This program translates a string into Morse code, represented in the form of light through an LED.
----- ----- ----- ----- ----- ---
What you need:
 I used a Raspberry Pi 3, some jumpers, a breadboard, and a led.
 Remember before start working to update and upgrade your Linux system. 
 
    sudo apt-get update
    sudo apt-get upgrade
 
 Use any Python editor, I recommend using Thonny, it comes pre-installed on the Raspberry Pi operating system.
----- ----- ----- ----- ----- ---
Code Explanation:
I try to get the code as basic as possible, at the same time I made it so it can be modified so it can be used with different devices, 
for example instead of a led, could be modified to use a buzzer. In morse code, there are three main ideas: the dot, the dash, and the silence.
 
* The dot has a one-unit portion.
* The dash has a three-unit portion.
* The silence has a two-unit portion.

 Having the main ideas of Morse Code, the program just need a Morse alphabet, a translator, and user input.
 For the Morse alphabet, I just represent it using the dot, dash, and silence functions per each letter.
 For the translator, I convert the word given by the user into a list. Then using an if statement to check what is word given.
 To finish the program, it just needs an intro to the program and an input method. I add a Complete message and a sequence of lights at the end.
