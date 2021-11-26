#Amy Ollomani
#Final Project

import turtle
import random
wn = turtle.Screen()
tess = turtle.Turtle()

phraselst = [""]
phrase = random.choice(phraselst)



def character(n):
    tess.penup()
    tess.goto(-600,0)
    count = 0
    char1 = 0
    for char in n:
        if char!= " ":
            tess.pendown()
            tess.forward(80)
            tess.penup()
            tess.forward(80)
            if char1 == 7:
                tess.goto(-600,-150)
            if char1 ==15:
                tess.goto(-600,-300)
                
            char1+=1
        if char == " ":
            tess.forward(160)
            if char1 == 7:
                tess.goto(-600,-150)
            if char == 15:
                 tess.goto(-600,-300)
            char1+= 1

        

def error():
    n = 2


def pole():
    n = 3

def getword():
    n = 4


def main():
    pole()
    
n = "Hel looooooo"
character(n)
