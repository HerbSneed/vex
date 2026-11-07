class Conversation:
    def __init__(self, id, created, topic = "New Chat", messages = None):
        self.id = id
        self.created = created 
        self.topic = topic
        if messages is None:
            self.messages = [
            ]
        else:
            self.messages = messages 
            
    def getMessages(self):
        return self.messages