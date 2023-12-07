with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

ids = []


def is_round_possible(round) -> bool:
    total_cubes = {"red": 12, "green": 13, "blue": 14}
    for cubes in round.split(", "):
        num_cube, cube_type = cubes.split()
        if int(num_cube) > total_cubes[cube_type]:
            return False
    return True


# for id, game in enumerate(test.split("\n"), start=1):
for id, game in enumerate(input, start=1):
    ids.append(id)
    for round in game[game.find(":") + 2:].split("; "):
        if not is_round_possible(round):
            ids.pop()
            break

print(sum(ids))
