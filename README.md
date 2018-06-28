# Eye-Tracking Visualization

This repository contains a collection of Python scripts, which visualizes the eye-tracking data of our fMRI experiments.

**Disclaimer 1: The code is very specific to our use case and may need substantial changes to work with other setups.**
**Disclaimer 2: I am not a Python programmer. I'm always grateful for feedback on how to improve my code.**

## Setup

The project should run in any Python 3.6 environment. It was developed with the [PyCharms IDE](https://www.jetbrains.com/pycharm/).

## Work Flow ##

Before starting the Python script, prepare the data. It needs to have the format of our [analyzer scripts](https://github.com/peitek/eyetracking-analyses). The easiest way is to run the data through the analyzer first, then to visualize it.

Make necessary adjustments to `config.py`.

Finally, you can create the visualizations by executing `main.py`.

# Related Repositories

* [EyeLink Ogama Connector](https://github.com/peitek/eyelink-ogama-connector)
* [Eye-Tracking Analysis Pipeline](https://github.com/peitek/eyetracking-analyses)


# License #

```
MIT License

Copyright (c) 2018 Norman Peitek
```