# MAYBE PUT C.AI IMPORT HERE?

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Scharle Boiling Point", color=#f00)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # we can ignore sprite for now but like JUST GET ME THE PROMPT

    show eileen happy

    # These display lines of dialogue.

    s "You're not supposed to be here."

    "august 12, 2036,,, the heatdeath of the universe.."

    # This ends the game.

    return
