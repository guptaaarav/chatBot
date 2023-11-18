import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"My name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"What is your name?",
        ["I am Aarav's chatbot.",]
    ],
    [
        r"How are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (good|great|fine)",
        ["That's wonderful to hear!",]
    ],
    [
        r"bye",
        ["Goodbye! Take care.", "Bye! Have a great day."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?",]
    ]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

def run_chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download('punkt')  # Download necessary data for nltk
    run_chatbot()
