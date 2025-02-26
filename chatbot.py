import re
def chatbot():

    print("Chatbot:Hello! How can I help You?")
    print("Type'Exit'to end the chat.")

    while True:
        user_input =input("Me:").lower()

        if re.search(r"\b(hi|hello|hey)\b",user_input):
            print("Chatbot:Hello! How can i assist you?")
        elif re.search(r"\b(who are you|your name)\b",user_input):
            print("Chatbot:I'm Simple Chatbot!")
        elif re.search(r"\b(how are you|are you okay)\b",user_input):
            print("Chatbot:Im just a bot,But I'm doing well Because of my devloper,How about You?")
        elif re.search(r"\b(bye|see you soon|talk to you later|Exit|exit)\b", user_input):
            print("Chatbot:Goodbye! Have a great day :) ")
            break
        else:
            print("Chatbot:Sorry I didn't Understand that.")
chatbot()
