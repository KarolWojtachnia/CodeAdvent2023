import re

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13


def one_of_results_is_not_feasible(results: list) -> [bool, int, int, int]:
    min_blues = 0
    min_reds = 0
    min_greens = 0
    for result in results:
        result = result.strip()
        not_feasible = False
        if "red" in result:
            if int(result.split(" ")[0]) > MAX_RED:
                not_feasible = True
            if int(result.split(" ")[0]) > min_reds:
                min_reds = int(result.split(" ")[0])
        if "green" in result:
            if int(result.split(" ")[0]) > MAX_GREEN:
                not_feasible = True
            if int(result.split(" ")[0]) > min_greens:
                min_greens = int(result.split(" ")[0])
        if "blue" in result:
            if int(result.split(" ")[0]) > MAX_BLUE:
                not_feasible = True
            if int(result.split(" ")[0]) > min_blues:
                min_blues = int(result.split(" ")[0])
    return not_feasible, min_blues, min_greens, min_reds


def is_game_feasible(draws: list) -> [bool, int, int, int]:
    feasible = True
    blues = 0
    greens = 0
    reds = 0
    for draw in draws:
        draw = draw.replace(", ", ",")
        results = draw.split(",")
        not_feasible, min_blues, min_greens, min_reds = one_of_results_is_not_feasible(
            results
        )
        feasible = not not_feasible
        if min_blues > blues:
            blues = min_blues
        if min_greens > greens:
            greens = min_greens
        if min_reds > reds:
            reds = min_reds
    return feasible, blues, greens, reds


def main():
    lines = None
    score = 0
    score_2 = 0

    with open("input.txt") as f:
        lines = f.readlines()

    for id, line in enumerate(lines):
        line = line.strip()
        line = re.sub("Game ([1-9]|[1-9]\d|100):", "", line)
        draws = line.split(";")
        feasible, blues, greens, reds = is_game_feasible(draws)
        print(f"game:{id} r:{reds} g:{greens} b:{blues}")
        if feasible:
            score += id + 1
        score_2 += blues * greens * reds

    print("Score of part 1 is " + str(score))
    print("Score of part 2 is " + str(score_2))


if __name__ == "__main__":
    main()
