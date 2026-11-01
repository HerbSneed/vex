#!/usr /bin/env python3
from chat import convo, continueConvo
from menu import mainMenu, subMenu
from ollama_client import chatV1
from chat_history import saveConvo, load_conversations, createNewConversation


listening = True
currentChat = []
userReq = ""
inProgress = False

conversations = load_conversations()

while listening == True:
  userChoice = mainMenu()
  if userChoice == 1:
    conversation = createNewConversation(conversations)
    userReq = convo(userChoice)
    chatV1(userReq, currentChat)
    inProgress = True
    while inProgress == True:
      subChoice = subMenu()
      if subChoice == 1:
        userReq = continueConvo(subChoice)
        chatV1(userReq, currentChat)
      elif subChoice == 2:
        saveConvo(currentChat)
        userChoice = mainMenu()
  elif userChoice == 2:
    pass
  elif userChoice == 3:
    listening = False
    print("Goodbye")
    break
  else:
    print("Invalid Entry, please try again")
      

  

