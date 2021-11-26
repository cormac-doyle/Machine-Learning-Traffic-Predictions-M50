import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import pause
from typing import List
from sklearn.tree import DecisionTreeRegressor



def visualise_dataset(df):
    """
    Utility function for visualising the preprocessed dataset

    Args:
        df: Pandas dataframe containing the data
    """
    red = "#b20710"

    fig, ax = plt.subplots(1, 1, figsize=(40, 10))

    lanes = ["northBound", "southBound"]
    colours = ["blue", "red"]

    ax.set(xlabel="", title="Lane Volume")
    for lane, colour in zip(lanes, colours):
        df[lane].plot(color=colour, label=lane)

    plt.ylabel("Volume")
    plt.legend()
    plt.show()


def visualise_features(
    feature_names: List[str], df: pd.DataFrame, large_title: str, target_var: str
):
    """
    Utility function for visualising features effect on data.

    Args:
        feature_names : A list of feature names
        df : Pandas dataframe of the dataset
        large_title : Large title used for the sub plots
        target_var : String of the column name we are trying to predict

    """

    num_plots: int = len(feature_names)
    fig, ax = plt.subplots(num_plots, 1, figsize=(20, num_plots * 5))

    fig.suptitle(large_title, fontsize=30)

    for feature, ax in zip(feature_names, ax.flatten()):
        grouped = df.groupby(feature)[target_var].mean()
        grouped.plot(ax=ax, color="red", marker="o")

def visualise_decision_tree(decision_tree_model,X,y):
    # Fit regression model
    

    # Predict
    y_pred = decision_tree_model.predict(X)
    

    # Plot the results
    plt.figure()
    
    x_axis=np.arange(0,y.size,1)
    plt.scatter(x_axis,y, s=20, edgecolor="black", c="orange", label="data")
    plt.plot(x_axis,y_pred, color="blue", label='decision tree regressor',linewidth=2)
    plt.xlabel("hour index")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    plt.show()
