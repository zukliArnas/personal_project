from pathlib import Path
import re
data = Path("advent_of_code_day_2_input").read_text().splitlines()


def count_min_color(color: str, line: str):
    colour = re.findall(r'\d+' + ' ' + color, line)
    colour = [int(item.split()[0]) for item in colour]
    max_value = max(colour, default=1)
    return max_value


def main(lines: list):
    sum_of_values = 0
    for line in lines:
        multiply = (count_min_color('red', line) * count_min_color('blue', line) *
                    count_min_color('green', line))
        sum_of_values += multiply
    print(sum_of_values)


if __name__ == "__main__":
    main(lines=data)