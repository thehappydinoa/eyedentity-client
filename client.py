import os

import requests

BASE_URL = "http://0.0.0.0:5000/"

QUESTION_1 = "What is your darkest fear?: "
QUESTION_2 = "What personal trait do you most admire??: "
QUESTION_3 = "What personal trait do you most despise???: "


def clear():
    print("\033[H\033[J")


def blink_eye(blink=1):
    clear()
    os.system("gif-for-cli -l %d blink.gif" % blink)


def add_sentences(sentences):
    # print(sentences)
    payload = {"sentences": sentences}
    response = requests.post(BASE_URL + "add_sentences", json=payload)
    if not response.status_code == requests.codes.ok:
        print("Failed")
        print(response)
        print(sentences)
    return response


def ask_questions():
    blink_eye()
    answer_1 = input(QUESTION_1)
    blink_eye()
    answer_2 = input(QUESTION_2)
    blink_eye()
    answer_3 = input(QUESTION_3)
    return [answer_1, answer_2, answer_3]


def main():
    sentences = ask_questions()
    response = add_sentences(sentences)


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
