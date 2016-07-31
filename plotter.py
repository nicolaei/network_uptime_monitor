#!/bin/python3
import sys
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt 

def get_filepaths():
    if len(sys.argv) is 1:
        print("Usage: plotter.py <log folder>")
        sys.exit(1)

    directory = listdir(sys.argv[1])

    return [sys.argv[1] + f for f in directory if isfile(sys.argv[1] + f)]


def get_values(filepaths):
    values = {}

    for filepath in filepaths:
        filename = "".join(filepath.split("/")[-1])
        values[filename] = {
                "datetimes": [],
                "average": [],
                "min": [],
                "max": [],
        }

        with open(filepath, 'r') as f:
            for line in f:
                # The datetime is the the first 2 sets of characters in the line
                values[filename]["datetimes"].append(" ".join(line.split(" ")[0:2]))

                # The pingtime is last in the file, with the format min/avg/max
                pingtimes = line.split(" ")[-1].split("/")
                values[filename]["min"].append(pingtimes[0])
                values[filename]["average"].append(pingtimes[1])
                values[filename]["max"].append(pingtimes[2])

    return values


def draw(values):
    datetimes = values["datetimes"]
    min_time = values["min"]
    max_time = values["max"]
    average_time = values["average"]

    # Since pyplot is cumbersome, we have to make the datetimes into ticks.
    x = [i for i in range(0, len(datetimes))]
    plt.xticks([i for i in x[::(60*6)]], [i for i in datetimes[::(60*6)]], rotation=90) # Only show tick every 6 hours

    # Labeling of the axies
    plt.ylabel("Time in ms")

    for times in (min_time, max_time, average_time):
        plt.plot(x, times)

    # Set up the legend
    plt.legend(["Minimum", "Maximum", "Average"])


if __name__ == "__main__":
    filepaths = get_filepaths()
    values = get_values(filepaths)

    # Give each file it's own figure
    i = 0
    for target in values:
        i = i + 1

        figure = plt.figure(i)
        figure.canvas.set_window_title(target)
        draw(values[target])

    plt.show()
