
import datetime

print("===== WELCOME TO CHATBOT =====")
print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: You can ask me simple questions.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How are you?")

    elif user == "how are you":
        print("Chatbot: I am doing great! How about you?")

    elif user == "what is your name":
        print("Chatbot: I am Python Chatbot.")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Chatbot: Current time is", current_time)

    elif user == "date":
        current_date = datetime.date.today()
        print("Chatbot: Today's date is", current_date)

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
