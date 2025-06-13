from histogram import histogram
import matplotlib.pyplot as plt
import numpy as np

from typing import TypedDict, Literal, Optional
from matplotlib.axes import Axes

class BarStyle(TypedDict):
    bins: int
    color: list[str]
    edgecolor: str
    histtype: Literal["bar", "step"]
    density: bool

class LabelOptions(TypedDict):
    text: str
    rotation: float
    font: float

def histogram(
    ax: Axes,
    x_array: list[list[float]],
    style: Optional[BarStyle] = {},
    title: Optional[LabelOptions] = {"text": "Title", "rotation": 0, "font": 18},
    x_style: Optional[LabelOptions] = {"text": "Axis X", "rotation": 0, "font": 14},
    y_style: Optional[LabelOptions] = {"text": "Axis Y", "rotation": 0, "font": 14},
) -> Axes:
    
    ax.hist(
        x = x_array,
        bins = style.get("bins", 20),
        density = style.get("density", False),
        histtype = style.get("histtype", "bar"),
        edgecolor = style.get("edgecolor", "lightgray"),
        color = style.get("color"),
    )

    ax.set_title(title.get("text", ""), fontsize=title.get("font", 18))
    ax.set_xlabel(x_style.get("text", ""), fontsize=x_style.get("font", 14))
    ax.set_ylabel(y_style.get("text", ""), fontsize=y_style.get("font", 14))
    ax.tick_params(axis="x", labelrotation=x_style.get("rotation", 0))
    ax.tick_params(axis="y", labelrotation=y_style.get("rotation", 0))

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    return ax
