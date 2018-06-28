import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from os import path

from config import INPUT_PATH, OUTPUT_PATH


def draw_plot(input_file, output_file):
    # Initialize the matplotlib figure
    sns.set(font_scale=1.1)
    sns.set_style("ticks")
    f, ax = plt.subplots(figsize=(8, 5))

    # Load the example car crash dataset
    aoi_participant_data = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    colors_str = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
    colors = sns.xkcd_palette(colors_str)
    colors_old = sns.color_palette("RdBu_r", 7)
    x = np.linspace(0, 10, 1000)

    plot_data = aoi_participant_data.distance_y
    distplot = sns.distplot(plot_data, vertical=True, color=colors[2])

    plt.plot(x, x + 25, linestyle='--', color='b')
    plt.plot(x, x - 25, linestyle='--', color='b')

    plt.plot(x, x + 40, linestyle=':', color='r')
    plt.plot(x, x - 40, linestyle=':', color='r')

    ax.set(xlabel="Percentage of Fixations", ylabel="Vertical Distance from Task Identifier")

    # Add text labels
    plt.text(0.00875, 70, 'Above Identifier', fontsize=12)
    plt.text(0.0095, -5, 'Identifier', fontsize=12, color=colors_old[0])
    plt.text(0.00875, -90, 'Below Identifier', fontsize=12)

    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = distplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False, bbox_inches='tight', pad_inches=0)
