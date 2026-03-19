# R15. pandas DataFrame 分組 groupby 範例

import pandas as pd


def main() -> None:
    # 建立範例資料：每一列代表一筆交易。
    df = pd.DataFrame(
        {
            "city": ["Taipei", "Taipei", "Taichung", "Kaohsiung", "Taichung", "Kaohsiung"],
            "product": ["A", "B", "A", "A", "B", "B"],
            "sales": [120, 80, 100, 90, 70, 110],
            "price": [30, 20, 25, 22, 18, 27],
        }
    )

    print("=== 原始資料 ===")
    print(df)
    print()

    # 依 city 分組，並針對不同欄位做聚合：
    # - total_sales: 該城市 sales 總和
    # - avg_price: 該城市 price 平均
    # - order_count: 該城市資料筆數
    result = (
        df.groupby("city", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            avg_price=("price", "mean"),
            order_count=("sales", "count"),
        )
    )

    print("=== 依 city 分組後的統計 ===")
    print(result)


if __name__ == "__main__":
    main()

