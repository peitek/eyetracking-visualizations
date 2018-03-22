import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from os import path

INPUT_PATH = 'input/'
OUTPUT_PATH = 'output/'


def draw_eyetrack_spatial_error_plot(input_file, output_file):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("RdBu_r", 7)
    f, ax = plt.subplots(figsize=(8, 3))
    ax.xaxis.grid(False)

    color_map = {
        'inner': colors[0],
        '25px': colors[-3],
        '50px': colors[-1],
    }

    # Plot the response with standard error
    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="aoi", value="value", color=color_map)
    # eyetrack_tsplot = sns.regplot(data=eyetrack, time="time", unit="subject", condition="axis", value="value")

    # customization in design
    eyetrack_tsplot.set(xticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    # eyetrack_tsplot.set(xlim=(0, 25))
    eyetrack_tsplot.set(ylim=(0))
    eyetrack_tsplot.set(ylabel='Fixation Count in AOIs')
    eyetrack_tsplot.set(xlabel='Comprehension Snippet')

    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # show interactively
    # plt.title("title")
    # plt.show(eyetrack_tsplot)

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)
