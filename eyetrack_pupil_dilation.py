import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats, random, math
from os import path
from PIL import Image
import statsmodels.api as sm

import luminosity

IMAGE_PATH = 'C:/Users/npeitek/Documents/OgamaExperiments/fMRI_Eyetracking_Mar_13/SlideResources'
INPUT_PATH = 'C:/Users/npeitek/Documents/GitHub/EyeLinkOgamaConnector/output/'
OUTPUT_PATH = 'output/'


def draw_timeline_over_time_all_participants(input_file, output_file, with_gaze=False, select_participant=None, limited=False):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)

    if limited:
        f, ax = plt.subplots(figsize=(10, 3))
    else:
        f, ax = plt.subplots(figsize=(80, 6))

    ax.xaxis.grid(False)

    if with_gaze:
        output_file += '_gaze'

    if limited:
        output_file += '_lim'

    if select_participant is not None:
        eyetrack = eyetrack[eyetrack["subject"] == select_participant]
        output_file += '_' + select_participant + '.png'
    else:
        output_file += '.png'

    if limited:
        eyetrack = eyetrack[:650]

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="pupil_dilation", color=colors[0], legend=True)

    if with_gaze:
        eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="gaze_x", color=colors[-1])
        eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="gaze_y", color=colors[-2])

        import eyetrack_aoi_task_count_bar
        eyetrack_aoi_task_count_bar.printColor(colors[0])
        eyetrack_aoi_task_count_bar.printColor(colors[-1])
        eyetrack_aoi_task_count_bar.printColor(colors[-2])

    xpos = 0
    if limited:
        ypos = 2300
    else:
        ypos = 0

    for i in range(25):
        xpos += 320.05
        plt.text(xpos-300, ypos, 'Comprehension', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 150.05
        plt.text(xpos - 130, ypos, 'D2', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 200.05
        plt.text(xpos - 180, ypos, 'Rest', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

    eyetrack_tsplot.set(xlabel='Time in 10th of second')
    eyetrack_tsplot.set(ylabel='Pupil Dilation as area | Gaze Pos')

    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)


def get_corrected_pupil_dilation(row):
    pupil_dilation = row['pupil_dilation']
    gaze_x = row['gaze_x']
    gaze_y = row['gaze_y']

    pupil_dilation_corrected = pupil_dilation - 0.721 - (-0.187*gaze_x) - (0.249*gaze_y)
    return pupil_dilation_corrected


def draw_corrected_timeline_over_time_all_participants(input_file, output_file, with_gaze=False, select_participant=None, limited=False):
    global eyetrack
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)

    if limited:
        f, ax = plt.subplots(figsize=(10, 3))
    else:
        f, ax = plt.subplots(figsize=(80, 6))

    ax.xaxis.grid(False)

    if with_gaze:
        output_file += '_gaze'

    if limited:
        output_file += '_lim'

    if select_participant is not None:
        eyetrack = eyetrack[eyetrack["subject"] == select_participant]
        output_file += '_' + select_participant + '.png'
    else:
        output_file += '.png'

    if limited:
        eyetrack = eyetrack[:650]

    # mean normalization
    eyetrack['pupil_dilation'] = (eyetrack['pupil_dilation'] - eyetrack['pupil_dilation'].mean()) / eyetrack['pupil_dilation'].std()
    eyetrack['gaze_x'] = (eyetrack['gaze_x'] - eyetrack['gaze_x'].mean()) / eyetrack['gaze_x'].std()
    eyetrack['gaze_y'] = (eyetrack['gaze_y'] - eyetrack['gaze_y'].mean()) / eyetrack['gaze_y'].std()

    # min-max normalization
    #eyetrack['pupil_dilation'] = (eyetrack['pupil_dilation'] - eyetrack['pupil_dilation'].min()) / (eyetrack['pupil_dilation'].max() - eyetrack['pupil_dilation'].min())
    #eyetrack['gaze_x'] = (eyetrack['gaze_x'] - eyetrack['gaze_x'].min()) / (eyetrack['gaze_x'].max() - eyetrack['gaze_x'].min())
    #eyetrack['gaze_y'] = (eyetrack['gaze_y'] - eyetrack['gaze_y'].min()) / (eyetrack['gaze_y'].max() - eyetrack['gaze_y'].min())

    eyetrack['pupil_dilation_corrected'] = eyetrack.apply(lambda row: get_corrected_pupil_dilation(row), axis=1)

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="pupil_dilation", color=colors[0], legend=True)
    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="pupil_dilation_corrected", color=colors[1], legend=True)

    if False and with_gaze:
        eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="gaze_x", color=colors[-1])
        eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", value="gaze_y", color=colors[-2])

        import eyetrack_aoi_task_count_bar
        eyetrack_aoi_task_count_bar.printColor(colors[0])
        eyetrack_aoi_task_count_bar.printColor(colors[1])
        eyetrack_aoi_task_count_bar.printColor(colors[-1])
        eyetrack_aoi_task_count_bar.printColor(colors[-2])

    xpos = 0
    if limited:
        ypos = 2300
    else:
        ypos = 0

    for i in range(25):
        xpos += 320.05
        plt.text(xpos-300, ypos, 'Comprehension', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 150.05
        plt.text(xpos - 130, ypos, 'D2', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

        xpos += 200.05
        plt.text(xpos - 180, ypos, 'Rest', fontsize=14)
        plt.axvline(x=xpos, color=colors[2])

    eyetrack_tsplot.set(xlabel='Time in 10th of second')
    eyetrack_tsplot.set(ylabel='Normalized Pupil Dilation')

    # remove lines around graph
    sns.despine(trim=True)
    plt.tight_layout()

    # save output as file, in a high resolution
    fig = eyetrack_tsplot.get_figure()
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)


def draw_timeline_per_conditions(input_file, output_file, filter=False, participant=None):
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(10, 6))
    ax.xaxis.grid(False)

    if filter:
        eyetrack = eyetrack[eyetrack["condition"].isin(["Compr_BU", "Compr_TD_B", "Compr_TD_N", "Compr_TD_U", "Syntax", "Rest"])]
        eyetrack['condition'] = eyetrack['condition'].replace({'Compr_BU': 'Bottom-up', 'Compr_TD_B': 'Top-Down (Beacon)', 'Compr_TD_U': 'Top-Down (Untrained)', 'Compr_TD_N': 'Top-Down (No Beacon)'})

    eyetrack = eyetrack.rename(columns={'condition': 'Task Condition'})

    if participant is not None:
        eyetrack = eyetrack[eyetrack["subject"] == participant]
        output_file += '_' + participant + '.png'
    else:
        output_file += '.png'

    eyetrack_tsplot = sns.tsplot(data=eyetrack, time="time", unit="subject", condition="Task Condition", value="pupil_dilation", err_style=None)

    eyetrack_tsplot.set(xlabel='Time in 10th of Second within Each Condition')
    eyetrack_tsplot.set(ylabel='Pupil Dilation Area (Arbitrary Unit)')

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


