print("Welcome to VIT Smart Chatbot!")
print("Type 'exit' to quit\n")

import random
import time

name = ""
greetings = ["Hello!", "Hey!", "Hi there!","Hi!"]
while True:
    user = input("You: ").lower()

    #ending Program
    if user == "exit":
        print("Bot: Bye", name if name else "",)
        break

    # Ask name
    elif "my name is" in user:
        name = user.replace("my name is" , "").strip()
        print(f"Bot: Nice to meet you, {name}!")

    # Greeting
    elif any(word in user for word in ["hi", "hello", "hey"]):
        print("Bot:", random.choice(greetings), name if name else "")

    # Fees
    elif "fees" in user:
        print("Bot: Fees for B.Tech depends on category.")  
        category = int(input("Enter the category (1-4) for the fees you want to know: "))
        if category == 1:
            print("Fees is around ₹2,00,000")
        elif category == 2:
            print("Fees is around ₹3,00,000")
        elif category == 3:
            print("Fees is around ₹4,00,000")
        elif category == 4:
            print("Fees is around ₹5,00,000")
        else:
            print("Invalid category")

    # Hostel
    elif "hostel" in user:
        print("Bot: Hostel available (AC/Non-AC). Very comfortable!")

    # Courses
    elif "course" in user:
        print("Bot: B.Tech, M.Tech, MBA, MCA and more!")

    # Placement
    elif "placement" in user:
        print("Bot: Great placements with top companies!")

    # Time feature
    elif "time" in user:
        print("Bot: Current time is:", time.strftime("%H:%M:%S"))

    # Simple calculator
    elif "calculate" in user:
        try:
            expr = user.replace("calculate", "")
            result = eval(expr)
            print("Bot: Answer is:", result)
        except:
            print("Bot: Invalid calculation!")

    # Fun responses
    elif "how are you" in user:
        print("Bot: I'm just code, but I'm feeling awesome ")

    else:
        print("Bot: I don't understand. Try asking about fees, hostel, joke, or time!")
