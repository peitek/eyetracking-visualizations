import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from os import path

from config import INPUT_PATH, OUTPUT_PATH


def draw_eyetrack_spatial_error_plot(input_file, output_file, individual_lines=False, trend_line=True, individual_axis=False):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(8, 3))
    ax.xaxis.grid(False)

    def draw_linear_trendline_for_axis(axis, color):
        global color_map
        x_axis = eyetrack[eyetrack.axis == axis]
        x_axis_time = x_axis.time.values
        x_axis_values = x_axis.value.values
        # plot line of generated linear fit
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_axis_time, x_axis_values)
        line = slope * x_axis_time + intercept
        plt.plot(x_axis_time, line, color=color, linewidth=1)

    if trend_line:
        draw_linear_trendline_for_axis('x', colors[1])
        draw_linear_trendline_for_axis('y', colors[-2])

    color_map = {
        'x': colors[0],
        'y': colors[-1],
    }

    # Plot the response with standard error
    if individual_lines:
        # individual error lines with average
        if individual_axis:
            eyetrack_tsplot = sns.tsplot(data=eyetrack[eyetrack.axis == individual_axis], time="time", unit="subject", condition="axis", value="value", err_style="unit_traces", color=color_map, legend=False)
        else:
            eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="axis", value="value", err_style="unit_traces", color=color_map, legend=False)

        # each line as individual line
        #eyetrack_tsplot = sns.tsplot(data=eyetrack[eyetrack.subject == 'bo23'], time="time", unit="subject", condition="axis", value="value", color=color_map)
        #eyetrack_tsplot = sns.tsplot(data=eyetrack[eyetrack.subject == 'ea65'], time="time", unit="subject", condition="axis", value="value", color=color_map)
    else:
        eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="axis", value="value", color=color_map)

    # eyetrack_tsplot = sns.regplot(data=eyetrack, time="time", unit="subject", condition="axis", value="value")

    # customization in design
    eyetrack_tsplot.set(xticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    # eyetrack_tsplot.set(xlim=(0, 25))
    #eyetrack_tsplot.set(ylim=(0))
    eyetrack_tsplot.set(ylim=(0, 270))
    eyetrack_tsplot.set(ylabel='Spatial Error from Fixation Cross in Pixel')
    eyetrack_tsplot.set(xlabel='Rest Condition')


    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # show interactively
    # plt.title("title")
    # plt.show(eyetrack_tsplot)

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)
