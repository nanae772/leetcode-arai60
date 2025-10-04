# ステップ１

与えられた二分木がBSTであることをvalidateする

- 部分木に含まれる最大値(get_max_subtree)
- 部分木に含まれる最小値(get_min_subtree)

の２つの関数を作っておいて、左部分木はget_max_subtreeで最大値を取り、右部分木はget_min_subtreeで最小値を取り、
それらを今見てるノードの値と比較してチェックするのを再帰的にやればよさそうなのでまずはそれを書いてみる。

入力では入ってこないことになっているが木が無いとき(root=Noneのとき)、true/falseどっちにするか悩んだがfalseにしておいた。
数学的にはtrueと判定するほうが正しそうだが、木が無いのに「これはBSTです」と判定されても実用的にはちょっと変な感じがする。

step1.pyではminを取る関数とmaxを取る関数を分けたが、min, maxを引数で渡して１つの関数にすることもできるので
そっちも書いてみた(step1-2.py)、こういう関数の名前はどうすればいいか分からないが。
あとfloat("inf")を使うのにやや抵抗があったためそれを使わないようにもしてみたがこれはこれで冗長な感じ。

# ステップ２

ステップ１で書いたコードは重大な欠陥があることに気づいた。
minやmaxを取る関数が同じノードに対して複数回呼ばれてしまうので最悪計算量がO(n^2)になってしまっている。
O(n^2)でn = 10^4の最大ケースだとPythonの実行速度ではとても1~2sで終わるものではなく
本来TLEしそうだがleetcode上のテストケースが弱かったのだろうか。

よくある再帰の組合せだからO(N)になってるだろうと安易に考えてしまい書く前に気づくことができなかった。

例えば 1 -> 2 -> 3 -> 4 という右に伸びたBSTを考えてみて

- valid: BSTか判定する関数
- min: 部分木の中の最小値を求める関数

として実行手順をたどってみると

1. topからvalid(1)を呼ぶ
2. valid(1)がvalid(2)を呼ぶ
3. valid(2)がvalid(3)を呼ぶ
4. valid(3)がvalid(4)を呼ぶ
5. valid(4)が4はleafなのでtrueを返す
6. valid(3)がmin(4)を呼ぶ
7. min(4)は4を返す
8. valid(3)は3 < 4なのでtrueを返す
9. valid(2)がmin(3)を呼ぶ
10. min(3)がmin(4)を呼ぶ
11. min(4)は4を返す
12. min(3)は3を返す
13. valid(2)は2 < 3なのでtrueを返す
14. valid(1)がmin(2)を呼ぶ
15. min(2)がmin(3)を呼ぶ
16. min(3)がmin(4)を呼ぶ
17. min(4)は4を返す
18. min(3)は3を返す
19. min(2)は2を返す
20. valid(1)が1 < 2なのでtrueを返す

となり、min(4)やmin(3)が複数回呼ばれてしまっていることが分かる。
ここでは分かりやすくするため偏った木を考えたが偏っていなくても同じことが起きる。
なぜこうなってしまったのか考えると再帰関数が２重に使われておりvalidは下の計算結果を直接利用するが、
minは実行されるたびに過去の結果を覚えてないので毎回葉まで再帰して計算しなおさねばならずに無駄が発生している。

この問題を解決するためには、主に２つの対応が考えられる。

1. functools.cacheなどを使ってメモ化する
2. 再帰関数を一つにまとめ、返り値を(is_valid, min, max)にする

## メモ化

メモ化は「ある引数の組合せに対する計算結果を覚えておいて、同じ引数の組合せが来たときに再度計算せず覚えておいた計算結果を返す」
という仕組みだったと記憶している。
例えば上の例で言うと15ステップ目で「min(2)がmin(3)を呼ぶ」をしたときに、メモ化されていれば既に10-12ステップ目で
min(3)の計算は終わっているのでその計算結果を流用すればよいということである。
これであれば関数の先頭に一行`@functools.cache`をつけるだけでよいので修正は簡単である。
もしfunctools.cacheが無くてもdictなどを使うことによって同様の処理が実装できる。

https://docs.python.org/ja/3/library/functools.html#functools.cache

## 再帰関数を一つにする

再帰関数を２つ使っているのが良くないので、再帰関数を(is_vaild, min_val, max_val)の３つを返す関数にまとめることで
minやmaxが複数回呼ばれることを防ぐこともできる。
こちらの方が自然かもしれない。

## 計測

実際にどれくらい変わるのか簡易的に以下のようなコードで手元で実測してみる。
まず木が偏っていて一直線になっている場合。

```python
NUMBER_OF_NODE = 10**4
root = TreeNode(0)
node = root
for i in range(1, NUMBER_OF_NODE):
    node.right = TreeNode(i)
    node = node.right

solver = Solution()
t0 = time.perf_counter()
ok = solver.isValidBST(root)
t1 = time.perf_counter()

print("isValidBST returned:", ok)
print(f"wall-clock elapsed: {(t1 - t0):.6f} seconds")
```

結果は以下のようになり、やはり最初のコードではO(N^2)なりの計算時間になってしまっていることが分かる。

- cache無し: 12.763859 seconds
- cache有り: 0.011062 seconds
- 再帰関数１つ: 0.004348 seconds

一方でheight-balanced treeになるように構築して試してみたところ、一直線の場合より大きな差ではなかった。

- cache無し: 0.017789 seconds
- cache有り: 0.008266 seconds
- 再帰関数１つ: 0.003387 seconds

min, maxが複数回呼ばれるという事実は間違ってはいないと思うが、その複数回がheight-balancedだと
logN回程度なのでheight-balanced treeの場合はO(NlogN)でO(N^2)の場合ほど悪くはならないという感じだろうか。

## 他の人のPRを見る

https://github.com/akmhmgc/arai60/pull/24/files

DFSでも「rootからnodeに至るまでのpathに現れたノードのlower_bound, upper_boundからvalidかを判定する」という
top-downでも解くことができる。

https://github.com/akmhmgc/arai60/pull/24/files#diff-12915c6bb1596db9039ea2c67b7b8642c14d4576238ddc9641cefeb689126859R50-R51

in-order traversalしてnodeの値を順にリストに詰めていき、それが昇順になっているか確認する方法でもよかったか。
分かりやすいし問題の意図としてはもしかしたらこっちだったのかもしれない。

https://github.com/ryosuketc/leetcode_arai60/pull/28/files#diff-5794d9205a66551c40f76308cad6b9adb19a3fbb42a961d1819cc4850f8a78d4R39-R56

in-order traversalする解法でgeneratorを使うやり方。
yield fromを使うことで再帰的に書くこともできるのか、なかなかよさそう。

https://github.com/ryosuketc/leetcode_arai60/pull/28/files#diff-5794d9205a66551c40f76308cad6b9adb19a3fbb42a961d1819cc4850f8a78d4R13-R15

root = Noneのとき、Falseを返すことにしたという判断が自分と同じだった。

# ステップ３

in-order traversalできるかという問題だと思ってin-order traversalでやる。
３回連続で書けるようになったので一旦完了。

-float('inf')を使わない場合以下のようにも書けるが、ちょっと分かりづらいだろうか。

```python
        values_in_order = get_val_in_order(root)
        val = next(values_in_order)
        for next_val in values_in_order:
            if not val < next_val:
                return False
            val = next_val
```

# ステップ４

GPTと話してたらPython3.10からはitertools.pairwiseを使うことで隣接する要素同士を簡単に取れて
より簡潔に書けることが分かったのでそれも書いた。
https://docs.python.org/ja/3.13/library/itertools.html#itertools.pairwise
