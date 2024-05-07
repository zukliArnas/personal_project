from pathlib import Path
p = Path("advent_of_code_1_input")
p = p.read_text()
lines = p.splitlines()

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
    return first_value+second_value

def main():
    sum_of_all_values = 0
    for element in lines:
        value = int(get_number(element))
        sum_of_all_values += value
    print(sum_of_all_values)

main()