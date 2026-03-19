# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
# 範例字串同時包含：空白、分號、逗號。
line = "asdf fjdk; afed, fjek,asdf, foo"

# re.split(pattern, text)：用正則規則切字串。
# [;,\s] 代表「任一個分隔符」：分號 ;、逗號 ,、或空白 \s。
# \s* 代表後面可接 0~多個空白，避免切完殘留多餘空格。
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲分組：分組但不保留分隔符
# (?:a|b|c) 用來表示多選一，
# 與一般分組 (a|b|c) 不同，?: 代表「只分組不捕獲」；
# 這樣 split 結果只會留下內容片段，不會把分隔符也放進結果。
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
# endswith / startswith 速度快、語意清楚，
# 適合做副檔名、前綴協定（例如 file:, http:）檢查。
print(filename.endswith(".txt"))  # True # .doc, .docx
print(filename.startswith("file:"))  # False

# 同時檢查多種後綴 → 傳入 tuple（不能傳 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
# 這裡只保留 C/C Header 檔案。
# name.endswith((".c", ".h")) 會檢查任一後綴符合即可。
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
# fnmatch 使用 shell 風格萬用字元：
# * 代表任意長度字元、? 代表單一字元、[0-9] 代表字元集合範圍。
print(fnmatch("foo.txt", "*.txt"))  # True
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# fnmatchcase 強制區分大小寫
# 當你需要跨平台固定行為（不依系統大小寫習慣）時，
# 建議使用 fnmatchcase 讓比對規則更可預期。
print(fnmatchcase("foo.txt", "*.TXT"))  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
# 只篩出以 " ST" 結尾的地址（注意前面有空白，可避免誤匹配）。
print([a for a in addresses if fnmatchcase(a, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
