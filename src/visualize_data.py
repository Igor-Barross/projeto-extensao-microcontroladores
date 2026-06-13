import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

charcoal = "#181818"
dark_gray = "#202020"
sky_blue = "#00A3E0"
teal = "#008D71"
red = "#FF0000"
gold = "#FFD700"
violet = "#BB86FC"
light_gray = "#E0E0E0"
medium_gray = "#444444"

color_palette = [sky_blue, teal, red, gold, violet]
text_color = light_gray


def setup_theme():
    sns.set_theme(
        style="darkgrid",
        rc={
            "figure.facecolor": charcoal,
            "axes.facecolor": dark_gray,
            "axes.edgecolor": light_gray,
            "axes.labelcolor": light_gray,
            "xtick.color": light_gray,
            "ytick.color": light_gray,
            "text.color": light_gray,
            "grid.color": medium_gray,
            "axes.titlecolor": light_gray,
            "figure.autolayout": True,
        },
    )
    sns.set_palette(color_palette)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["savefig.facecolor"] = charcoal
    plt.rcParams["savefig.edgecolor"] = charcoal
    plt.rcParams["font.size"] = 11


def save_bar_chart(series, title, xlabel, ylabel, output_path: Path, colors=None):  # noqa:  E501
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(series.index, series.values, color=colors)

    ax.set_title(title, fontsize=18, fontweight="bold", pad=15)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    for bar, valor in zip(bars, series.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + 0.15,
            str(int(valor)),
            ha="center",
            va="bottom",
            color=text_color,
            fontsize=11
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def save_barh_chart(series, title, xlabel, ylabel, output_path: Path):
    cores_barras = (color_palette * 10)[:len(series)]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.barh(series.index, series.values, color=cores_barras)

    ax.set_title(title, fontsize=18, fontweight="bold", pad=15)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    for i, valor in enumerate(series.values):
        ax.text(
            valor + 0.1,
            i,
            str(int(valor)),
            va="center",
            ha="left",
            color=text_color,
            fontsize=10
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
