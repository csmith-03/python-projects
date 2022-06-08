##
## Name: Channing Smith
## bmi.py
##
## Purpose: The purpose of this program is to compute Body Mass Index,
# Ideal Body Weight, Lean Body Weight, and Body Surface Area.
##
## I ceritfy that this lab is entirely my own work, but I discussed it
## with Anthony Morrell.
##
## Input: The inputs will be the user's height in centimeters and
## weight in grams.
## Output: The program will return the user's Body Mass Index, Ideal
## Body Weight (men), Lean Body Weight (female), and Body Surface Area
## using the Mosteller, DuBois & DuBois, and Boyd formulas.

## This function will calculate your Body Mass Index, Ideal Body
## Weight(men), and Lean Body Weight (women).

import math
def calc_bsa():
    print("This function will calculate your Body Mass Index, Ideal"
        " Body Weight (men), Lean Body Weight (women), and BSA "
        "using three different formulas.")
    # user enters height in centimeters
    height= eval(input("Please enter your height in (cm):"))
    # user enters weight in kilograms
    weight= eval(input("Please enter your weight in (kg):"))

    # below calculates BMI
    body_mass_index = 10000 * weight / height ** 2
    # below calculates Ideal Body Weight
    ideal_body_weight = 50 + (2.3 * ((height / 2.54) - 60))
    # below calculates Lean Body Weight
    lean_body_weight = (1.07 * weight) - (148 * (weight ** 2 /
                                                 height ** 2))
    # below calculates BSA using Mosteller
    mosteller= math.sqrt((height * weight / 3600))
    # below calculates BSA using DuBois & DuBois
    du_bois= 0.20247 * ((height / 100) ** 0.725) * weight ** 0.425
    # below calculates BSA using Boyd formula
    boyd= 0.0003207 * (height ** 0.3) * ((1000 * weight) ** (0.6721 -
                                        0.0188 * math.log(weight,10)))

    # prints BMI and rounds
    print("Your Body Mass Index (BMI) is:" , round(body_mass_index
                                                       , 1) , "kg/m^2.")
    # prints Ideal Body Weight and rounds
    print("Your Ideal Body Weight (men) is:" ,
        round(ideal_body_weight , 2) , "kg.")
    # prints Lean Body Weight and rounds
    print("Your Lean Body Weight (women) is:" ,
        round(lean_body_weight , 2) , "kg.")
    # prints BSA using Mosteller formula
    print("Your calculated Body Surface Area using Mosteller is:" ,
        round(mosteller , 3) , "m^2.")
    # prints BSA using DuBois & DuBois formula
    print("Your calculated Body Surface Area using"
        " DuBois & DuBois formula is:" , round(du_bois , 3) , "m^2.")
    # prints BSA using Boyd formula
    print("Your calculated Body Surface Area using "
        "Boyd formula is:" , round(boyd , 3) , "m^2.")

def main():
    calc_bsa()

main()
