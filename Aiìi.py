def respond(message):
    msg = message.lower().strip()
    if any(greet in msg for greet in ("hi", "hello", "hey")):
        return "Hello! How can I help you?"
    elif "weather" in msg:
        return "I can't check the weather right now, but it looks nice!"
    elif "time" in msg:
        from datetime import datetime
        return "Current time: " + datetime.now().strftime("%H:%M:%S")
    elif "bye" in msg or "exit" in msg or "quit" in msg:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand. Try asking about the weather or time."

if __name__ == "__main__":
    while True:
        user = input("You: ")
        reply = respond(user)
        print("AI:", reply)
        if reply == "Goodbye!":
            break
