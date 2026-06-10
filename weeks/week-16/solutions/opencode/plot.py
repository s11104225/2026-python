import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

_TITLE_FONT = FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc", size=14)
_LABEL_FONT = FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc", size=12)
_LEGEND_FONT = FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc", size=10)


def load_results(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def plot_results(results: dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    sizes = sorted(int(n) for n in next(iter(results.values())).keys())
    plt.figure(figsize=(10, 6))

    for name, data in results.items():
        means = [data[str(n)]["mean"] for n in sizes]
        plt.plot(sizes, means, marker="o", label=name)

    plt.xlabel("資料量 n", fontproperties=_LABEL_FONT)
    plt.ylabel("平均耗時 (秒)", fontproperties=_LABEL_FONT)
    plt.yscale("log")
    plt.title("排序演算法效能比較", fontproperties=_TITLE_FONT)
    plt.legend(prop=_LEGEND_FONT)
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
