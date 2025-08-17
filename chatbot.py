import random
import datetime

# --- Response Generators ---
def get_greeting():
    return random.choice([
        "Hello! How are you doing?",
        "Hi there! Need any help?",
        f"{get_time_based_greeting()} How can I assist you?"
    ])

def get_farewell():
    return random.choice([
        "Goodbye! Take care.",
        "See you later!",
        "Bye! Have a wonderful day!"
    ])

def get_time_based_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning! "
    elif hour < 18:
        return "Good afternoon! "
    else:
        return "Good evening! "

def get_joke():
    return random.choice([
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why was the math book sad? Because it had too many problems.",
        "What do you call fake spaghetti? An impasta!"
    ])

# --- Main Chatbot ---
print("🤖 ChatBot 2.0 (type 'bye', 'quit' or 'exit' to end conversation)")

while True:
    user_input = input("You: ").lower()
    
    # Exit condition
    if user_input in ["bye", "quit", "exit"]:
        print("Bot:", get_farewell())
        break
        
    # Greetings
    elif any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
        print("Bot:", get_greeting())
        
    # Name questions
    elif "your name" in user_input:
        print("Bot: I'm ChatBuddy, your Python assistant!")
    elif "my name" in user_input:
        print("Bot: Sorry, I don't know your name. You can tell me if you like!")
    elif "name" in user_input:
        print("Bot: I'm not sure whose name you mean. Could you clarify?")
        
    # Time/date
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: It's currently {current_time} ")
    elif "date" in user_input:
        today = datetime.date.today().strftime("%B %d, %Y")
        print(f"Bot: Today is {today} ")
        
    # Time-based greetings
    elif any(phrase in user_input for phrase in ["good morning", "good afternoon", "good evening", "good night"]):
        print("Bot:", get_time_based_greeting())
        
    # Jokes
    elif "joke" in user_input:
        print("Bot:", get_joke())
        
    # Well-being
    elif "how are you" in user_input:
        print("Bot: I'm just a program, but I'm functioning perfectly! How about you?")
        
    # Gratitude
    elif "thank" in user_input:
        print("Bot: You're welcome! ")
        
    # Age (new addition)
    elif "old" in user_input or "age" in user_input:
        print("Bot: I was just created today! Brand new and ready to help.")
        
    # Fallback
    else:
        print("Bot: I'm still learning. Could you rephrase or ask something else?")