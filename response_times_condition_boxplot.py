import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def draw_response_times_plot(input_file, output_file):
    sns.set_style("ticks", {"'xtick.major.size'": "0"})
    # Load the example tips dataset
    response_times = pd.read_csv(input_file, sep=';')
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
    plt.show(boxplot)
    # save output as file, in a high resolution
    fig = boxplot.get_figure()
    fig.savefig(output_file, dpi=300)



