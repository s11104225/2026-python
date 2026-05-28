# Week 14（115/05/25－115/05/31）

- 主題：測試、除錯與例外 + 綜合練習
- 課堂範例：[`in_class/`](./in_class/) — Python3 Cookbook 第 14 章，依 Bloom's Taxonomy 分為 R/U 兩層共 5 個範例
- 解題：[11349](./QUESTION-11349.md) | [11417](./QUESTION-11417.md) | [11461](./QUESTION-11461.md) | [12019](./QUESTION-12019.md)
- 作業：完成 4 題並提交到 `weeks/week-14/solutions/<student-id>/`

---

## 課堂範例（in_class/）

涵蓋教材：[Python3 Cookbook 第 14 章：測試、調試和異常](https://python3-cookbook.readthedocs.io/zh-cn/latest/chapters/p14_test_debug_and_exceptions.html)

### 記憶層（R — Remember）

| 檔案 | 涵蓋節次 | 主題 |
|------|----------|------|
| [R01](./in_class/R01-unittest-basics.py) | 14.1–14.3 | unittest 基礎：`redirect_stdout` / `mock.patch` / `assertRaises` |
| [R02](./in_class/R02-exceptions-basic.py) | 14.6–14.8 | 例外處理基本：多例外 tuple / `except Exception` / 自定義例外 |
| [R03](./in_class/R03-profile-basic.py) | 14.13 | 效能測量：`timed` 裝飾器 / `timeit` / `cProfile` |

### 理解層（U — Understand）

| 檔案 | 涵蓋節次 | 主題 |
|------|----------|------|
| [U01](./in_class/U01-test-warnings-why.py) | 14.4, 14.5, 14.11 | 測試控制與警告：`skipIf` 的報表價值 / `stacklevel=2` / Warning 種類選擇 |
| [U02](./in_class/U02-debug-speedup-why.py) | 14.9, 14.10, 14.12, 14.14 | 例外、除錯與加速：四種 raise 寫法對照 / `print_exc` 必要性 / `LOAD_FAST` vs `LOAD_GLOBAL` |

詳細說明見 [`in_class/README.md`](./in_class/README.md)。

---

## 解題清單

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 11349 | UVA 11349 — Symmetric Matrix | ⭐ | [QUESTION-11349.md](./QUESTION-11349.md) |
| 11417 | UVA 11417 — GCD | ⭐ | [QUESTION-11417.md](./QUESTION-11417.md) |
| 11461 | UVA 11461 — Square Numbers | ⭐ | [QUESTION-11461.md](./QUESTION-11461.md) |
| 12019 | UVA 12019 — Doom's Day Algorithm | ⭐ | [QUESTION-12019.md](./QUESTION-12019.md) |
