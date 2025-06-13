from typing import TypedDict, Optional, Literal
from matplotlib.axes import Axes
import numpy as np

class LabelOptions(TypedDict):
    text: str
    rotation: float
    font: float

class BarsOptions(TypedDict, total=False):
    label: list[list[str]]
    color: list[str]
    anchor: Literal["center", "edge"]
    format: Literal["number", "currency"]
    rotation: float

def vertical_bar(
    ax: Axes,
    x_axis: list[str],
    y_axis: list[list[float]],
    tooltip: Optional[BarsOptions] = {},
    title: Optional[LabelOptions] = {"text": "Title", "font": 18},
    x_style: Optional[LabelOptions] = {"text": "Axis X", "rotation": 0, "font": 14},
    y_style: Optional[LabelOptions] = {"text": "Axis Y", "rotation": 0, "font": 14},
) -> Axes:

    bottom = np.zeros(len(x_axis))
    format_type = tooltip.get("format", "number")
    format_str = "{:,.0f}" if format_type == "number" else "{:,.2f}"

    default_colors = [f"#00{i}" for i in range(len(y_axis))]
    colors = tooltip.get("color", default_colors)

    for index, value in enumerate(y_axis):

        bar = ax.bar(
            x=x_axis,
            height=value,
            bottom=bottom,
            color=colors[index % len(colors)],
            label = tooltip.get(
                "label",
                    [
                        f"Type {i}" for i in range(1, len(x_axis) + 1)
                    ]      
                )[index]
        )

        bottom += value

        ax.bar_label(
            container=bar,
            fmt=lambda v: format_str.format(v).replace(".", ";").replace(",", ".").replace(";", ","),
            label_type=tooltip.get("anchor", "center"),
            rotation=tooltip.get("rotation", 0)
        )

    ax.set_title(title.get("text", ""), fontsize=title.get("font", 18))
    ax.set_xlabel(x_style.get("text", ""), fontsize=x_style.get("font", 14))
    ax.set_ylabel(y_style.get("text", ""), fontsize=y_style.get("font", 14))
    ax.tick_params(axis="x", labelrotation=x_style.get("rotation", 0))
    ax.tick_params(axis="y", labelrotation=y_style.get("rotation", 0))

    ax.legend()
    ax.set_yticks([])

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    return ax


def horizontal_bar(
    ax: Axes,
    y_axis: list[str],
    x_axis: list[list[float]],
    tooltip: Optional[BarsOptions] = {},
    title: Optional[LabelOptions] = {"text": "Title", "font": 18},
    x_style: Optional[LabelOptions] = {"text": "Axis X", "rotation": 0, "font": 14},
    y_style: Optional[LabelOptions] = {"text": "Axis Y", "rotation": 0, "font": 14},
) -> Axes:

    left = np.zeros(len(y_axis))
    format_type = tooltip.get("format", "number")
    format_str = "{:,.0f}" if format_type == "number" else "{:,.2f}"

    default_colors = [f"#00{i}" for i in range(len(y_axis))]
    colors = tooltip.get("color", default_colors)

    for index, value in enumerate(x_axis):

        bar = ax.barh(
            y=y_axis,
            width=value,
            left=left,
            color=colors[index % len(colors)],
            label = tooltip.get(
                "label",
                    [
                        f"Type {i}" for i in range(1, len(x_axis) + 1)
                    ]      
                )[index]
        )

        left += value

        ax.bar_label(
            container=bar,
            fmt=lambda v: format_str.format(v).replace(".", ";").replace(",", ".").replace(";", ","),
            label_type=tooltip.get("anchor", "center"),
            rotation=tooltip.get("rotation", 0)
        )

    ax.set_title(title.get("text", ""), fontsize=title.get("font", 18))
    ax.set_xlabel(x_style.get("text", ""), fontsize=x_style.get("font", 14))
    ax.set_ylabel(y_style.get("text", ""), fontsize=y_style.get("font", 14))
    ax.tick_params(axis="x", labelrotation=x_style.get("rotation", 0))
    ax.tick_params(axis="y", labelrotation=y_style.get("rotation", 0))

    ax.legend()
    ax.set_xticks([])

    for spine in ["top", "right", "bottom"]:
        ax.spines[spine].set_visible(False)

    return ax
