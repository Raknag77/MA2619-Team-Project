import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from functools import partial
from typing import Literal

my_data = pd.read_excel("CycleData.xlsx", index_col=0)
figsize = (20, 5)

def validate_input(prompt: str, acceptable_values: list[str]):
    result = input(prompt)
    while result not in acceptable_values:
        print(f"Your input must be one of: {', '.join(acceptable_values)}")
        result = input(prompt)
    return result

def _make_plot_with_data(data: pd.DataFrame, _period_type: Literal["T", "D"], title: str) -> plt:
    x_col = "Full_time"  # _period_type = "D"
    if period_type == "T":
        x_col = "Time"

    plt.figure(figsize=figsize)
    sns.scatterplot(data, x=x_col, y="Count", hue=shade)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel("Count")
    plt.legend(title=shade)
    return plt

def create_plot(station, shade, period_type):  # noqa: Scope warning
    global figsize, my_data

    station_data = my_data[my_data["Station"] == station]
    plot = _make_plot_with_data(station_data, period_type, f"Scatterplot for station: {station}")
    plot.show()

def create_plot_with_mode(station, shade, period_type):  # noqa: Scope warning
    global my_data, figsize

    station_data = my_data[my_data["Station"] == station]
    station_data = station_data[station_data["Mode"] == "Private cycles"]
    _make_plot_with_data(station_data, period_type, f"Scatterplot for station: {station} with 'Private cycles' Mode").show()


def create_plot_with_direction(station, shade, period_type, direction):  # noqa: Scope warning
    global my_data, figsize

    station_data = my_data[my_data["Station"] == station]
    station_data = station_data[station_data["Direction"] == direction]
    _make_plot_with_data(station_data, period_type, f"Scatterplot for station: {station} with Direction").show()


def create_plot_with_direction_and_mode(station, shade, period_type, direction):  # noqa: Scope warning
    global my_data, figsize

    station_data = my_data[my_data["Station"] == station]
    station_data = station_data[station_data["Direction"] == direction]
    station_data = station_data[station_data["Mode"] == "Private cycles"]

    _make_plot_with_data(station_data, period_type, f"Scatterplot for station: {station} with Direction and 'Private cycles' Mode").show()


if __name__ == "__main__":
    station = validate_input("Enter desired station (ML0028/ML0032/ML0040): ", ["ML0028", "ML0032", "ML0040"])
    direction = validate_input("Enter desired direction (Any/Northbound/Southbound): ", ["Northbound", "Southbound", "Any"])
    private_only = validate_input("Do you want to restrict to private cycles only (Y/N)?: ", ["Y", "N"])
    period_type = validate_input("Do you want to display the date by time (T) or by date and time (D)?: ", ["T", "D"])
    shade = validate_input("Do you want to colour code by Weather, Direction, or Mode?: ",
                           ["Weather", "Direction", "Mode"])

    if private_only == "Y":
        plt_func = partial(create_plot_with_mode, station, shade, period_type)
        if direction != "Any":
            plt_func = partial(create_plot_with_direction_and_mode, station, shade, period_type, direction)
    else:
        if direction != "Any":
            plt_func = partial(create_plot_with_direction, station, shade, period_type, direction)
        else:
            plt_func = partial(create_plot, station, shade, period_type)
    plt_func()