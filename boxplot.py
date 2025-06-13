from typing import Optional, TypedDict, Literal
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

def box_plot(
    ax: Axes,
    array: list[list[float]],
    labels: list[str],
    colors: list[str],
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    title: Optional[LabelOptions] = {"text": "Title", "rotation": 0, "font": 18},
    x_style: Optional[LabelOptions] = {"text": "Axis X", "rotation": 0, "font": 14},
    y_style: Optional[LabelOptions] = {"text": "Axis Y", "rotation": 0, "font": 14},
) -> Axes:
    
    boxplot = ax.boxplot(
        x = array,
        orientation = orientation,
        patch_artist = True,
        tick_labels = labels
    )

    for patch, color in zip(boxplot["boxes"], colors):
        patch.set_facecolor(color)

    ax.set_title(title.get("text", ""), fontsize=title.get("font", 18))
    ax.set_xlabel(x_style.get("text", ""), fontsize=x_style.get("font", 14))
    ax.set_ylabel(y_style.get("text", ""), fontsize=y_style.get("font", 14))
    ax.tick_params(axis="x", labelrotation=x_style.get("rotation", 0))
    ax.tick_params(axis="y", labelrotation=y_style.get("rotation", 0))

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)


    return ax
