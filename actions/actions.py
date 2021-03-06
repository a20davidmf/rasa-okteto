# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Text, Any, Dict, List

from random import Random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
        return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         numero = Random.randint(4)

         dispatcher.utter_message(text="Hello World! I'm using a action. This is the number: " + str(numero))
         return []
