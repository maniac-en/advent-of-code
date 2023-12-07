with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

powers = []

# for id, game in enumerate(test.split("\n"), start=1):
for id, game in enumerate(input, start=1):
    min_cubes = {"red": float("-inf"), "green": float("-inf"), "blue":
                 float("-inf")}
    for round in game[game.find(":") + 2:].split("; "):
        for cubes in round.split(", "):
            num_cube, cube_type = cubes.split()
            if int(num_cube) > min_cubes[cube_type]:
                min_cubes[cube_type] = int(num_cube)

    powers.append(min_cubes["red"] * min_cubes["green"] * min_cubes["blue"])

print(sum(powers))
