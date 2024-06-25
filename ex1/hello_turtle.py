#################################################################
# FILE : hello_turtle.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex1 2024
# DESCRIPTION: Practising functions definitions and functions calls utilizing turtle module
# STUDENTS I DISCUSSED THE EXERCISE WITH: Me, Myself & I.
# WEB PAGES I USED: none
# NOTES: ...
#################################################################

import turtle


def draw_triangle():
    """Parameterless function draws an equilateral triangle
     with side of 45 steps and angle of 60deg"""
    turtle.down()  # validation step
    turtle.forward(45)
    turtle.right(120)
    turtle.forward(45)
    turtle.right(120)
    turtle.forward(45)
    turtle.right(120)


def draw_sail():
    """Parameterless function draws a sail utilizing draw_triangle func """
    turtle.down()  # validation step
    """ Turn left from ship base, draw a sail must and turn on starting pos for triangle """
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    draw_triangle()

    """Coming to ship base part. """
    turtle.right(30)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)  # starting point angle


def draw_ship():
    """Parameterless function draws a ship utilizing draw_sail func"""
    turtle.down()  # validation step

    """Upper ship part"""
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)
    draw_sail()
    turtle.forward(50)

    """Lower ship part"""
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(180)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(120)  # starting point angle


def draw_fleet():
    """Parameterless function draws a fleet (hardcoded 2 ships) utilizing draw_ship func"""
    draw_ship()

    """Prep_Config steps to define 2 ship position relatively to the first ship"""
    turtle.up()
    turtle.left(180)
    turtle.forward(300)
    turtle.right(180)

    """Second Ship"""
    draw_ship()

    """Back to starting point"""
    turtle.up()
    turtle.forward(300)


if __name__ == '__main__':
    draw_fleet()
    turtle.done()
