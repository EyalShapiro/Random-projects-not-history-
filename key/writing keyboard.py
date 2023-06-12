"""
הקלד אוטומטי
ולחץ על המקלדת באופן אוטומטי
"""
import keyboard

keyboard.write("eyal\n")


keyboard.press_and_release('shift + r, shift + k, \n')
keyboard.press_and_release('R, e')

# it blocks until ctrl is pressed
keyboard.wait('Ctrl')
