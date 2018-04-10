import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats
from os import path

from config import INPUT_PATH, OUTPUT_PATH


def draw_plot(input_file, output_file):
    # Initialize the matplotlib figure
    sns.set_style("ticks")
    f, ax = plt.subplots(figsize=(6, 5))

    # Load the example car crash dataset
    aoi_participant_data = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    colors = sns.color_palette("RdBu_r", 7)
    x = np.linspace(0, 10, 1000)

    distplot = sns.distplot(aoi_participant_data.distance_y, vertical=True, color=colors[1])

    plt.plot(x, x + 25, linestyle='--', color=colors[0])
    plt.plot(x, x - 25, linestyle='--', color=colors[0])

    plt.plot(x, x + 40, linestyle=':', color=colors[-1])
    plt.plot(x, x - 40, linestyle=':', color=colors[-1])

    ax.set(xlabel="Percentage of Fixations", ylabel="Vertical Distance from Center of Task Identifier")

    # Add text labels
    plt.text(0.009, 70, 'Above Identifier', fontsize=10)
    plt.text(0.0095, -5, 'Identifier', fontsize=10, color=colors[0])
    plt.text(0.009, -90, 'Below Identifier', fontsize=10)

    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = distplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)