def get_brightness(row, quick_and_dirty=False):
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

    if quick_and_dirty:
        return calculate_brightness(path.join(IMAGE_PATH, snippet))

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


def calculate_blink_rate(row):
    amount_participants = 8

    blink_rate = (row["amount_blinks"] / amount_participants) * 2
    return blink_rate


def analyze_blink_rates_per_snippet(input_file):
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    eyetrack = eyetrack.groupby(['condition','snippet'], as_index=False)['blink_rate'].count()

    eyetrack = eyetrack.rename(columns={'blink_rate': 'amount_blinks'})

    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("D2")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("DecTime")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("Rest")]

    eyetrack['blink_rate'] = eyetrack.apply(lambda row: calculate_blink_rate(row), axis=1)

    print(eyetrack.to_string())


def analyze_pupil_dilation_per_snippet(input_file):
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    eyetrack = eyetrack.groupby(['subject','condition','snippet'], as_index=False)['pupil_dilation'].mean()

    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("D2")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("DecTime")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("Rest")]

    eyetrack['brightness'] = eyetrack.apply(lambda row: get_brightness(row, True), axis=1)

    print(eyetrack.to_string())

    pass


def analyze_pupil_dilation_per_condition(input_file):
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    eyetrack = eyetrack.groupby(['subject','condition','snippet'], as_index=False)['pupil_dilation'].mean()

    eyetrack['brightness'] = eyetrack.apply(lambda row: get_brightness(row, True), axis=1)

    eyetrack = eyetrack.groupby(['subject','condition'], as_index=False).mean()

    print(eyetrack.to_string())

    pass


def draw_timeline_per_snippet_brightness(input_file, output_file, only_comprehension=False, sum_comprehension=False):
    # Load the long-form example gammas dataset
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')
    sns.set_style("whitegrid")
    colors = sns.color_palette("BrBG", 7)
    f, ax = plt.subplots(figsize=(10, 10))
    ax.xaxis.grid(False)

    # get the average pupil dilation of an entire snippet
    eyetrack = eyetrack.groupby(['subject','condition','snippet'], as_index=False)['pupil_dilation'].mean()

    # optionally only select snippets conditions
    if only_comprehension:
        eyetrack = eyetrack[~eyetrack['snippet'].str.contains("D2")]
        eyetrack = eyetrack[~eyetrack['snippet'].str.contains("DecTime")]
        eyetrack = eyetrack[~eyetrack['snippet'].str.contains("Rest")]

    if sum_comprehension:
        eyetrack['condition'] = eyetrack['condition'].replace({'Compr_BU': 'Comprehension', 'Compr_TD_B': 'Comprehension', 'Compr_TD_U': 'Comprehension', 'Compr_TD_N': 'Comprehension', 'Syntax': 'Comprehension'})
        eyetrack['condition'] = eyetrack['condition'].replace({'Comprehension': 'Code Display'})

    eyetrack = eyetrack.rename(columns={'condition': 'Task Condition'})

    eyetrack['brightness'] = eyetrack.apply(lambda row: get_brightness(row, True), axis=1)

    eyetrack_plot = sns.lmplot(data=eyetrack, x="brightness", y="pupil_dilation", hue="Task Condition", ci=None, fit_reg=True, aspect=2, legend_out=False)

    if False:
        y = eyetrack["pupil_dilation"]
        x = eyetrack["brightness"]

        for i in x:
            print(i)

        print("----")

        for i in y:
            print(i)

    # remove lines around graph
    #sns.despine(trim=True)
    eyetrack_plot.set(ylim=(1000,1900))
    eyetrack_plot.set(xlabel='Image Brightness of Code Snippet')
    eyetrack_plot.set(ylabel='Pupil Dilation Area (Arbitrary Unit)')

    # once for each algorithm (fast, or slow)
    #plt.text(0.18, 1350, 'r²=0.18', fontsize=10)
    plt.text(4.8, 1350, 'r²=0.18', fontsize=10)

    # save output as file, in a high resolution
    fig = eyetrack_plot.fig
    fig.savefig(path.join(OUTPUT_PATH, output_file), dpi=300, transparent=False)