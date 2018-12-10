import os
from random import shuffle
from time import sleep

import requests

BASE_URL = "http://0.0.0.0:5000/"

questions = ["What is your biggest irrational fear?", "What's your biggest regret in life?",
             "What personal trait do you most despise?", "If you died tomorrow, what would you wish you had done?",
             "What makes you feel uneasy?", "Tell me your biggest supernatural or paranormal fear?"]

shuffle(questions)


def clear():
    print("\033[H\033[J")


def blink_eye(blinks=1):
    clear()
    os.system("gif-for-cli -l %d blink.gif" % blinks)


def add_sentences(sentences):
    # print(sentences)
    payload = {"sentences": sentences}
    response = requests.post(BASE_URL + "add_sentences", json=payload)
    if not response.status_code == requests.codes.ok:
        print("Failed")
        print(response)
        print(sentences)
    else:
        print("Thank you %s. Your answers have been submitted" %
              response.json().get("key").replace(".png", ""))
    return response


def ask_questions():
    answers = list()
    for question in questions[:len(questions) - 1]:
        blink_eye()
        answer = ""
        while answer == "":
            answer = input(question + ": ")
        answers.append(answer)
    return answers


def main():
    sentences = ask_questions()
    response = add_sentences(sentences)


if __name__ == "__main__":
    try:
        while True:
            main()
            sleep(10)
            print("Reseting...")
    except (KeyboardInterrupt, EOFError):
        print("Exiting...")
        exit(0)
