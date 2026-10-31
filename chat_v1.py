#!/usr /bin/env python3
from ollama import chat
from ollama import ChatResponse
import json
import datetime

now = datetime.datetime.now()


def chatV1(string, chatList):
  chatList.append(string)
  result = " ".join(chatList)
  response: ChatResponse = chat(
    model='qwen3:8b',
    messages=[
      {
        'role': 'user',
        'content': result,
      },
    ],
  )
  chatList.append(response.message.content)
  print(response['message']['content'])
  current_reply = response['message']['content']
  return chatList


def saveChat(current):
  
  data = {
    "id": 0,
    "topic": current[0],  
    "conversation": current
  }
  
  
  with open("conversations.json", "a", encoding="utf-8") as file:
    json.dump(
      data, file, indent=4
    )  
   
    
  
  