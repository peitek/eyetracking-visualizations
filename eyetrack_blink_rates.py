import pandas as pd
from os import path

from config import INPUT_PATH


def calculate_blink_rate(row):
    amount_participants = 8

    blink_rate = (row["amount_blinks"] / amount_participants) * 2
    return blink_rate


def analyze_blink_duration_per_snippet(input_file):
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    eyetrack = eyetrack.groupby(['condition', 'snippet'], as_index=False)['blink_rate'].mean()

    eyetrack = eyetrack.rename(columns={'blink_rate': 'blink_duration'})

    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("DecTime")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("D2")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("Rest")]

    print(eyetrack.to_string())


def analyze_blink_duration_per_condition(input_file):
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    eyetrack = eyetrack.groupby(['condition'], as_index=False)['blink_rate'].mean()

    eyetrack = eyetrack.rename(columns={'blink_rate': 'blink_duration'})

    #eyetrack = eyetrack[~eyetrack['snippet'].str.contains("DecTime")]
    #eyetrack = eyetrack[~eyetrack['snippet'].str.contains("D2")]
    #eyetrack = eyetrack[~eyetrack['snippet'].str.contains("Rest")]

    print(eyetrack.to_string())


def analyze_blink_rates_per_snippet(input_file):
    eyetrack = pd.read_csv(path.join(INPUT_PATH, input_file), sep=';')

    eyetrack = eyetrack.groupby(['condition','snippet'], as_index=False)['blink_rate'].count()

    eyetrack = eyetrack.rename(columns={'blink_rate': 'amount_blinks'})

    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("D2")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("DecTime")]
    eyetrack = eyetrack[~eyetrack['snippet'].str.contains("Rest")]

    eyetrack['blink_rate'] = eyetrack.apply(lambda row: calculate_blink_rate(row), axis=1)

    print(eyetrack.to_string())
