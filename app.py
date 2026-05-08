from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(message):
    message = message.lower()
    
    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"
    
    elif any(word in message for word in ["how are you", "how r u"]):
        return "I'm doing great, thanks for asking! How about you?"
    
    elif any(word in message for word in ["your name", "who are you"]):
        return "I'm AIChatbot, built by Emmanuel using Python and Flask!"
    
    elif any(word in message for word in ["weather"]):
        return "I can't check live weather yet, but that's a feature coming soon!"
    
    elif any(word in message for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"
    
    elif any(word in message for word in ["help"]):
        return "I can answer basic questions. Try asking my name or saying hello!"
    
    elif any(word in message for word in ["python"]):
        return "Python is an amazing language! I was actually built with Python and Flask."
    
    elif any(word in message for word in ["dublin", "ireland"]):
        return "Dublin is a great tech hub! Google, Meta, and Microsoft all have offices there."
    
    else:
        return "That's an interesting question! I'm still learning. Try asking me something else."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)