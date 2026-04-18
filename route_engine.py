import pandas as pd
from collections import deque

stations_df = pd.read_csv("data/stations.csv")

metro_graph = {}

lines = stations_df["line"].unique()

for line in lines:

    line_stations = stations_df[stations_df["line"] == line]
    line_stations = line_stations.sort_values("sequence")

    stations = line_stations["station"].tolist()

    for i in range(len(stations)):

        station = stations[i]

        if station not in metro_graph:
            metro_graph[station] = []

        if i > 0:
            prev_station = stations[i - 1]
            metro_graph[station].append(prev_station)

        if i < len(stations) - 1:
            next_station = stations[i + 1]
            metro_graph[station].append(next_station)


def find_route(start, end):

    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        station = path[-1]

        if station == end:
            return path

        if station not in visited:

            visited.add(station)

            for neighbor in metro_graph[station]:

                new_path = list(path)
                new_path.append(neighbor)

                queue.append(new_path)

    return None