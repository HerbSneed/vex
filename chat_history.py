#!/usr /bin/env python3
import json
import os
from conversation import Conversation
from util import timestamp

currentTime = timestamp()

def load_conversations():
    if os.path.exists("conversations.json"):
        with open("conversations.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = {}
        
    conversations = {}

    for ID, conversation_data in data.items():
        conversations[ID] = Conversation(
            id = conversation_data["id"],
            created= conversation_data["created"],
            topic = conversation_data["topic"],
            messages = conversation_data["content"]
        ) 
    
    return conversations

def loadPastChat(userChoice, conversations):
    for conversation in conversations.items():
        if userChoice == int(conversation[0]):
            pastContent = conversation[1]
            for i in pastContent.messages:
                print(f"{i['role']}\n{i['content']}\n")
    return pastContent

def createNewConversation(conversations):
    id = len(conversations)
    conversation = Conversation(id=id, created=currentTime, topic="New Topic");
    conversations[id] = conversation
    return conversation

def convertConvoToDict(conversation):
    return {
        "id": conversation.id,
        "created": conversation.created,
        "topic": conversation.topic,
        "content": conversation.messages
    }
    
def saveConvo(conversations):
    data = {}
    for ID, conversation in conversations.items():        
        data[ID] = convertConvoToDict(conversation)

    with open("conversations.json", "w", encoding="utf-8") as file:
        json.dump(
        data, file, indent=4
        )       
        
    with open("conversations.json", "r") as file:
        data = json.load(file)
        data[str(ID)]
        
      