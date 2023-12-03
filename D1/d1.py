import re


def main():
    lines = None
    score = 0
    digits_as_literals = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    with open("input.txt") as f:
        lines = f.readlines()

    for id, line in enumerate(lines):
        print(line.strip())
        number = "".join(c for c in line.strip() if c.isdigit())

        score += int(number[0] + number[-1])
    print(number[0] + number[-1])

    print("Score for part one is: " + str(score))

    score = 0
    for line in lines:
        digits = []
        for i, c in enumerate(line.strip()):
            if c.isdigit():
                digits.append(c)
            else:
                for d, val in enumerate(digits_as_literals):
                    if line[i:].startswith(val):
                        digits.append(str(d + 1))
        score += int(digits[0] + digits[-1])

    print("Score for part two is: " + str(score))


if __name__ == "__main__":
    main()
