def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm working fine!"
    elif "name" in user_input:
        return "I'm your Python chatbot 🤖"
    else:
        return "I didn't understand that."

print("Chatbot started! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Bye!")
        break

    reply = chatbot_response(user_input)
    print("Chatbot:", reply)
