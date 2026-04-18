import pandas as pd
import math

stations_df = pd.read_csv("data/stations.csv")


def haversine_distance(lat1, lon1, lat2, lon2):

    R = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat/2)**2 +
        math.cos(lat1) * math.cos(lat2) *
        math.sin(dlon/2)**2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c


def find_nearest_station(user_lat, user_lon):

    nearest_station = None
    min_distance = float("inf")

    for _, row in stations_df.iterrows():

        distance = haversine_distance(
            user_lat,
            user_lon,
            row["lat"],
            row["lon"]
        )

        if distance < min_distance:
            min_distance = distance
            nearest_station = row["station"]

    return nearest_station, min_distance