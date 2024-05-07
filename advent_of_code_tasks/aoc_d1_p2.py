from pathlib import Path

p = Path("advent_of_code_1_input")
p = p.read_text()
lines = p.splitlines()

word_number_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                   'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def converter(line, dictionary):
    char_inx = 0
    while char_inx < len(line):
        for word, number in dictionary.items():
            if line.startswith(word, char_inx):
                replaced = (word.replace(word[0], number))
                line = line.replace(word, replaced)
        char_inx += 1
    return line


def get_number(line):
    first_value = "0"
    for char in line:
        if char.isdigit():
            first_value = char
            break

    second_value = "0"
    for char in reversed(line):
        if char.isdigit():
            second_value = char
            break
    return first_value + second_value


def main():
    sum_of_all_values = 0
    for line in lines:
        converted_line = converter(line, word_number_map)
        value = int(get_number(converted_line))
        sum_of_all_values += value
    print(sum_of_all_values)


main()