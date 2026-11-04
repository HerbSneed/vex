#!/usr /bin/env python3
from chat_history import load_conversations

def mainMenu():
    userChoice = 0
    print("\n1: New chat\n2: View past chats\n3: Quit")
    userChoice = int(input("Select an option: "))
    return userChoice


def subMenu():
    userChoice = int(input("1: Continue conversation\n2: End chat\n"))
    return userChoice

def pastChatsMenu():
    pastChats = load_conversations()
    print("\nUSER PAST CHATS")
    for chat in pastChats.items():
        print(f"{int(chat[0]) +1 }: {chat[1].topic}")
    print("0: Return to previous menu")
    userChoice = int(input("Select a previous chat: "))
    return userChoice - 1
        