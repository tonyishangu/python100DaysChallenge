print('Welome to treasure island.\nYour mission is to find the treasure.')
print('You are at a junction which side do you go left or right?')
side = input('Right or Left\n')
lower_text = side.lower()
if lower_text == 'left':
    print('Do you chose to swim or wait for the boat remember time is ticking')
    move = input('Swim or Boat\n')
    lower_move = move.lower()
    if lower_move == 'boat':
        print('Which door do you choose Red, Blue or Yellow')
        color = input('Red, Blue or Yellow\n')
        lower_color = color.lower()
        if lower_color == 'yellow':
            print('Lucky you. You found the treasure. Too bad for the others init')
        elif lower_color == 'blue':
            print("You dead I knew you would think blue is the mostlikely one. Guess What it ain't")
        elif lower_color == 'red':
            print("Who tf opens the red door. Naah never come back again even in the afterlife cause that's where you are going.")
        else:
            print("English ain't that hard")
    elif lower_move == 'swim':
        print("Stop being white. You think sharks are friendly. Yeah you dead game over!!")
    else:
        print("English ain't that hard")
elif lower_text == 'right':
    print('Yeah the right side is not it. You dead and game over!!')
else:
    print("English ain't that hard")