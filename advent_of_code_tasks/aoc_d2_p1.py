from pathlib import Path
data = Path("advent_of_code_day_2_input").read_text().splitlines()

RED = 12
GREEN = 13
BLUE = 14


def is_game_valid(line: str):
    line = line[line.find(":") + 1:]  # Removing everything after "Game X: "
    games = line.split(";")           # Splitting in single elements before ";"

    single_game = []                  # Creating a new list of single games
    for game in games:
        single_game.extend(game.split(','))  # Adding all elements into single_game list, creating a fully extracted
                                             # data into single elements ['number colour', ...]

    for colour in single_game:
        colour.strip()                      # Removing necessary empty spaces
        amount = int(colour[:3].strip())    # Separating amount from colours values
        colour = colour[3:].strip()         # Separating colours from amount

        if colour == 'red' and amount > RED:
            return False
        elif colour == 'blue' and amount > BLUE:
            return False
        elif colour == 'green' and amount > GREEN:
            return False
    return True


def main(lines: list):
    sum_of_game = 0
    for i, line in enumerate(lines):
        if is_game_valid(line):
            sum_of_game += 1 + i
    print(sum_of_game)


if __name__ == "__main__":
    main(data)