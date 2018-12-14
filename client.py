#!/usr/bin/env python3
import os
from random import shuffle
from time import sleep

import requests

# BASE_URL = "http://0.0.0.0:5000"
BASE_URL = "http://www.eyedentity.net"
number_of_questions = 6
questions = ["What is your biggest irrational fear?", "What's your biggest regret in life?",
             "What trait do you envy in others?", "Do you consider yourself an introvert or an extrovert?",
             "What makes you feel uneasy?", "What's your philosophy in life?",
             "What makes you feel accomplished?", "What's an ideal weekend for you?",
             "What is your idea of a perfect vacation?", "What is the weirdest thing about you?",
             "How would your best friend describe you in five words?"]

shuffle(questions)


def clear():
    print("\033[H\033[J")


def gif(file, loops=1):
    clear()
    os.system(
        "gif-for-cli --display-mode=256fgbg --rows `tput lines` --cols `tput cols` -l %d %s" % (loops, file))


def add_sentences(sentences):
    payload = {"sentences": sentences}
    response = requests.post(BASE_URL + "/add_sentences", json=payload)
    if not response.status_code == requests.codes.ok:
        print("Failed")
        print(response)
        print(sentences)
    else:
        gif("bars.gif", loops=6)
        sleep(2)
        gif("thank-you.gif", loops=10)
        print("Thank you %s. Checkout www.eyedentity.net and find your results." %
              response.json().get("key").replace(".png", ""))


def ask_questions():
    answers = list()
    for question in questions[:number_of_questions - 1]:
        gif("blink.gif")
        answer = ""
        while answer == "":
            answer = input(question + ": ").strip()
        answers.append(answer)
    return answers


def main():
    sentences = ask_questions()
    add_sentences(sentences)


if __name__ == "__main__":
    status = requests.get(BASE_URL + "/status")
    if not status.text == "OK":
        gif("error.gif")
        print("Can't access " + BASE_URL)
        exit(1)
    try:
        while True:
            main()
            sleep(30)
            print("Reseting...")
    except (KeyboardInterrupt, EOFError):
        print("Exiting...")
        exit(0)
