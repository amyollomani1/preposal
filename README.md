# preposal

Youtube Video URL
https://youtu.be/UzY8TlYhMGY


Description of project:
This project was Hangman (christmas edition). A random phrase or word was picked from a list that I created that the user would have to guess. We used a turtle module to draw out the hangman board. If they guessed the word correctly before the Hangman was drawn, then the turtle would write out "YOU WON" and the code would stop running. If they lost, then the turtle would write you "YOU LOST" instead.

Adversities and problem solving:
The hardest part of the code was drawing out the correctly guessed character on the corresponding line and also drawing out letters that appeared multiple times in the word (such as e or i). To solve the first part, I created two dictionary which stored the x and y corridates of each line. If the user correctly guess the first charavter, than I would access the first character's cordinates in the dictionary and draw out the character. The way I solved the second problem was by using multiple nested if and while loops. By doing so, the guessed character was iterated throughout the word multiple times to ensure that each occurance of the letter was drawn out. 



