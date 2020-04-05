"""
CP1404 Practical
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff",
                "AntiqueWhite": "#faebd7",
                "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4",
                "aquamarine4": "#458b74",
                "azure1": "#f0ffff",
                "azure4": "#838b8b",
                "black": "#000000",
                "BlueViolet": "#8a2be2"}

colour_name = input("Enter a colour name: ").upper()

while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ").upper()
