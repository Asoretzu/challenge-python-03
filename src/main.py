# Resolve the problem!!

import re


def run():
    text = ""
    letters = "[a-z]"
    message = ""

    with open("encoded.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            text += line
    
    for letter in text:
        if re.match(letters, letter):
            message += letter
    
    print(message)


if __name__ == '__main__':
    run()
