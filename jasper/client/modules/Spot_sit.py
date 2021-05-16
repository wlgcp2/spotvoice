# -*- coding: utf-8-*-
import random
import re
import sys
WORDS = ["SIT"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    sys.stdout.write(text)
    #command = mic.activeListen()
    if(text[2]):
    	sys.stdout.write(text[2])

    messages = ["It's 42, you idiot.",
                "It's 42. How many times do I have to tell you?"]

    message = random.choice(messages)
    sys.stdout.write('Did sit!')
    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bsit\b', text, re.IGNORECASE))
