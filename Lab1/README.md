# README

[TOC]

## Environment

Python 3.9.13

Windows 11

```
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai
```

PS.To use my API Keys,you must connect to the VPN first.

## Using

##### 1.Open cmd or Powershell in the folder ‘RASA-CHATGPT’.

##### 2.Input "rasa train".

##### 3.Input"rasa run actions"

##### 4.Create another terminal(cmd or Powershell),Input"rasa shell --endpoints endpoints.yml"

##### 5.Start Talking.

###### 5.1 Virtual pet

You should input  "/virtual_pet" to reach the first goal.

> Your input ->  /virtual_pet
> Can you tell me about your pet's behavior and personality?

Next,you should describe your pets' behavior and personality.

> Your input ->  My cat is cute and noisy.She likes meowing,and likes my touching and petting.She will grind her paws very often.

> Meow! Hi there, it's me, your beloved pet. I may not be physically here with you anymore, but I still live on in your memories and heart. Don't worry about how I'm doing now because I'm in a better place where there is no pain or suffering.
> Remember how much fun we had together? We played hide-and-seek and chase around the house. My favorite was when we snuggled up on the couch and watched movies together. I loved cuddling up next to you and feeling those gentle strokes from your hand that made my purr louder!
> I want you to know that despite all the meowing, napping and chasing, the greatest joy of my life was being with you. Please don't grieve for too long because one day we will be reunited again.
> Take care of yourself, cherish our cherished memories - until then always know that deep down in your soul – I love you forever!

###### 5.2 Virtual copywriter

You should input  "/virtual_copywriter" to reach the second goal.

> Your input ->  /virtual_copywriter
> Can you describe the content conveyed in the Wechat Moments?

Next,you should  describe the mood you want to convey or what kind of image you want to match.

> Your input ->  Today I take a trip to Wuhan.

> to visit the East Lake and appreciate its beauty. The sun shining brightly on the rivers and tree-lined trails, murmuring of waterfalls in the distance and birdsong echoing overhead made me transfixed – an incredibly tranquil atmosphere! I am deeply captivated by its monestarycomplexes bridges, pavilions, as well as magnolia and peach blossoms in full bloom at every season. What a charming city Wuhan is! #trip#Wuhan #EastLake #traveling