# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

# OrderedDict 是 dict 的子類別，
# 核心用途是「明確保留插入順序」，並提供一些順序操作能力。
#
# 補充：Python 3.7+ 一般 dict 也保留插入順序，
# 因此在許多情境下可直接使用 dict；
# 但 OrderedDict 在語意表達與特定 API（例如 move_to_end）上仍有價值。
from collections import OrderedDict

# 建立有序字典。
d = OrderedDict()

# 依序插入鍵值。
# 這裡先插入 foo，再插入 bar。
d['foo'] = 1
d['bar'] = 2

# 關鍵取捨：
# 1) 優點：可預期的順序行為，適合需要依插入順序輸出/處理資料的情境。
# 2) 成本：為了追蹤順序，需要額外資料結構，通常比一般 dict 更耗記憶體。
# 3) 實務建議：
#    - 只要「保留插入順序」且無特殊順序操作需求，通常 dict 就夠用。
#    - 若需要明確的順序語意或進階順序操作，再選 OrderedDict。
