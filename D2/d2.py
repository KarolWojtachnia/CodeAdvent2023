import re

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13


def one_of_results_is_not_feasible(results: list) -> bool:
    for result in results:
        result = result.strip()
        if "red" in result and int(result.split(" ")[0]) > MAX_RED:
            return True
        if "green" in result and int(result.split(" ")[0]) > MAX_GREEN:
            return True
        if "blue" in result and int(result.split(" ")[0]) > MAX_BLUE:
            return True
    return False


def is_game_feasible(draws: list) -> bool:
    for draw in draws:
        draw = draw.replace(", ", ",")
        results = draw.split(",")
        if one_of_results_is_not_feasible(results):
            return False
    return True


def main():
    lines = None
    score = 0

    with open("input.txt") as f:
        lines = f.readlines()

    for id, line in enumerate(lines):
        line = line.strip()
        line = re.sub("Game ([1-9]|[1-9]\d|100):", "", line)
        draws = line.split(";")
        if is_game_feasible(draws):
            score += id + 1

    print("Score of part 1 is " + str(score))


if __name__ == "__main__":
    main()
