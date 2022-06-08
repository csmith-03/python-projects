# Channing Smith
#
# morse_code.py
#
# The purpose of this program is to design a program that translates to
# Morse Code using the graphics package.
#
# Certification of Authenticity:
# I certify that this greeting card homework is entirely my own work,
# but I received help from the Tutoring Center.
#
# Input: The user will input a string into the graphics window.
#
# Output: The output will display the Morse Code based on the string
# the user inputs.

from graphics import *

def making_window():
    # draw window and set background color
    win = GraphWin("Morse Code" , 800 , 800)
    win.setBackground("grey")

    # creates entry box for user to input a string
    inputBox = Entry(Point(450, 200), 50)
    inputBox.setFill("yellow")
    inputBox.draw(win)

    # creates the message "Message To Code"
    message = Text(Point(200, 200), "Message To Code:")
    message.draw(win)

    # creates encode button for user to click when done typing the
    # string they are entering.
    encode_button = Rectangle(Point(350, 350), Point(500, 300))
    encode_button.draw(win)
    encode_text = Text(Point(425, 325), "Encode")
    encode_text.draw(win)
    win.getMouse()
    encode_button.undraw()
    encode_text.undraw()

    # "message" is used in the loop to grab the text and "message2"
    # makes the message uppercase.
    message = inputBox.getText()
    message2 = message.upper()

    # inserting alphabet and morse code as a list to refer
    # back to in the loop.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                  '....', '..', '.---', '-.-', '.-..', '--', '-.',
                  '---', '.--.', '--.-', '.-.', '...', '-', '..-',
                  '...-', '.--', '-..-', '-.--', '--..']

    # set an empty string with spaces for the morse code.
    word_decode = " "
    for i in message2:
        # creates an index to find the letter in the alphabet
        index_alphabet = alphabet.find(i)
        # word_decode adds the morse code to the empty string
        word_decode += morse_code[index_alphabet]
        # the index is the morse code translated from the string
        # the user inputs. Also sets size and color of the morse code
        # to display to.
    index = Text(Point(400, 400), word_decode)
    index.setSize(35)
    index.setFill("yellow")
    index.draw(win)

    # the result message displays above the morse code in black color
    result_message = Text(Point(400 , 350), "Resulting Message:")
    result_message.setFill("black")
    result_message.draw(win)

    # creates the exit text "Click to close"
    exit_text = Text(Point(400, 500), "Click anywhere to close the "
                                      "window.")
    exit_text.setTextColor("black")
    exit_text.draw(win)
    win.getMouse()
    win.close()



def main():
    making_window()
main()