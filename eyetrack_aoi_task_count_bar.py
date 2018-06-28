import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from os import path

from config import INPUT_PATH, OUTPUT_PATH


def print_color_in_rgb(param):
    print("R: ", 256*param[0])
    print("G: ", 256*param[1])
    print("B: ", 256*param[2])


def draw_plot(input_file, output_file):
    # Initialize the matplotlib figure
    sns.set(font_scale=1.1)
    sns.set_style("whitegrid")
    f, ax = plt.subplots(figsize=(8, 6))

    # Load the example car crash dataset
    aoi_participant_data = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    aoi_participant_data = aoi_participant_data.sort_values("aoi_50px", ascending=True)

    colors = sns.color_palette("RdBu_r", 7)

    print_color_in_rgb(colors[-1])
    print_color_in_rgb(colors[-3])
    print_color_in_rgb(colors[1])

    sns.barplot(y="aoi_50px", x="snippet", data=aoi_participant_data, label="Extra AOI (50px)", color=colors[-1])
    sns.barplot(y="aoi_25px", x="snippet", data=aoi_participant_data, label="Extra AOI (25px)", color=colors[-3])
    barplot = sns.barplot(y="aoi_inner", x="snippet", data=aoi_participant_data, label="Inner AOI", color=colors[1])

    # Add a legend and informative axis label
    ax.legend(loc="upper left")
    ax.set(ylim=(0), xlabel="Code Snippets", ylabel="Fixation Count in AOIs around Task Identifier")

    plt.xticks(rotation=90)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = barplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False, bbox_inches='tight', pad_inches=0)
