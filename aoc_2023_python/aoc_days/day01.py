def find_strdigits_in_line(line: str) -> list[tuple[int, int]]:
    digits: list[tuple[int, int]] = []

    number_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for word in number_mapping.keys():
        start_index = 0
        while start_index is not -1:
            start_index = line.find(word, start_index)
            if start_index is not -1:
                digits.append((start_index, number_mapping[word]))
                start_index += len(word)

    print(f"StrDigits Found: {digits}")
    return digits


def find_intdigits_in_line(line: str) -> list[tuple[int, int]]:
    digits: list[tuple[int, int]] = []

    print(f"")
    for index, character in enumerate(line):
        if character.isdigit():
            print(f"INDEX: {index}, CHAR: {character}")
            digits.append((index, int(character)))

    print(f"IntDigits Found: {digits}")
    return digits


def combine_first_and_last_digits(digits: list[int]) -> int:
    first_digit: int = digits[0]
    last_digit: int = digits[-1]

    return_value = first_digit * 10 + last_digit
    print(f"Converted {digits} -> {return_value}")
    return return_value


def d01_trebuchet_one(calibration_document: list[str]) -> int:
    print("Exercise for Day 01 - Part 1!")
    print("-----------------------------")
    print()

    list_of_numbers: list[int] = []

    for line in calibration_document:
        digits = find_intdigits_in_line(line=line)
        number = combine_first_and_last_digits(digits=[x[1] for x in digits])
        print(f"({line} has number {number})")
        print()
        list_of_numbers.append(number)

    return_value = sum(list_of_numbers)
    print(f" ---------------------------------------------")
    print(f" --- Sum of all numbers is {return_value} --- ")
    print(f" ---------------------------------------------")

    return return_value


def d01_trebuchet_two(calibration_document: list[str]) -> int:
    print("Exercise for Day 01 - Part 2!")
    print("-----------------------------")
    print()

    list_of_numbers: list[int] = []

    for line in calibration_document:
        print("=====================")
        print(f"Current line: {line}")
        digits = find_intdigits_in_line(line=line)
        words = find_strdigits_in_line(line=line)

        sorted_line = sorted(digits + words, key=lambda x: x[0])
        number = combine_first_and_last_digits(digits=[x[1] for x in sorted_line])
        list_of_numbers.append(number)

    return_value = sum(list_of_numbers)
    print(f" ---------------------------------------------")
    print(f" --- Sum of all numbers is {return_value} --- ")
    print(f" ---------------------------------------------")

    return return_value
