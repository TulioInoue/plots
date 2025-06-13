from typing import TypedDict, Literal, Optional
from matplotlib.axes import Axes

class DataOptions(TypedDict):
    x: list
    y: list[float]
    color: str
    marker: Literal['.',',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','_']
    linestyle: Literal['-', '--', '-.', ':']
    linewidth: float
    markersize: float

class LabelOptions(TypedDict):
    text: str
    rotation: float
    font: float

def line(
    ax: Axes,
    datas: list[DataOptions],
    title: Optional[LabelOptions] = {"text": "Title", "rotation": 0, "font": 14},
    x_style: Optional[LabelOptions] = {"text": "Axis X", "rotation": 0, "font": 14},
    y_style: Optional[LabelOptions] = {"text": "Axis Y", "rotation": 0, "font": 14}
) -> Axes:

    [
        ax.plot(
            data['x'],
            data['y'],
            color = data.get("color", "blue"),
            marker = data.get("marker", ""),
            linestyle = data.get("linestyle", "-"),
            linewidth = data.get("linewidth", 1),
            markersize = data.get("markersize", 12),
        ) for data in datas
    ]

    ax.set_title(label = title.get("text", ""), fontsize = title.get("font", 18))
    ax.set_xlabel(xlabel = x_style.get("text", ""), fontsize = x_style.get("font", 14))
    ax.set_ylabel(ylabel = y_style.get("text", ""), fontsize = y_style.get("font", 14))
    ax.tick_params(axis = "x",labelrotation = x_style.get("rotation", 0))
    ax.tick_params(axis = "y",labelrotation = y_style.get("rotation", 0))
    
    ax.grid(visible = True, axis = "both")

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    return ax
