from flask import Flask, render_template, request
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize Flask app
app = Flask(__name__)

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLP tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word.isalpha() and word not in stop_words]
    return " ".join(words)

# Chatbot logic with pattern matching
def chatbot_response(user_input):
    processed_text = preprocess_text(user_input)
    
    
    if re.search(r"\b(hi|hello|hey)\b", processed_text):
        return "Hello! How can I assist you?"
    elif re.search(r"\b(who are you|your name)\b", processed_text):
        return "I'm a simple chatbot here to assist you!"
    elif re.search(r"\b(how are you|how is it going)\b", processed_text):
        return "I'm doing well! What about you?"
    elif re.search(r"\b(weather|temperature)\b", processed_text):
        return "I can't check real-time weather yet, but I can help with other things!"
    elif re.search(r"\b(bye|exit|goodbye)\b", processed_text):
        return "Goodbye! Have a great day!"
    else:
        return "I'm still learning. Can you rephrase your question?"

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_text = request.args.get("msg")
    response = chatbot_response(user_text)
    if "goodbye" in response.lower():
     return response
    return response


if __name__ == "__main__":
    app.run(debug=True)
