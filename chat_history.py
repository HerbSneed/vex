#!/usr /bin/env python3
import json
import datetime
import os
from conversation import Conversation

now = datetime.datetime.now()

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
            topic = conversation_data["topic"],
            messages = conversation_data["content"]
        ) 
    
    return conversations

def createNewConversation(conversations):
    id = len(conversations)
    conversation = Conversation(id=id, topic="New Top");
    conversations[id] = conversation
    return conversation

def convertConvoToDict(conversation):
    return {
        "id": conversation.id,
        "topic": conversation.topic,
        "content": conversation.messages
    }
    
def saveConvo():
    data = {}
    for ID, conversation in conversation.items():        
        data[ID] = convertConvoToDict(conversation)

    with open("conversations.json", "w", encoding="utf-8") as file:
        json.dump(
        data, file, indent=4
        )       
        
    with open("conversations.json", "r") as file:
        conversation = json.load(file)
        conversation[id]
        
      