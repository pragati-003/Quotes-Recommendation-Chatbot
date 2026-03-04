import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


motivational_quotes = [
"Don't watch the clock; do what it does. Keep going. — Sam Levenson",
"Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
"Believe you can and you're halfway there. — Theodore Roosevelt"
]

inspirational_quotes = [
"Believe you can, and you're halfway there. — Theodore Roosevelt",
"The best way to get started is to quit talking and begin doing. — Walt Disney",
"Dream big and dare to fail. — Norman Vaughan"
]

success_quotes = [
"Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau",
"Opportunities don't happen. You create them. — Chris Grosser",
"Success is walking from failure to failure with no loss of enthusiasm. — Winston Churchill"
]

funny_quotes = [
"Why don’t programmers like nature? Too many bugs.",
"I would love to change the world, but they won’t give me the source code.",
"Debugging: Being the detective in a crime movie where you are also the murderer."
]


class ActionMotivationalQuote(Action):

    def name(self) -> Text:
        return "action_motivational_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        quote = random.choice(motivational_quotes)

        dispatcher.utter_message(text=f"Here's a motivational quote for you:\n{quote}")

        dispatcher.utter_message(text="Was this quote helpful? (yes/no)")

        return []


class ActionInspirationalQuote(Action):

    def name(self) -> Text:
        return "action_inspirational_quote"

    def run(self, dispatcher, tracker, domain):

        quote = random.choice(inspirational_quotes)

        dispatcher.utter_message(text=f"Here's an inspirational quote for you:\n{quote}")
        dispatcher.utter_message(text="Was this quote helpful? (yes/no)")

        return []


class ActionSuccessQuote(Action):

    def name(self):
        return "action_success_quote"

    def run(self, dispatcher, tracker, domain):

        quote = random.choice(success_quotes)

        dispatcher.utter_message(text=f"Here's a success quote for you:\n{quote}")
        dispatcher.utter_message(text="Was this quote helpful? (yes/no)")

        return []


class ActionFunnyQuote(Action):

    def name(self):
        return "action_funny_quote"

    def run(self, dispatcher, tracker, domain):

        quote = random.choice(funny_quotes)

        dispatcher.utter_message(text=f"Here's something funny 😄\n{quote}")
        dispatcher.utter_message(text="Was this quote helpful? (yes/no)")

        return []