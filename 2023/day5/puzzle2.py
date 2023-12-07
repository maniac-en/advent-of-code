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


def process_input(filename):
    seeds = []
    maps = []

    for line in input:
        if line == '':
            continue

        token = line.split()

        if token[1] == 'map:':
            maps.append([])
            map_index = len(maps) - 1
            continue

        if token[0] == 'seeds:':
            st = 1
            while st < len(token):
                seed_start = int(token[st])
                seed_end = seed_start + int(token[st + 1]) - 1
                seeds.append((seed_start, seed_end))
                st += 2
            continue

        dest = int(token[0])
        source = int(token[1])
        range_len = int(token[2])
        source_end = source + range_len - 1
        adjustment = dest - source
        maps[map_index].append((source, source_end, adjustment))
    return seeds, maps


def apply_maps(seeds, maps):
    lowest = float("inf")
    for seed in seeds:
        destinations = []
        destinations.append(seed)
        for map in maps:
            sources = destinations
            destinations = []
            while len(sources) > 0:
                source = sources.pop()
                source_start, source_end = source
                for range in map:
                    map_start, map_end, adjust = range
                    if source_start >= map_start and source_end <= map_end:
                        destinations.append(
                            (source_start + adjust, source_end + adjust))
                        break
                    if source_end < map_start or source_start > map_end:
                        continue
                    if source_start < map_start:
                        sources.append((source_start, map_start - 1))
                        sources.append((map_start, source_end))
                        break
                    if source_end > map_end:
                        sources.append((source_start, map_end))
                        sources.append((map_end + 1, source_end))
                        break
                else:
                    destinations.append(source)
        seed_lowest = lowest_location(destinations)
        lowest = min(lowest, seed_lowest)
    return lowest


def lowest_location(locations):
    lowest = locations[0][0]
    for location in locations:
        lowest = min(location[0], lowest)
    return lowest


seeds, maps = process_input(input)
print(apply_maps(seeds, maps))
