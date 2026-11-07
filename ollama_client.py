#!/usr /bin/env python3
from ollama import chat
from ollama import ChatResponse
from util import timestamp

currentTime = timestamp()

def chatV1(string, conversation):
  SYSTEM_PROMPT = "Your name is Vex, you are my personal AI. My name is Herbie Sneed, people call me Herb or Morlique.  When I make a request I want short direct answers no more than 50 word unless stated otherwise."
  if conversation.topic == "New Topic":
    conversation.topic = string
  
  conversation.messages.append({
    "role": "USER",
    "timestamp": currentTime,
    "content": string
  })
  
  response: ChatResponse = chat(
    model='qwen3:8b',
    messages=[
      {
        "role": "system",
        "content": SYSTEM_PROMPT
      },
      
        *conversation.messages
    ],
  )
  conversation.messages.append({
    "role": "VEX",
    "content": response.message.content
  })
  print("\n")
  print(response['message']['content'])
  print("\n")
  return conversation