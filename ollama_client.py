#!/usr /bin/env python3
from ollama import chat
from ollama import ChatResponse

def chatV1(string, conversation):
  SYSTEM_PROMPT = "Your name is Vex, you are my personal AI. My name is Herbie Sneed, people call me Herb or Morlique.  When I make a request I want short direct answers no more than 50 word unless stated otherwise."
  if conversation.topic == "New Topic":
    conversation.topic = string
  
  conversation.messages.append({
    "role": "user",
    "content": string
  })
  
  print(conversation.messages)
  # result = " ".join(conversation.messages.content)
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
    "role": "assistant",
    "content": response.message.content
  })
  print(conversation)
  print(response['message']['content'])
  return conversation