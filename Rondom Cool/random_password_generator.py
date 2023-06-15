import random

"""
יוצר סיסמות רנדומליות על פי ארוך שאת מכניס 

"""


def A_To_Z(start, end):
    """
    לדוגמה 
    start==a
    end==z
    return: "abcdefghijklmnopqrstuvwxyz"
    """

    char = start
    string = char
    while end != char:
        char = chr(ord(str(char))+1)
        string = string+""+char
    return string


def main():
    # הזן את אורך הסיסמה
    passlen = int(input("enter the length of password:\t"))
    A_Z = A_To_Z('A', 'Z')  # ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a_z = A_To_Z('a', 'z')  # ="abcdefghijklmnopqrstuvwxyz"
    א_ת = A_To_Z('א', 'ת')
    s = f"{A_Z}{a_z}{א_ת}01234567890!@#$%^&*()?"
    p = "".join(random.sample(s, passlen))
    print(p, '\n len cher:', len(p))


if __name__ == '__main__':
    main()
