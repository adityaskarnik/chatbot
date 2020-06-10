# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
class FetchMumbaiRestaurants(Action):

    def name(self) -> Text:
        return "fetch_mumbai_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class FetchPuneRestaurants(Action):

    def name(self) -> Text:
        return "fetch_pune_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class FetchBangaloreRestaurants(Action):

    def name(self) -> Text:
        return "fetch_bangalore_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        conn = sqlite3.connect('hotel_conn.db')
        data = conn.execute("SELECT * FROM HOTEL_INFO WHERE CITY = 'BANGALORE'")

        dispatcher.utter_message(text=data)

        return []
