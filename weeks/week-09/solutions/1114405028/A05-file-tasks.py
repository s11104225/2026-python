# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'a' 模式） ──────────────
# 規則：同一天可多次追寫一行時間戳。
from datetime import datetime

today = date.today().isoformat()          # 例如 2026-04-23
diary = Path(f"diary-{today}.txt")

with open(diary, "a", encoding="utf-8") as f:   # 'a' = append
    now = datetime.now().isoformat()
    f.write(f"{now}: 今天學了檔案 I/O。\n")
print(f"已附加到 {diary}")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 走訪目錄 → 逐檔逐行讀 → 累計三個數字
def count_py(folder: Path):
    total, nonblank, defs, comments = 0, 0, 0, 0
    for p in folder.rglob("*.py"):
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                s = line.strip()
                if s:
                    nonblank += 1
                if s.startswith("def "):
                    defs += 1
                if s.startswith("#"):
                    comments += 1
    return total, nonblank, defs, comments

target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    total, nonblank, defs, comments = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
    print(f"  註解行數     : {comments}")
    
    # 寫到 stats.tsv
    with open("stats.tsv", "wt", encoding="utf-8") as f:
        print("項目", "數量", sep="\t", file=f)
        print("總行數", total, sep="\t", file=f)
        print("非空白行", nonblank, sep="\t", file=f)
        print("def 起頭行數", defs, sep="\t", file=f)
        print("註解行數", comments, sep="\t", file=f)
    print("統計結果已寫到 stats.tsv")
else:
    print(f"示範目錄不存在：{target}")

# 已實作課堂延伸挑戰
