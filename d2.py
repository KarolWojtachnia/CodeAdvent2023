import re
from my_utils import get_input_for_day

WHICH_DAY = 2
MAX_COLORS = {"blue": 14, "red": 12, "green": 13}


def evaluate_results(results: list, min_values: dict) -> tuple:
    not_feasible = False

    for result in results:
        value_str, color = result.strip().split(" ")
        value = int(value_str)

        if value > MAX_COLORS[color]:
            not_feasible = True

        if value > min_values[color]:
            min_values[color] = value

    return not_feasible, min_values["blue"], min_values["green"], min_values["red"]


def evaluate_game(draws: list) -> tuple:
    feasible = True
    min_colors = {"blue": 0, "green": 0, "red": 0}

    for draw in draws:
        draw = draw.replace(", ", ",")
        results = draw.split(",")
        not_feasible, min_blues, min_greens, min_reds = evaluate_results(
            results, min_colors
        )
        feasible = not not_feasible

        min_colors["blue"] = max(min_colors["blue"], min_blues)
        min_colors["green"] = max(min_colors["green"], min_greens)
        min_colors["red"] = max(min_colors["red"], min_reds)

    return feasible, min_colors["blue"], min_colors["green"], min_colors["red"]


def main():
    score_part_1 = 0
    score_part_2 = 0

    lines = get_input_for_day(WHICH_DAY)

    for id, line in enumerate(lines):
        line = re.sub("Game ([1-9]|[1-9]\d|100):", "", line.strip())
        draws = line.split(";")
        feasible, blues, greens, reds = evaluate_game(draws)
        print(f"game:{id} r:{reds} g:{greens} b:{blues}")
        if feasible:
            score_part_1 += id + 1
        score_part_2 += blues * greens * reds

    print("Score of part 1 is " + str(score_part_1))
    print("Score of part 2 is " + str(score_part_2))


if __name__ == "__main__":
    main()
