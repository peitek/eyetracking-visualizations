import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from os import path

from config import INPUT_PATH, OUTPUT_PATH


def draw_response_times_plot(input_file, output_file):
    sns.set_style("ticks", {"'xtick.major.size'": "0"})

    response_times = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    # colors
    td_beacon_color = "#08519C"
    td_no_beacon_color = "#6BAED6"
    td_untrained_color = "#006D2C"
    bottom_up_color = "#74C476"
    flatui = [td_beacon_color, td_no_beacon_color, td_untrained_color, bottom_up_color]

    # Draw a boxplot
    boxplot = sns.boxplot(x="Condition", y="ResponseTime", data=response_times, palette=sns.color_palette(flatui))

    # set axes dimensions & labels
    boxplot.set(ylim=(0, 35000))
    boxplot.set(ylabel='Response Time in msec')

    # remove lines around graph
    sns.despine(bottom=True, trim=True)

    # save output as file, in a high resolution
    fig = boxplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)
