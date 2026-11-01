#!/usr /bin/env python3

def mainMenu():
    num = 0
    num = int(input("1: New chat\n2: View past chats\n3: Quit\n"))
    return num


def subMenu():
    num = int(input("1: Continue conversation\n2: End chat\n"))
    return num