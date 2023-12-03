from my_utils import get_input_for_day

WHICH_DAY = 1
DIGITS_AS_LITERALS = [
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


def main():
    lines = get_input_for_day(WHICH_DAY)
    score = 0

    do_part1(lines, score)

    score = 0
    do_part2(lines, score)


def do_part2(lines, score):
    for line in lines:
        digits = []
        for i, c in enumerate(line.strip()):
            append_digit(line, digits, i, c)
        score += int(digits[0] + digits[-1])
    print("Score for part two is: " + str(score))


def do_part1(lines, score):
    for line in lines:
        number = "".join(c for c in line.strip() if c.isdigit())
        score += int(number[0] + number[-1])
    print("Score for part one is: " + str(score))


def append_digit(line, digits, id, character):
    if character.isdigit():
        digits.append(character)
    else:
        for d, val in enumerate(DIGITS_AS_LITERALS):
            if line[id:].startswith(val):
                digits.append(str(d + 1))


if __name__ == "__main__":
    main()
