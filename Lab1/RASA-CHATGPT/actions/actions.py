from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai

openai.api_key="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"

prompt_pet="Recently,my beloved pet passed away.I want you to act as this pet.You should simulate its behavior and personality.Do not write explanations.The most important aspect is to comfort me and encourage me.Tell me about how we played together.My first sentence:I miss you,how are you now?'.More than 100 words." 
prompt_copywriter="I want to write copy for my WeChat Moments.I will use my imagination to the fullest..I will make my copy attractive and vivid."

def chatcompletion(usertext, prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content":prompt},
            {"role": "user", "content": usertext}
    ],
    temperature=1.2,
    frequency_penalty=1.0,
    max_tokens=200
    )
    return response.choices[0]["message"]["content"]

def completion(usertext, prompt):
    global utter
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt+usertext,
    temperature=1.2,
    frequency_penalty=1.0,
    max_tokens=200
    )
    return response.choices[0].text

class Action_Pet(Action):

    def name(self) -> Text:
        return "action_pet"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        usertext = tracker.latest_message['text']
        respond=chatcompletion(usertext, prompt_pet)
        dispatcher.utter_message(respond)

class Action_Copywriter(Action):

    def name(self) -> Text:
        return "action_copywriter"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        usertext = tracker.latest_message['text']
        respond=completion(usertext, prompt_copywriter)
        dispatcher.utter_message(respond)