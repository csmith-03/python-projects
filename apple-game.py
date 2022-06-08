# Channing Smith
#
# hw7.py
#
# Purpose: The purpose is to design a game based off the criteria for
# this homework.
#
# Certification of Authenticity:
# I certify that this homework is entirely my own work, but I received
# help from the Tutoring Center.
#
# Input: The user will be able to click when the apples fall and try to
# land them in the basket.

# Output: The output will display the final score and an output message
# to close the window.
import math
import random
from graphics import *


def creating_window():
    """ Creates window for graphics
        Argument: N/A
        Return: win """
    win = GraphWin("Apple Catcher" , 800 , 800)
    win.setBackground("green")
    return win


def overlap(cir1 , cir2):
    """ Determines if there is overlap between apple and basket.
        Argument: cir1 , cir2
        Return: True if touching, False if not in range """
    distance = math.sqrt((cir1.getCenter().getX() -
                          cir2.getCenter().getX()) ** 2 + (
            cir1.getCenter().getY() - cir2.getCenter().getY()) ** 2)
    if cir1.getRadius() + cir2.getRadius() >= distance:
        return True
    else:
        return False

def hit_floor(cir , win):
    """ Determines if the apple has hit the bottom.
        Argument: cir , win
        Return: True if y value is greater than window
        minus radius of circle. """
    # get Y value for Circle
    win = 800
    center_circle = cir.getCenter()
    y_point = center_circle.getY()
    if y_point > win - cir.getRadius():
        return True
    return False


def hit_wall(cir , win):
    # get X value for circle
    """ Determines if the circle hits the wall.
        Argument: cir , win
        Return: True if x value is less than cir radius or x
        value is greater than window. """
    center_circle = cir.getCenter()
    x_point = center_circle.getX()
    if x_point < cir.getRadius() or x_point > 800 - \
            cir.getRadius():
        return True
    return False

def create_cart(win , radius , height):
    """ Creates the cart with random for the apples to fall into.
        Argument: win, radius , height
        Return: cart_cir """
    cart_cir = Circle(Point(random.randint(radius , 800 -
                                           radius) , height) , radius)
    cart_cir.setFill("yellow4")
    cart_cir.draw(win)
    return cart_cir


def create_apple(win , radius , min_height):
    """ Creates apple at random position
        Argument: win , radius , min_height
        Return: apple_cir """
    apple_cir = Circle(Point(random.randint(0, 800),
                             random.randint(0 , min_height)), radius)
    apple_cir.setFill("red")
    apple_cir.draw(win)
    return apple_cir

def apple_clicked(apple , pt):
    """ Determines if the apple(s) have been clicked.
        Argument: apple , pt (point)
        Return: True if apple has been clicked, False if not """
    if pt.getX() > apple.getCenter().getX() - \
            apple.getRadius() and pt.getX() < apple.getCenter().getX() \
            + apple.getRadius():
        if pt.getY() > apple.getCenter().getY() - apple.getRadius() \
                and pt.getY() < apple.getCenter().getY() + \
                apple.getRadius():
            return True
    return False

def main():
    # creates window
    win = creating_window()

    # creates name of game and rectangle underneath
    name_game = Text(Point(400 , 100) , "APPLE CATCHER")
    name_game.setOutline('red')
    name_game.setSize(36)
    name_game.setStyle('bold')
    name_box = Rectangle(Point(0 , 50) , Point(800 , 150))
    name_box.setFill("white")
    name_box.draw(win)
    name_game.draw(win)


    # creates start text and box under the text.
    start_text = Text(Point(400 , 400) , "Try to drop the apples in the "
                                         "basket.\n Click to start!")
    start_text.setSize(20)
    start_box = Rectangle(Point(0 , 350) , Point(800 , 450))
    start_box.setFill("white")
    start_box.draw(win)
    start_text.draw(win)
    win.getMouse()
    start_box.undraw()
    start_text.undraw()
    name_game.undraw()
    name_box.undraw()

    # creates the cart
    cart_circle = create_cart(win , 100 , 700)
    # list of apples to create
    apples = [create_apple(win, 75, 400), create_apple(win, 75, 400),
              create_apple(win, 75, 400), create_apple(win, 75, 400),
              create_apple(win, 75, 400)]
    # list of apples clicked
    click = [False, False, False, False, False]
    # undrawn apples keeps up with app the apples that have either
    # dropped into the basket or hit the bottom.
    undrawn_apples = [False, False, False, False, False]



    # velocity of x and y to control speed of cart.
    x_velocity = 10
    y_velocity = 10

    # initialize count as zero.
    count = 0

    # creates the text box for count and rectangle underneath text.
    count_rect = Rectangle(Point(20 , 50) , Point(225 , 150))
    count_rect.setFill("white")
    count_text = Text(Point(125, 100), "Count = 0")
    count_text.setSize(25)
    count_rect.draw(win)
    count_text.draw(win)

    # while loop that moves cart and reverses the direction
    # when it hits the wall.
    while undrawn_apples[0] == False or undrawn_apples[1] == False or \
            undrawn_apples[2] == False or undrawn_apples[3] == \
            False or undrawn_apples[4] == False:
        point = win.checkMouse()
        cart_circle.move(x_velocity , 0)
        if hit_wall(cart_circle , win):
            x_velocity *= -1

        # loop for the apples and if overlap occurs, undraw apple
        # and move off screen, also add to count.
        for j in range(5):
            if overlap(apples[j], cart_circle):
                apples[j].undraw()
                undrawn_apples[j] = True
                apples[j].move(880 , 880)
                count += 1
                count_text.setText("Count = " + str(count))

            # moves apples based on if they are clicked/ hit floor
            if point != None and not click[j]:
                click[j] = apple_clicked(apples[j] , point)
            if click[j]:
                apples[j].move(0 , y_velocity)
                if hit_floor(apples[j] , win):
                    apples[j].undraw()
                    undrawn_apples[j] = True

    # undraw the cart circle before displaying end text
    cart_circle.undraw()

    # displays end text and rectangle behind the text.
    end_box = Rectangle(Point(0 , 350) , Point(800 , 450))
    end_text = Text(Point(400, 400), "GAME OVER\n Click to end.")
    end_text.setOutline("red")
    end_text.setStyle('bold')
    end_text.setSize(30)
    end_box.setFill("white")
    end_box.draw(win)
    end_text.draw(win)

    # displays final score.
    count_text.setText("Final score = " + str(count) + "/" + "5")
    win.getMouse()
main()