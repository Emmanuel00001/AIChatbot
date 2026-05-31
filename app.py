from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

import os
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

conversation_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    
    data = request.json
    user_message = data.get("message")
    is_new_chat = data.get("newChat", False)
    
    if is_new_chat:
        conversation_history = []
        return jsonify({"response": "New conversation started. How can I help you?"})
    
    conversation_history.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=conversation_history
        )
        
        bot_response = response.text
        
        conversation_history.append({
            "role": "model",
            "parts": [{"text": bot_response}]
        })
        
        return jsonify({"response": bot_response})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, I encountered an error. Please try again."})

if __name__ == "__main__":
    app.run(debug=True)