
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

def nexus_ai(message):
    text = message.lower().strip()
    
    if "eman ur rehman" in text or "eman ur rehman" in text:
        import random

        roasts = [
            "Eman has entered the chat. Even the loading screen needs a break! 😂",
            "NEXUS AI detected extra drama in the system. 😂",
            "Warning: Eman mode activated. Sarcasm levels rising!",
            "Eman doesn't need a spotlight. The drama brings its own lighting!",
            "NEXUS AI recommends a coffee break for this much main-character energy! ☕",
            "Plot twist: Eman is the reason the notification bell never rests!",
            "Even the Wi-Fi needs a moment to process this much energy!"
        ]

        return random.choice(roasts)


    if any(x in text for x in ["hello", "hi", "salam"]):
        return "Welcome to NEXUS AI! How can I help?"

    if "who are you" in text:
        return "I am NEXUS AI, your digital assistant."

    if "python" in text:
        return "Python is a powerful programming language."

    if "science" in text:
        return "Science explains the world through experiments and evidence."

    if "urdu" in text:
        return "میں NEXUS AI ہوں۔ آپ کیسے ہیں؟"

    return (
        "NEXUS AI DEMO: I received your message: "
        + message
        + ". Real AI connectivity will be added soon."
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()

    if not message:
        return jsonify({"error": "Enter a message"}), 400

    if len(message) > 4000:
        return jsonify({"error": "Message too long"}), 400

    return jsonify({
        "reply": nexus_ai(message),
        "mode": "DEMO MODE"
    })

@app.route("/status")
def status():
    return jsonify({
        "name": "NEXUS AI",
        "status": "online",
        "mode": "DEMO MODE"
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
