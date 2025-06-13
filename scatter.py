from typing import Optional, TypedDict
from matplotlib.axes import Axes

class StyleOptions(TypedDict):
    size: list[float]
    color: list[str]
    alpha: float
    edgecolors: str
    
class LabelOptions(TypedDict):
    text: str
    rotation: float
    font: float

def scatter(
    ax: Axes,
    x_array: list[float],
    y_array: list[float],
    style: Optional[StyleOptions] = {},
    title: Optional[LabelOptions] = {"text": "Title", "font": 18},
    x_style: Optional[LabelOptions] = {"text": "Axis X", "rotation": 0, "font": 14},
    y_style: Optional[LabelOptions] = {"text": "Axis Y", "rotation": 0, "font": 14},
) -> Axes:
    
    ax.scatter(
        x = x_array,
        y = y_array,
        s = style.get("size", None),
        c = style.get("color", None),
        alpha = style.get("alpha", 1),
        edgecolors = style.get("edgecolors", None)
    )

    ax.set_title(title.get("text", ""), fontsize=title.get("font", 18))
    ax.set_xlabel(x_style.get("text", ""), fontsize=x_style.get("font", 14))
    ax.set_ylabel(y_style.get("text", ""), fontsize=y_style.get("font", 14))
    ax.tick_params(axis="x", labelrotation=x_style.get("rotation", 0))
    ax.tick_params(axis="y", labelrotation=y_style.get("rotation", 0))

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    return ax