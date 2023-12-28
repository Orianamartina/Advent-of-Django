from lib.input_handlers import read_file
from lib.answer_display import print_answer
import re
from collections import defaultdict

file_contents = read_file("day15/15input.txt")

pattern = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)

parsed_input = pattern.findall(file_contents)

coordinates = []
for line in parsed_input:
    x1, y1, x2, y2 = line
    coordinates.append({"sensor": (int(x1), int(y1)), "beacon": (int(x2), int(y2))})


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


pair_distances = []

for pair in coordinates:
    sensor, beacon = pair.values()
    pair_distances.append(
        manhattan_distance(sensor[0], sensor[1], beacon[0], beacon[1])
    )


def positions_that_dont_contain_beacons_in(row, map):
    empty_coordinates = set()
    used_x = set()
    for i, coordinate in enumerate(map):
        sensor, beacon = coordinate.values()
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon

        beacon_distance = pair_distances[i]

        limit = max(beacon_distance - abs(row - sensor_y), 0)
        if sensor_y == row:
            used_x.add(sensor_x)
        if beacon_y == row:
            used_x.add(beacon_x)
        for i in range(sensor_x - limit, sensor_x + limit + 1):
            if i not in used_x:
                empty_coordinates.add(i)
    return len(empty_coordinates)


# part 2:

map = coordinates


def find_signal(map):
    counter = 1
    passed_coordinates = defaultdict(lambda: 0)
    for i, coordinate in enumerate(map):
        sensor_x, sensor_y = coordinate["sensor"]

        print("Analyzing: ", counter, "/", len(pair_distances))
        beacon_distance = pair_distances[i] + 1

        distance = generate_points_with_manhattan_distance(
            sensor_x, sensor_y, beacon_distance, passed_coordinates
        )
        if distance:
            return distance
        counter += 1


def generate_points_with_manhattan_distance(
    central_x, central_y, radius, passed_coordinates
):
    limit = 4000000
    for x in range(max(central_x - radius, 0), min(central_x + radius + 1, limit)):
        possible_y_values = radius - abs(x - central_x)
        length = len(pair_distances)
        for y in [central_y + possible_y_values, central_y - possible_y_values]:
            counter = 0
            if y < limit and y > 0:
                passed_coordinates[(x, y)] += 1
                if passed_coordinates[(x, y)] == 4:
                    for j, coordinate in enumerate(map):
                        sensor = coordinate["sensor"]
                        distance = manhattan_distance(x, y, sensor[0], sensor[1])
                        if distance <= pair_distances[j]:
                            break
                        else:
                            counter += 1
                    if counter == length:
                        return (x, y)


print_answer("15.1", positions_that_dont_contain_beacons_in(2000000, coordinates))
print("Part 2:")
part_two = list(find_signal(map))
print_answer("15.2", (part_two[0] * 4000000) + part_two[0])
