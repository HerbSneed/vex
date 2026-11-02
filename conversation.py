class Conversation:
    def __init__(self, id, topic = "New Chat", messages = None):
        self.id = id
        self.topic = topic
        
        if messages is None:
            self.messages = [
            ]
        else:
            self.messages = messages 