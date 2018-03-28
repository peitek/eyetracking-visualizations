import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats, random, math
from os import path
from PIL import Image

import luminosity

IMAGE_PATH = 'C:/Users/npeitek/Documents/OgamaExperiments/fMRI_Eyetracking_Mar_13/SlideResources'
INPUT_PATH = 'C:/Users/npeitek/Documents/GitHub/EyeLinkOgamaConnector/output/'
OUTPUT_PATH = 'output/'


def draw_timeline_over_time_all_participants(input_file, output_file, with_gaze=False, select_participant=None):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(80, 6))
    ax.xaxis.grid(False)

    if with_gaze:
        output_file += '_gaze'

    if select_participant is not None:
        eyetrack = eyetrack[eyetrack["subject"] == select_participant]
        output_file += '_' + select_participant + '.png'
    else:
        output_file += '.png'

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="pupil_dilation", color=colors[0])

    if with_gaze:
        eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="gaze_x", color=colors[-1])
        eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="gaze_y", color=colors[-2])

    xpos = 0
    for i in range(25):
        xpos += 320.05
        plt.text(xpos-300, 0, 'Comprehension', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 150.05
        plt.text(xpos - 130, 0, 'D2', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 200.05
        plt.text(xpos - 180, 0, 'Rest', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

    eyetrack_tsplot.set(xlabel='Time in 10th of second')
    eyetrack_tsplot.set(ylabel='Pupil Dilation as area | Gaze Pos')

    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)


def draw_timeline_per_conditions(input_file, output_file, participant=None):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(10, 6))
    ax.xaxis.grid(False)

    if participant is not None:
        eyetrack = eyetrack[eyetrack["subject"] == participant]
        output_file += '_' + participant + '.png'
    else:
        output_file += '.png'

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="condition", value="pupil_dilation", err_style=None)

    #eyetrack_tsplot.set(xlabel='Time in 10th of second')
    #eyetrack_tsplot.set(ylabel='Pupil Dilation as area')

    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)


def draw_timeline_per_snippet(input_file, output_file, group=None):
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(10, 6))
    ax.xaxis.grid(False)

    if group is not None:
        eyetrack = eyetrack[eyetrack["condition"] == group]
        output_file += '_' + group + '.png'
    else:
        output_file += '.png'

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="snippet", value="pupil_dilation", err_style=None)

    #eyetrack_tsplot.set(xlabel='Time in 10th of second')
    #eyetrack_tsplot.set(ylabel='Pupil Dilation as area')

    # remove lines around graph
    sns.despine(trim=True)

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)


def draw_timeline_per_snippet_compare(input_file, output_file, snippet1, snippet2):
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(10, 6))
    ax.xaxis.grid(False)

    eyetrack = eyetrack[eyetrack["snippet"].isin([snippet1, snippet2])]

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="snippet", value="pupil_dilation", err_style=None)

    #eyetrack_tsplot.set(xlabel='Time in 10th of second')
    #eyetrack_tsplot.set(ylabel='Pupil Dilation as area')

    # remove lines around graph
    sns.despine(trim=True)

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)


def get_brightness(row):
    snippet = row['snippet']

    if 'DecTime' in snippet:
        snippet = snippet.replace('DecTime', 'dec_time_')
        snippet += '.png'

    if 'D2' in snippet:
        snippet = snippet.replace('D2', 'attention_task')
        snippet += '.png'

    if 'Rest' in snippet:
        snippet = snippet.replace('Rest', 'rest_')
        snippet += '.png'

    #return calculate_brightness(path.join(IMAGE_PATH, snippet))
    brightness = luminosity.get_brightness(path.join(IMAGE_PATH, snippet))
    print(snippet + " has a brightness of " + str(brightness))
    return brightness


def calculate_brightness(image_path):
    image = Image.open(image_path)
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else (brightness / scale) * 10


def draw_timeline_per_snippet_brightness(input_file, output_file, only_comprehension=False):
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(10, 10))
    ax.xaxis.grid(False)

    # get the average pupil dilation of an entire snippet
    eyetrack = eyetrack.groupby(['subject','condition','snippet'], as_index=False)['pupil_dilation'].mean() \

    # optionally only select snippets conditions
    if only_comprehension:
        eyetrack = eyetrack[~eyetrack['snippet'].str.contains("D2")]
        eyetrack = eyetrack[~eyetrack['snippet'].str.contains("DecTime")]
        eyetrack = eyetrack[~eyetrack['snippet'].str.contains("Rest")]

    eyetrack['brightness'] = eyetrack.apply(lambda row: get_brightness(row), axis=1)

    eyetrack_plot = sns.lmplot(data=eyetrack, x="brightness", y="pupil_dilation", hue="condition", ci=None, legend_out=False)

    # remove lines around graph
    sns.despine(trim=True)
    eyetrack_plot.set(ylim=(900,2000))
    eyetrack_plot.set(xlabel='Code Image Brightness')
    eyetrack_plot.set(ylabel='Pupil Dilation as area')

    # save output as file, in a high resolution
    fig = eyetrack_plot.fig
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)