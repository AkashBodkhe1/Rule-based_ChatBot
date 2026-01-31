import random
import re


class RuleBot:
    # Negative & exit responses
    negative_responses = ("no", "nope", "nah", "not really", "sorry")
    exit_commands = ("quit", "exit", "bye", "goodbye", "later")

    # Random starter questions (College Admission themed)
    random_questions = (
        "Which college are you planning to apply to? ",
        "What course or program are you interested in? ",
        "Have you started the admission process yet? ",
        "What factors matter most to you while selecting a college? ",
        "Are you preparing for any entrance examinations? "
    )

    def __init__(self):
        # Intent recognition using keyword/regex mapping
        self.intent_patterns = {
            "describe_planet": r"(college|campus|university)",
            "answer_why": r"(why|reason|purpose)",
            "about_intellipaat": r"(intellipaat|course|training)",
            "about_music": r"(music|song|sing)"
        }

    def greet(self):
        self.name = input("May I know your name?\n")
        response = input(
            f"Hello {self.name}! I am a college admission assistant chatbot. Would you like some guidance?\n"
        ).lower()

        if response in self.negative_responses:
            print("No problem. Wishing you the best for your future 😊")
            return

        self.chat()

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()

        while not self.check_exit(reply):
            reply = input(self.match_intent(reply)).lower()

    def check_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thank you for chatting. Best wishes for your admission journey 👋")
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
            "A good college offers a supportive learning environment and strong academic culture.\n",
            "Universities usually provide modern infrastructure, experienced faculty, and campus facilities.\n"
        )
        return random.choice(responses)

    def answer_why(self):
        responses = (
            "Choosing the right college helps shape both career and personal growth.\n",
            "A well-planned admission decision can open better opportunities in the future.\n",
            "Your choice of college plays an important role in your professional journey.\n"
        )
        return random.choice(responses)

    def about_intellipaat(self):
        responses = (
            "Intellipaat provides industry-focused training programs for skill development.\n",
            "It helps students and professionals upskill for better career opportunities.\n",
            "Intellipaat offers guided learning in various technical domains.\n"
        )
        return random.choice(responses)

    def about_music(self):
        responses = (
            "Many colleges encourage cultural activities like music and arts.\n",
            "Participating in music clubs can enhance creativity and confidence.\n",
            "Music and extracurricular activities help maintain a balanced college life.\n"
        )
        return random.choice(responses)

    def no_match(self):
        responses = (
            "Could you please provide more details?\n",
            "That sounds interesting. Can you explain a bit more?\n",
            "I would like to understand your admission preferences better.\n",
            "Please share more information.\n"
        )
        return random.choice(responses)


# Run the chatbot
if __name__ == "__main__":
    bot = RuleBot()
    bot.greet()
