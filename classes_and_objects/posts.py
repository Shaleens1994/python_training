class Post:
   def __init__(self,messages,author):
        self.messages = messages
        self.author= author
   def new_message(self, new_message):
       self.messages = new_message

   def display_message(self):
       print(f"Latest message is {self.messages}")







