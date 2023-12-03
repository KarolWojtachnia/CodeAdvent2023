def get_input_path(which_day: int) -> str:
    return f"inputs/input{which_day}.txt"


def read_lines(filepath: str) -> list:
    with open(filepath) as f:
        return f.readlines()


def get_input_for_day(which_day: int) -> list:
    return read_lines(get_input_path(which_day))
