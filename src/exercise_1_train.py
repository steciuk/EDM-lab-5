import os
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

DATA_PATH = os.path.join(os.getcwd(), "data", "day_prepared.csv")
MODELS_PATH = os.path.join(os.getcwd(), "models")

RS = 42


def main():
    # Load the data
    day_df = pd.read_csv(DATA_PATH)

    # Split the data into X and y
    X = day_df.drop("cnt", axis=1)
    y = day_df["cnt"]

    # Train a random forest regressor
    rf = RandomForestRegressor(random_state=RS)
    rf.fit(X, y)

    # Save the model
    os.makedirs(MODELS_PATH, exist_ok=True)
    with open(os.path.join(MODELS_PATH, "exercise_1_rf.pkl"), "wb") as f:
        pickle.dump(rf, f)


if __name__ == "__main__":
    main()
