#!/usr /bin/env python3
from ollama import chat
from ollama import ChatResponse

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