import pyautogui
import os
# ניתב מיקום קובץ לדוגמא "/home/User/Desktop/"
path_Screen = os.path.split(os.path.abspath(__file__))[0]+r'\Screen.png'
print(path_Screen)

def main():
    image = pyautogui.screenshot(imageFilename=path_Screen)
    image.save(path_Screen)  # שמור את תמונה לםי מיקום
    image.show()  # פותח את תוכנה של תמונה
    print(image)
    image.close()
    print('screen is save ')


if __name__ == '__main__':
    main()
