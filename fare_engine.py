import pandas as pd

fare_df = pd.read_csv("data/fare_matrix.csv")


def calculate_fare(distance):

    slab = fare_df[
        (fare_df["distance_km_min"] <= distance) &
        (fare_df["distance_km_max"] >= distance)
    ]

    if not slab.empty:
        return slab.iloc[0]["fare_inr"]

    return None