from aoc_2023_python.aoc_days.day01 import d01_trebuchet_one, d01_trebuchet_two
from aoc_2023_python.aoc_days.day02 import d02_cubegames_one, d02_cubegames_two
from aoc_2023_python.lib.helpers import input_loader, cube_loader
from aoc_2023_python.lib.classes import Cubes


def aoc():
    calibration_document_example1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    calibration_document_example2 = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    calibration_document_list = input_loader("day01")
    

    # d01_trebuchet_one(calibration_document=calibration_document_example1)
    # d01_trebuchet_one(calibration_document=calibration_document_list)

    # d01_trebuchet_two(calibration_document_example2)
    # d01_trebuchet_two(calibration_document=calibration_document_list)

    
    game_list = cube_loader("day02")
    bag_cube_count = Cubes(red=12, green=13, blue=14)
    d02_cubegames_one(games_list=game_list, bag_cube_count=bag_cube_count)

    # print(game_list)
    


if __name__ == "__main__":
    aoc()
