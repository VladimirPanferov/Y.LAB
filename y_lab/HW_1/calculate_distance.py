import math

from typing import (
    List,
    Tuple,
)


def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))


def find_nearest_point(result: List, destinations: dict) -> Tuple[int, int]:
    point_a = list(result[-1].keys())[0]
    for point in destinations:
        destinations[point] = calculate_distance(point_a, point)
    return min(destinations, key=destinations.get)


def main():
    start_point = {(0, 2): 0}
    destinations = {
        (2, 5): 0,
        (5, 2): 0,
        (6, 6): 0,
        (8, 3): 0,
    }
    result = [start_point]
    while destinations:
        point_with_min_distance = find_nearest_point(result, destinations)
        result.append(
            {point_with_min_distance: destinations.pop(point_with_min_distance)}
            )
    for point in start_point:
        point_a = list(result[-1].keys())[0]
        result.append(
            {point: calculate_distance(point_a, point)}
        )
    distance = 0
    path = []
    for route_point in result:
        point = list(route_point.keys())[0]
        distance += route_point[point]
        path.append(f"{point}{f'[{distance}]' if route_point[point] else ''}")
    print(" -> ".join(path))


if __name__ == "__main__":
    main()
