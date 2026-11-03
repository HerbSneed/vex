#!/usr /bin/env python3
from chat_history import load_conversations

def mainMenu():
    userChoice = 0
    userChoice = int(input("1: New chat\n2: View past chats\n3: Quit\n"))
    return userChoice


def subMenu():
    num = int(input("1: Continue conversation\n2: End chat\n"))
    return num

def pastChatsMenu():
    pastChats = load_conversations()
    print("\nUSER PAST CHATS")
    for chat in pastChats.items():
        print(f"{int(chat[0]) +1 }: {chat[1].topic}")
    userChoice = int(input("Select a previous chat: "))
    return userChoice - 1
        