import random
import re


class RuleBot:
    # Negative & exit responses
    negative_responses = ("no", "nope", "nah", "not really", "sorry")
    exit_commands = ("quit", "exit", "bye", "goodbye", "later")

    # Random starter questions
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do humans consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? "
    )

    def __init__(self):
        # Intent recognition using keyword/regex mapping
        self.intent_patterns = {
            "describe_planet": r"(planet|earth|world)",
            "answer_why": r"(why|reason|purpose)",
            "about_intellipaat": r"(intellipaat|course|training)",
            "about_music": r"(music|song|sing)"
        }

    def greet(self):
        self.name = input("What is your name? \n")
        response = input(
            f"Hi {self.name}, I am a rule-based chatbot. Will you help me learn about your planet?\n"
        ).lower()

        if response in self.negative_responses:
            print("Alright! Have a nice Earth day 👋")
            return

        self.chat()

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()

        while not self.check_exit(reply):
            reply = input(self.match_intent(reply)).lower()

    def check_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("It was nice talking to you. Goodbye 👋")
                return True
        return False

    def match_intent(self, reply):
        for intent, pattern in self.intent_patterns.items():
            if re.search(pattern, reply):
                if intent == "describe_planet":
                    return self.describe_planet()
                elif intent == "answer_why":
                    return self.answer_why()
                elif intent == "about_intellipaat":
                    return self.about_intellipaat()
                elif intent == "about_music":
                    return self.about_music()

        return self.no_match()

    # ----- Intent Responses -----

    def describe_planet(self):
        responses = (
            "Earth seems to be a beautiful planet full of life 🌍\n",
            "I have heard Earth has oceans, forests, and amazing biodiversity.\n"
        )
        return random.choice(responses)

    def answer_why(self):
        responses = (
            "I come in peace to learn about humans 👽\n",
            "I am here to collect information about your planet.\n",
            "Curiosity brought me here.\n"
        )
        return random.choice(responses)

    def about_intellipaat(self):
        responses = (
            "Intellipaat is a professional online education platform.\n",
            "Intellipaat helps people upskill and grow their careers.\n",
            "Intellipaat provides industry-focused training programs.\n"
        )
        return random.choice(responses)

    def about_music(self):
        responses = (
            "Music feels like a universal language 🎵\n",
            "Humans express emotions beautifully through music.\n",
            "Music seems to connect humans deeply.\n"
        )
        return random.choice(responses)

    def no_match(self):
        responses = (
            "Interesting. Can you tell me more?\n",
            "I see. Please elaborate.\n",
            "Why do you think that?\n",
            "That sounds fascinating.\n"
        )
        return random.choice(responses)


# Run the chatbot
if __name__ == "__main__":
    bot = RuleBot()
    bot.greet()
