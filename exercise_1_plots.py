import os
import pickle

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.inspection import PartialDependenceDisplay

DATA_PATH = os.path.join(os.getcwd(), "data", "day_prepared.csv")
MODEL_PATH = os.path.join(os.getcwd(), "models", "exercise_1_rf.pkl")
PDP_PLOT_PATH = os.path.join(os.getcwd(), "plots", "exercise_1", "pdp_plot.png")
PDP_DENSITY_PLOT_PATH = os.path.join(
    os.getcwd(), "plots", "exercise_1", "pdp_density_plot.png"
)

RS = 42


def main():
    # Read the data and model
    day_df = pd.read_csv(DATA_PATH)
    with open(MODEL_PATH, "rb") as f:
        rf = pickle.load(f)

    # Split the data into X and y
    X = day_df.drop("cnt", axis=1)
    y = day_df["cnt"]

    # Create PDP plots
    features = [
        "temp",
        "hum",
        "windspeed",
        "days_since_2011",
    ]

    labels = [
        "Temperature",
        "Humidity",
        "Windspeed",
        "Days since 2011",
    ]

    # PDP plot
    fig = plt.figure(figsize=(10, 10))
    fig = fig.subplots(2, 2)
    PartialDependenceDisplay.from_estimator(
        rf,
        X,
        features,
        ax=fig,
        kind="both",
        random_state=RS,
        ice_lines_kw={"alpha": 0.1},
    )

    for ax, label in zip(fig.ravel(), labels):
        ax.set_xlabel(label)

    plt.tight_layout()
    plt.savefig(PDP_PLOT_PATH)

    # PDP density plot
    fig = plt.figure(figsize=(10, 10))
    fig = fig.subplots(2, 2)
    PartialDependenceDisplay.from_estimator(
        rf,
        X,
        features,
        ax=fig,
        grid_resolution=700,
        categorical_features=features,
        random_state=RS,
    )

    for ax, label in zip(fig.ravel(), labels):
        ax.set_xlabel(label)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)

    plt.tight_layout()
    plt.savefig(PDP_DENSITY_PLOT_PATH)


if __name__ == "__main__":
    main()
