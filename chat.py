#!/usr /bin/env python3

def convo(userChoice):
  if userChoice == 1:
    print("What do you want to know?")
    knowledge = input()
    userReq = f"{knowledge}. I want a short summary unless stated otherwise.\n"
    return userReq
  elif userChoice == 2:
    return userChoice
  elif userChoice == 3:
    return userChoice
  else:
    return userChoice
    
    
def continueConvo(userChoice):
  if userChoice == 1:
    userReq = input("Enter text\n");
    return userReq
