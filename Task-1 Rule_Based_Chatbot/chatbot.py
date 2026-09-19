import re
from datetime import datetime

BOT_NAME = "RuleBot"

RULES = [
    (
        r"\b(hi|hello|hey|namaste)\b",
        "Hello! How can I help you?"
    ),

    (
        r"\bhow are you\b",
        "I'm doing great! Thanks for asking."
    ),

    (
        r"\b(your name|who are you)\b",
        f"My name is {BOT_NAME}. I am a rule-based chatbot."
    ),

    (
        r"\b(help|what can you do)\b",
        "I can respond to greetings, tell you the date and time, "
        "and answer some basic questions."
    ),

    (
        r"\b(time|current time)\b",
        f"The current time is {datetime.now().strftime('%I:%M %p')}."
    ),

    (
        r"\b(date|today|today's date)\b",
        f"Today's date is {datetime.now().strftime('%d %B %Y')}."
    ),

    (
        r"\b(thank you|thanks)\b",
        "You're welcome! Happy to help."
    ),

    (
        r"\b(bye|goodbye|exit|quit)\b",
        "Goodbye! Have a great day!"
    )
]


def get_response(user_input):
    text = user_input.lower().strip()

    for pattern, response in RULES:
        if re.search(pattern, text):
            return response

    return (
        "Sorry, I don't understand that yet. "
        "Try asking for help, the time, or today's date."
    )


def main():

    print("=" * 50)
    print("              RULE-BASED CHATBOT")
    print("=" * 50)

    print("Hello! I am RuleBot.")
    print("Type 'bye' to exit.")
    print()

    while True:

        user_input = input("You: ")

        if not user_input.strip():
            print("RuleBot: Please type something.")
            continue

        response = get_response(user_input)

        print("RuleBot:", response)

        if re.search(
            r"\b(bye|goodbye|exit|quit)\b",
            user_input.lower()
        ):
            break


if __name__ == "__main__":
    main()