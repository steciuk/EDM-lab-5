import os

import pandas as pd


def main():
    DATA_PATH = os.path.join(os.getcwd(), "data", "day.csv")
    day_df = pd.read_csv(DATA_PATH)

    # Drop unused columns
    day_df = day_df.drop(
        columns=[
            "instant",
            "yr",
            "mnth",
            "weekday",
            "atemp",
            "casual",
            "registered",
        ]
    )

    # Use one-hot encoding for season (it will give you 3 features).
    season_dummies = pd.get_dummies(day_df["season"], prefix="season", drop_first=True)
    day_df = pd.concat([day_df, season_dummies], axis=1)
    day_df = day_df.drop("season", axis=1)

    # Create a feature MISTY that is 1 when weathersit is 2. In other cases it will be 0.
    day_df["misty"] = day_df["weathersit"].apply(lambda x: 1 if x == 2 else 0)
    # Create a feature RAIN that will be 1 when weathersit is 3 or 4. It will be 0 in other case.
    day_df["rain"] = day_df["weathersit"].apply(lambda x: 1 if x == 3 or x == 4 else 0)
    day_df = day_df.drop("weathersit", axis=1)

    # Denormalize temp, hum and windspeed.
    t_min = -8
    t_max = 39
    hum_max = 100
    windspeed_max = 67

    day_df["temp"] = day_df["temp"] * (t_max - t_min) + t_min
    day_df["hum"] = day_df["hum"] * hum_max
    day_df["windspeed"] = day_df["windspeed"] * windspeed_max

    day_df["days_since_2011"] = day_df["dteday"].apply(
        lambda x: (pd.to_datetime(x) - pd.to_datetime("2011-01-01")).days
    )
    day_df = day_df.drop("dteday", axis=1)

    # Save the result to data/day_prepared.csv
    day_df.to_csv(os.path.join(os.getcwd(), "data", "day_prepared.csv"), index=False)


if __name__ == "__main__":
    main()
