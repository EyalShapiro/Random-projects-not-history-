import pyautogui
image = pyautogui.screenshot()
image.save(r'C:\\Eyal\\Codes\\py\\Capture screen save\Screen.png')
image.show()
print(image)
image.close()
print('screen is save ')
