from aoc_2023_python.lib.classes import Game, Cubes

def d02_cubegames_one(games_list: list[Game], bag_cube_count: Cubes) -> int:
    print("Exercise for Day 02 - Part 1!")
    print("-----------------------------")
    print()

    possible_games: list[Game] = []

    a = Cubes(red=12, green=13, blue=14)
    print(a > bag_cube_count)

    for game in games_list:
        valid_game = True
        for round in game.rounds:
            if round > bag_cube_count:
               valid_game = False
        if valid_game:
            possible_games.append(game)

    valid_game_ids = [game.id for game in possible_games]
    valid_game_ids_sum = sum(valid_game_ids)

    print(f" ---------------------------------------------")
    print(f" --- Sum of possible Game IDs {valid_game_ids_sum} --- ")
    print(f" ---------------------------------------------")

    return valid_game_ids_sum

def d02_cubegames_two():
    pass

