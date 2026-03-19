"""U6. defaultdict 為何比手動初始化乾淨（1.6）

使用同一份 bible.txt 做字數統計，比較兩種寫法：
1) 手動初始化：if key not in dict
2) defaultdict(int)：自動初始化
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re
import statistics
import timeit


def load_words() -> list[str]:
    """讀取同資料夾下的 bible.txt，回傳小寫英文詞彙清單。"""
    text = Path(__file__).with_name("bible.txt").read_text(encoding="utf-8")
    # 只保留英文單字（含可能出現的 apostrophe）做公平比較。
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.lower())


def count_manual(words: list[str]) -> dict[str, int]:
    """L9 風格：手動判斷並初始化。"""
    counts: dict[str, int] = {}
    for w in words:
        if w not in counts:
            counts[w] = 0
        counts[w] += 1
    return counts


def count_defaultdict(words: list[str]) -> dict[str, int]:
    """L14 風格：使用 defaultdict(int) 自動初始化。"""
    counts: defaultdict[str, int] = defaultdict(int)
    for w in words:
        counts[w] += 1
    return dict(counts)


def benchmark(words: list[str], repeat: int = 7, number: int = 5) -> None:
    """執行基準測試並輸出平均、最佳與速度提升比例。"""
    # 先驗證結果一致，確保比較的是同樣工作。
    manual_result = count_manual(words)
    default_result = count_defaultdict(words)
    if manual_result != default_result:
        raise RuntimeError("兩種方法統計結果不一致，請檢查邏輯。")

    t_manual = timeit.repeat(
        "count_manual(words)",
        globals={"count_manual": count_manual, "words": words},
        repeat=repeat,
        number=number,
    )
    t_default = timeit.repeat(
        "count_defaultdict(words)",
        globals={"count_defaultdict": count_defaultdict, "words": words},
        repeat=repeat,
        number=number,
    )

    manual_runs = [x / number for x in t_manual]
    default_runs = [x / number for x in t_default]

    manual_avg = statistics.mean(manual_runs)
    default_avg = statistics.mean(default_runs)
    manual_best = min(manual_runs)
    default_best = min(default_runs)

    print("=== Word Count Benchmark (bible.txt) ===")
    print(f"tokens: {len(words)}")
    print(f"unique words: {len(manual_result)}")
    print(f"manual avg: {manual_avg:.6f}s")
    print(f"defaultdict avg: {default_avg:.6f}s")
    print(f"manual best: {manual_best:.6f}s")
    print(f"defaultdict best: {default_best:.6f}s")

    if manual_avg < default_avg:
        speedup = (default_avg - manual_avg) / default_avg * 100
        print(f"faster: manual (L9), by {speedup:.2f}% on average")
    else:
        speedup = (manual_avg - default_avg) / manual_avg * 100
        print(f"faster: defaultdict (L14), by {speedup:.2f}% on average")


def main() -> None:
    words = load_words()
    benchmark(words)


if __name__ == "__main__":
    main()
