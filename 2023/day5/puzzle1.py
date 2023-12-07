with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# input = test.split("\n")
maps = {}
inside_map = False

for ix, line in enumerate(input[2:]):
    if line.endswith("map:") and not inside_map:
        map_name = line[:-5]
        maps[map_name] = []
        inside_map = True
    elif line == "":
        inside_map = False
    else:
        ls = line.split(" ")
        source_start, source_end = int(ls[1]), int(ls[1]) + int(ls[2])
        destination_start = int(ls[0])
        maps[map_name].append((
            source_start,
            source_end,
            destination_start,
        ))


def get_destination(source, source_type, final_destination) -> int:
    global maps
    destination, destination_type = None, None

    for map_type in maps.keys():
        if map_type.startswith(source_type):
            destination_type = map_type[map_type.index("-to-") + 4:]
            break

    if destination_type is not None:
        destination = source
        for map in maps[map_type]:
            if source >= map[0] and source < map[1]:
                destination = source - map[0] + map[2]
                break

        if destination_type != final_destination:
            return get_destination(
                destination,
                destination_type,
                final_destination)

    return destination


lowest_location = float("inf")
seeds = [int(n) for n in input[0].split(": ")[1].split()]
for seed in seeds:
    location = get_destination(seed, "seed", "location")
    if lowest_location > location:
        lowest_location = location

print(lowest_location)
