from datetime import datetime
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = None


spy = Spy('nirav', 'Ms.', 22, 4.9)

f1 = Spy('isha', 'Ms.', 19,4.7)
f2 = Spy('mahi', 'Mr.', 17,4.8)
f3 = Spy('misha', 'Ms.', 16,4.5)

friends = [f1, f2, f3]

class chat_message:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
