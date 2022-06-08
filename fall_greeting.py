# Channing Smith
#
# fall_greeting.py
#
# Purpose: The purpose is to design a fall greeting card following the
# curriculum and guidelines of HW4.
#
# Certification of Authenticity:
# I certify that this greeting card homework is entirely my own work.
#
# Input: The user will be allowed to click to show a message and
# click to close the window.

# Output: The outputs will display a gorgeous turkey and a message.

from graphics import *

def main():
    # creates window
    win = GraphWin("My Greeting Card" , 800 , 800)
    # creates an orange color to use throughout program.
    good_orange = color_rgb(255, 69, 0)
    back_colors = ["red4" , "orange4" , "yellow4" , good_orange ,
                   "orange"]
    for i in (back_colors):
        win.setBackground(i)
        time.sleep(.3)

    # creates Text "Happy Thanksgiving!" and white message box
    message_box = Rectangle(Point(0, 740), Point(800, 660))
    message_box.setFill("white")
    message_box.draw(win)
    display_message = Text(Point(400 , 700) , "Click to display "
                                              "a message!")
    display_message.draw(win)
    print(display_message.getText())
    win.getMouse()
    display_message.undraw()

    message = Text(Point(400, 700) , "HAPPY THANKSGIVING!")
    message.draw(win)
    message.setStyle("bold")
    message.setTextColor("orange4")
    message.setSize(36)

    # creates feathers by cloning and moving each one after the other.
    # also uses Oval class
    feather1 = Oval(Point(300, 100) , Point(260 , 480))
    feather1.draw(win)
    feather1.setFill("red")
    feather2 = feather1.clone()
    feather2.move(40 , 20)
    feather2.setFill("orange4")
    feather2.draw(win)
    feather3 = feather2.clone()
    feather3.move(40, -20)
    feather3.setFill(good_orange)
    feather3.draw(win)
    feather4 = feather3.clone()
    feather4.move(40, 20)
    feather4.setFill("red")
    feather4.draw(win)
    feather5 = feather4.clone()
    feather5.move(40, -20)
    feather5.setFill("orange4")
    feather5.draw(win)
    feather6 = feather5.clone()
    feather6.move(40, 20)
    feather6.setFill(good_orange)
    feather6.draw(win)
    feather7 = feather6.clone()
    feather7.move(40, -20)
    feather7.setFill("red")
    feather7.draw(win)

    # creates body of turkey using Circle class
    body = Circle(Point(400, 400) , 150)
    body.setFill("red4")
    body.draw(win)

    # creates black buttons on body using Circle class
    button1 = Circle(Point(400, 400), 10)
    button1.setFill("black")
    button1.draw(win)
    button2 = button1.clone()
    button2.move(0 , 50)
    button2.draw(win)


    # creates head of turkey using Circle class
    head = Circle(Point(400, 270) ,  90)
    color = color_rgb(160,82,45)
    head.setFill(color)
    head.draw(win)

    # creates hat on turkey's head using Oval and Rectangle
    hat = Oval(Point(300 , 185) , Point(500 , 220))
    hat.setFill("black")
    hat.draw(win)
    hat_top = Rectangle(Point(350 , 140) , Point(450 , 210))
    hat_top.setFill("black")
    hat_top.draw(win)

    # creates legs using Rectangle class.
    legs = Rectangle(Point(340, 510), Point(350, 600))
    color_leg = color_rgb(255, 69, 0)
    legs.setFill(color_leg)
    legs.draw(win)
    legs2 = legs.clone()
    legs2.move(100, 0)
    legs2.draw(win)

    # creates toes of turkey using Rectangle class.
    toes = Rectangle(Point(320, 590) , Point(350 , 600))
    color_toes = color_rgb(255, 69, 0)
    toes.setFill(color_toes)
    toes.draw(win)
    toes2 = toes.clone()
    toes2.move(120 , 0)
    toes2.draw(win)

    # creates eyes of turkey using Circle
    c3 = Circle(Point(375, 260), 20)
    c3.draw(win)
    c3.setFill("white")

    # creates other eye of turkey using Circle
    c4 = Circle(Point(425, 260), 20)
    c4.draw(win)
    c4.setFill("white")

    # creates inside eye using Circle
    c5 = Circle(Point(375, 260), 10)
    c5.draw(win)
    c5.setFill("black")
    c6 = Circle(Point(425, 260), 10)
    c6.draw(win)
    c6.setFill("black")

    # creates orange nose of turkey using Polygon
    nose = Polygon([Point(375,280) , Point(425,280) , Point(400, 320)])
    nose.draw(win)
    nose.setFill("orange")

    # creates red gobble under turkey's neck using Oval.
    gobble = Oval(Point(390,305) , Point(410,370))
    gobble.draw(win)
    gobble.setFill("red")

    # creates line for text "Eat More Chicken" using Line class and Text
    aLine = Line(Point(160, 400) , Point(260 , 300))
    aLine.draw(win)
    message2 = Text(Point(150, 420), "Eat More Chicken!")
    message2.draw(win)
    message2.setFace("helvetica")
    message2.setTextColor("black")
    message2.setSize(20)

    # Exits greeting card and tells user where to click.
    message_box2 = Rectangle(Point(600, 100), Point(780, 150))
    message_box2.setFill("white")
    message_box2.draw(win)
    display_message2 = Text(Point(690, 125), "Click to close "
                                             "the window!")
    display_message2.draw(win)
    print(display_message2.getText())

    win.getMouse()
    win.close()

main()