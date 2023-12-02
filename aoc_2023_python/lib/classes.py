from dataclasses import dataclass
from typing import Self

@dataclass
class Cubes:
    blue: int
    green: int
    red: int

    def __gt__(self, other: "Cubes"):
        return self.blue > other.blue or self.green > other.green or self.red > other.red


@dataclass
class Game:
    id: int
    rounds: list[Cubes]


    @classmethod
    def from_text_input(cls: type[Self], text: str) -> Self:

        # Find the Game ID
        begin = "Game "
        id = text[text.find(begin) + len(begin):text.rfind(":")]

        # Find the rounds 
        rounds_string = text.split(":")[1]
        rounds = rounds_string.split(";")

        rounds_list: list[Cubes] = []
        for round in rounds:
            cubes = round.split(",")
            colour_counts = Cubes(blue=0, green=0, red=0)
            for colour in cubes:
                count, colour_type = colour.strip().split()

                # Match the colour type
                match colour_type:
                    case "blue":
                        colour_counts.blue = int(count)
                    case "green":
                        colour_counts.green = int(count)
                    case "red": 
                        colour_counts.red = int(count)
                    case _:
                        raise SystemExit("Wrong Colour.")

            rounds_list.append(colour_counts) 

        return Game(
            id = int(id),
            rounds = rounds_list
        )


        