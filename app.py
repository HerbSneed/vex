#!/usr /bin/env python3
from menu import *
from ollama_client import chatV1
from chat_history import saveConvo, load_conversations, createNewConversation, loadPastChat

listening = True
userReq = ""
inProgress = False

conversations = load_conversations()

while listening == True:
  userChoice = mainMenu()
  if userChoice == 1:
    conversation = createNewConversation(conversations)
    userReq = (input("Let's get started! What would you like to know?\n"))
    chatV1(userReq, conversation)
    inProgress = True
    while inProgress == True:
      subChoice = subMenu()
      if subChoice == 1:
        userReq = input("Enter text: ");
        chatV1(userReq, conversation)
      elif subChoice == 2:
        saveConvo(conversations)
        break
  elif userChoice == 2:
      pastChatChoice = pastChatsMenu()
      if pastChatChoice == -1:
        pass
      else:
        pastContent = loadPastChat(pastChatChoice, conversations)
        newUserReg = input("Enter text: ")
        chatV1(newUserReg, pastContent)
        inConvo = True
        while inConvo:
          subChoice = subMenu()
          if subChoice == 1:
            userReq = input("Enter text: ");
            chatV1(userReq, pastContent)
          elif subChoice == 2:
            saveConvo(conversations)
            inConvo = False
  elif userChoice == 3:
    listening = False
    print("Goodbye")
    break
  else:
    print("Invalid Entry, please try again")
      

  

