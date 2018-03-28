import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats
from os import path

INPUT_PATH = 'C:/Users/npeitek/Documents/GitHub/EyeLinkOgamaConnector/output/'
OUTPUT_PATH = 'output/'


def draw_timeline_over_time_all_participants(input_file, output_file):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(80, 6))
    ax.xaxis.grid(False)

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="pupil_dilation", err_style="unit_traces")

    xpos = 0
    for i in range(25):
        xpos += 320.05
        plt.text(xpos-300, 3300, 'Comprehension', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 150.05
        plt.text(xpos - 130, 3300, 'D2', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 200.05
        plt.text(xpos - 180, 3300, 'Rest', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])


    eyetrack_tsplot.set(xlabel='Time in 10th of second')
    eyetrack_tsplot.set(ylabel='Pupil Dilation as area')

    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)


def draw_timeline_per_conditions(input_file, output_file):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(10, 6))
    ax.xaxis.grid(False)

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="condition", value="pupil_dilation", err_style=None)

    #eyetrack_tsplot.set(xlabel='Time in 10th of second')
    #eyetrack_tsplot.set(ylabel='Pupil Dilation as area')

    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)