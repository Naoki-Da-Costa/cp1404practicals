"""
CP1404/CP5632 Practical
Find hex code by name
"""

COLOUR_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "#ffebcd"
                 , "blue1": "#0000ff", "brown": "#a52a2a"}

COLOUR = input("Colour? ")
while COLOUR != "":
    if COLOUR in COLOUR_TO_HEX:
        print(COLOUR_TO_HEX[COLOUR])
        COLOUR = input("Colour? ")
    else:
        print("Invalid colour")
        COLOUR = input("Colour? ")
