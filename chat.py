#!/usr /bin/env python3

def convo(userChoice):
  if userChoice == 1:
    print("What do you want to know?")
    userReq = input()
    return userReq
  elif userChoice == 2:
    return userChoice
  elif userChoice == 3:
    return userChoice
  else:
    return userChoice
    
    
def continueConvo(userChoice):
  if userChoice == 1:
    userReq = input("Enter text: \n");
    return userReq
