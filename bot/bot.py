from datetime import datetime

def chatbot():
    print("🤖 Chatbot: Hello! I am SimpleBot.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("🤖 Chatbot: Bye! Have a great day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")

        elif "your name" in user_input:
            print("🤖 Chatbot: I am SimpleBot, a rule-based chatbot.")

        elif "who created you" in user_input:
            print("🤖 Chatbot: I was created using Python as a mini project.")

        elif "what can you do" in user_input:
            print("🤖 Chatbot: I can answer basic questions and chat with you.")

        elif "help" in user_input:
            print("🤖 Chatbot: You can ask me about my name, time, date, Python, or say hi!")

        elif "time" in user_input:
            print("🤖 Chatbot: Current time is", datetime.now().strftime("%H:%M:%S"))

        elif "date" in user_input:
            print("🤖 Chatbot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

        elif "what is python" in user_input:
            print("🤖 Chatbot: Python is a high-level programming language known for simplicity.")

        elif "purpose" in user_input:
            print("🤖 Chatbot: My purpose is to demonstrate how a basic chatbot works.")

        elif "thank" in user_input:
            print("🤖 Chatbot: You're welcome 😊")

        elif "bye" in user_input or "goodbye" in user_input:
            print("🤖 Chatbot: Goodbye! See you soon 👋")
            break

        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

chatbot()

