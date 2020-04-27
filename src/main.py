# Resolve the problem!!

import re


def run():
    pattern = re.compile(r"[a-z]")
    message = ""

    with open("encoded.txt", mode="r", encoding="utf-8") as f:
        text = f.read()

    message = re.findall(pattern, text)

    print("".join(message))


if __name__ == '__main__':
    run()
