"""
intersectionとsortにかかる時間を比較するための測定用コード(by GPT)
"""

import timeit
from random import randint, seed

# ----- 設定 -----
NUMBER_OF_ITERATION = 10**3  # 繰り返し回数
MAX_VALUE = 10**5  # 乱数の最大値
N = 10**5  # 配列の長さ

# 再現性を少し上げたい場合はシード固定（不要なら消してOK）
seed(0)

a = [randint(0, MAX_VALUE) for _ in range(N)]
b = [randint(0, MAX_VALUE) for _ in range(N)]


# 時間の単位を見やすく整形
def fmt_seconds(s: float) -> str:
    if s < 1e-6:
        return f"{s * 1e9:.2f} ns"
    if s < 1e-3:
        return f"{s * 1e6:.2f} µs"
    if s < 1:
        return f"{s * 1e3:.2f} ms"
    return f"{s:.3f} s"


def measure(label: str, func, number: int = NUMBER_OF_ITERATION):
    total = timeit.timeit(func, number=number)  # func は引数なし呼び出し可能
    per = total / number
    print(
        f"{label:<28}  total: {fmt_seconds(total):>9}   per-op: {fmt_seconds(per):>9}   n={number:,}"
    )


print(
    f"Dataset: N={N:,}, MAX_VALUE={MAX_VALUE:,}, NUMBER_OF_ITERATION={NUMBER_OF_ITERATION:,}\n"
)

# a と b の積集合（毎回 set(a) を作って list b と交差を取る）
measure("intersection(set(a), b)", lambda: set(a).intersection(b))

# 一度だけ交差を作成
c = set(a).intersection(b)

# c をソート
measure("sorted(c)", lambda: sorted(c))

# 参考（サイズ）
print(f"\nSizes -> |a|={len(a):,}, |b|={len(b):,}, |c|={len(c):,}")
