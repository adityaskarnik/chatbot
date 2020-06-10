# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

class FetchMumbaiRestaurants(Action):

    def name(self) -> Text:
        return "fetch_mumbai_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            restaurant = str((tracker.latest_message)['text']).split("Provide me Menu of")[1].strip()
            import sqlite3
            conn = sqlite3.connect('hotel_conn.db')
            data = conn.execute("SELECT FOOD_ITEM, PRICE FROM HOTEL_INFO WHERE RESTAURANTS='" + restaurant +"'")
            print("DATA",data, type(data))
            for i in data:
                dispatcher.utter_message(text=str(i))

            return []

class FetchPuneRestaurants(Action):

    def name(self) -> Text:
        return "fetch_pune_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            restaurant = str((tracker.latest_message)['text']).split("Provide me Menu of")[1].strip()
            import sqlite3
            conn = sqlite3.connect('hotel_conn.db')
            data = conn.execute("SELECT FOOD_ITEM, PRICE FROM HOTEL_INFO WHERE RESTAURANTS='" + restaurant +"'")
            print("DATA",data, type(data))
            for i in data:
                dispatcher.utter_message(text=str(i))

            return []

class FetchBangaloreRestaurants(Action):

    def name(self) -> Text:
        return "fetch_bangalore_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            restaurant = str((tracker.latest_message)['text']).split("Provide me Menu of")[1].strip()
            import sqlite3
            conn = sqlite3.connect('hotel_conn.db')
            data = conn.execute("SELECT FOOD_ITEM, PRICE FROM HOTEL_INFO WHERE RESTAURANTS='" + restaurant +"'")
            print("DATA",data, type(data))
            for i in data:
                dispatcher.utter_message(text=str(i))

            return []
