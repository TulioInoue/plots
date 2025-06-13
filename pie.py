from typing import Optional, TypedDict
from matplotlib.axes import Axes
import numpy as np

class LabelsOptions(TypedDict):
    text: str
    font: float

class ValuesOptions(TypedDict):
    colors: list[str]
    explode: list[float]
    counterclock: bool

def pie(
    ax: Axes,
    values: list[float],
    labels: list[str],
    values_style: Optional[ValuesOptions] = {},
    title: Optional[LabelsOptions] = {
        "text": "Title",
        "font": 18,
    },
) -> Axes:
    
    ax.pie(
        x = values,
        labels = labels,
        autopct = "%1.2f%%",
        colors = values_style.get("colors", ["pink", "turquoise", "darkcyan", "darkorange", "orange", "#f77", "#ff5", "#f55"]),
        explode = values_style.get("explode", np.zeros(len(values))),
        counterclock = values_style.get("counterclock", False),
    )

    ax.set_title(
        label = title["text"],
        fontsize = title["font"]
    )

    return ax