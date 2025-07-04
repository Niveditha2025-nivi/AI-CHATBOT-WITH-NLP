import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hey there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I’m CODTECH Chatbot created for internship Task-3."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great! How about you?"]
    ],
    [
        r"(.*) your name ?",
        ["I'm CODTECH Bot."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you please rephrase?"]
    ]
]


chatbot = Chat(pairs, reflections)

print("Hi! I’m your AI Chatbot. Type 'quit' to exit.")
chatbot.converse()
