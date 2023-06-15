import random
"""
תחרות ניכוש מספרים עם החבר הכי טוב שלך 
המחשב שלך 
"""


def Guess_num(num):
    """
    הפעולה מקבלת מספר כדי
    וצריך לכניס מספרים לנסות לנחש את תשובה יש 3 ניסונות לנחש 
    ומחזיר אם ניצחת או לא
    """
    for i in range(0, 3):
        user = int(input("guess the number:"))
        if user == num:
            print("Hurray!!")
            print(f"you guessed the number right it's {num}")
            break
    if user != num:
        print(f"Your guess is incorrect the number is {num}")


def main():
    num = random.randint(1, 10)
    Guess_num(num)


if __name__ == '__main__':
    main()
