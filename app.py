#!/usr /bin/env python3
from chat_v1 import chatV1, saveChat

listening = True
currentChat = []

while listening == True:
  user_req = ""
  num = int(input("1: New chat\n2: View past chats\n3: Quit\n"))
  if num == 1:
    print("What do you want to know?")
    knowledge = input()
    user_req = f"{knowledge}. I want a short summary unless stated otherwise.\n"
    chatV1(user_req, currentChat)
  elif num == 2:
    print("NOT COMPLETE")
  elif num == 3:
    print("Goodbye")
    saveChat(currentChat)
    listening = False
  else:
    print("Invalid Entry, please try again")