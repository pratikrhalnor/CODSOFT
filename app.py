from flask import Flask, render_template, request
import re

app = Flask(_name_)

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I assist you?"
    elif re.search(r"\b(who are you|your name)\b", user_input):
        return "I'm a simple chatbot!"
    elif re.search(r"\b(how are you|are you okay)\b", user_input):
        return "I'm just a bot, but I'm doing well. How about you?"
    elif re.search(r"\b(bye|see you soon|talk to you later|exit)\b", user_input):
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_text = request.args.get("msg")
    return chatbot_response(user_text)

if __name__ == "_main_":
    app.run(debug=True)