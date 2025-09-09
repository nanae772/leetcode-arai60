# ステップ１

数値の配列から頻度の高い上位k個の値を出力せよという問題。

最もシンプルな解法は

1. dictで各数値の出現回数をカウント
2. (数値, 頻度)の配列に変換し、頻度の降順でソート
3. 上位k個を取得

1はdictを使わずに、numsをソートして前から順に(ユニークな値、頻度)という風にまとめる方法もある。
がdictを使ったほうがシンプルそう、あとpythonだとCounterっていうクラスがあったような。
それにnumsを突っ込めば{数値: 頻度}の辞書が自動的にできる、みたいな。
https://docs.python.org/ja/3.13/library/collections.html#collections.Counter

ドキュメントを読むとmost_commonというメソッドもあり、これを使えば一発だ…
https://docs.python.org/ja/3.13/library/collections.html#collections.Counter.most_common

このやり方で計算量的には

1. 平均O(n)
2. k個のソートなのでO(klogk)
3. O(k)

なのでO(n + klogk)で以下の条件は満たせている…？

> Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

あるいはO(n)とかO(nloglogn)とかでやることが求められているのだろうか？
ちょっと分からない。

とりあえず最初に思いついたシンプルな解法で実装してみる。
実質２行で済んでしまった。

（メタ読みだけど）ヒープの問題に分類されているからヒープを使った解法もあるんだろうけど、ちょっと思いつかない…
次のステップに行く。

# ステップ２

まずEditorialを見てみる。

> the particular case k=N could be considered separately and solved in O(1) time.

流石にO(1)にはならなくない…？と思ったけど、与えられたリストをそのまま返すだけだからO(1)なのか。

Approach1はCounterを使って(数値、頻度)にするところまで全く一緒で、それをヒープに入れるという解法だったが、
正直なところヒープを使う理由がよく分からない。動的に変わっていかないのならソートでいいのではないだろうか。

Approach2もやっぱり最初に(数値,頻度)にするのは必要。後はほぼクイックソートだけど降順にやるとして、
左と右に分けた後にpivot_indexがk-1より小さいなら左側は無視できる、k-1より大きいなら右側は無視できる、なので
全体をソート自体をする必要は無いのでクイックソートより速くできるということか。
それでも最悪計算量はO(N^2)(これはクイックソートと同じ)だけど、ピボットをランダムに取ればその確率はほぼ無視できるらしい。
理論的にどれくらいの確率になるのかはよく分かっていない。
平均的には見ていく区間が半分、半分、半分…となっていくのでだいたいN + N/2 + N/4 + ... = 2N = O(N)という感じか。

左と右に分けるときのアルゴリズムでLomuto's Partition Schemeというのが紹介されていたけどピンとこない。
一回自分でやるとどうなるか書いてみる。

最後に紹介されいる[Median of Medians](https://en.wikipedia.org/wiki/Median_of_medians)は計算量だけ見ると
O(N)だが定数倍が重くかつ重複があると動かないので実践的ではないと書かれていた。

GPTに軽く説明してもらったところ、クイックセレクトと考え方は一緒で「良いピボットを求める」ことで計算量を減らす工夫をしている。

1. 配列を小さいグループに分けて(5つずつなど)、各グループの中央値を求める
2. それらの中央値の中央値をピボットにする

とするとピボットが常に「全体の30%以上、70%以下の位置」に来るらしい。
それを元に再帰式を作って計算量を求めるとO(N)になるらしい。

とりあえずMedian of Mediansは知識として持っておくぐらいにしておこう。

ちょっと実装しながら考えてたけどランダムピボットのクイックセレクトでも全部同じ値だとO(N^2)になるのではという気がした。
左と右に分けるときにピボットと同じ値だったらどっちに振るかを決定的にやっていると１個ずつしか区間が狭まっていかないのではないか。
なのでピボットと同じ値が来た時に1/2で左、1/2で右に振るというランダム性をここでも入れたほうがいいのか？

調べてみた。自分で実装してみた方法(とLomuto's Partition)はやはり全ての値が等しい場合に
区間が１つずつしか狭まっていかないのでO(N^2)になってしまう問題がある。
この問題についてGPTに問うと以下の解決法を示された。

1. (pivotより大きい区間),(pivotと等しい区間),(pivotより小さい区間)で三分割する方法
  - オランダの国旗に見たてて[Dutch national flag](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)という名前がついている
2. [Hoare's Partition](https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme)を使う

Hoare's Partitionのほうの理解に時間がかかったが、「pivot以上」「pivot以下」と分けることができて
全ての値が同じでも真ん中あたりで分かれるので効率的に区間を狭めていけるようだ。

データクラスの名前をValueAndFrequencyにしていたがやや長く冗長に感じたのでValueCountにしてみる

なんかHoare's PartitionのアルゴリズムのときにWAが出てとても沼ってしまった

```python
return select_top_k_frequent(left, rightmost_at_least_pivot - 1)
```

これがダメで

```python
return select_top_k_frequent(left, rightmost_at_least_pivot)
```

にしなければいけなかった。

Lomuto's Partiton(my partitionも)の場合はいずれも最終的にrightmost_at_least_pivotにピボットが来るから、
そこを削っても左側が「pivot以上」が保たれているので大丈夫だったが、
Hoare's Partitionの場合は、rightmost_at_least_pivotにピボットが来るわけではないので、
rightmost_at_least_pivotを削った区間で探索するとおかしなことになっていた。

例えばa = [4, 1, 2, 5, 3]という数列をHoare's Partitonで2番目に大きい数を求めることを考えてみる。

最初のピボットを3にしてこれを左側は3以上、右側は3以下になるようにPartitioningすることを考える

4, 1, 2, 5, 3 -> i = 1, j = 4 をスワップ
   ^        ^
   i        j

4, 3, 2, 5, 1 -> i = 2, j = 3 をスワップ
      ^  ^
      i  j

4, 3, 5, / 2, 1 -> i = 3, j = 2 となり停止
      ^    ^
      j    i

となり、次に(left = 0, right = j - 1 = 1)で再帰してしまうと含めるべきだった5が考慮されなくなり正しい値を求められない。

正直かなり混乱してしまい今もまだ上手く飲み込めていないので全然違うことを言っているかもしれない。
Dutch national flagもやろうと思っていたが疲れてしまったので一旦このあたりで切り上げてステップ３に行く。

(追記)
無限再帰になってしまうケースがあることが発覚しました。
自戒のために残しておき、後日考えることにします。

# ステップ３

３回連続で通せるようになったので一旦完了。
most_commonは封印して解いたほうがよかったかもしれない…

# ステップ４

昨日はクイックセレクトを考えるときに、まだちゃんと理解できてない状態で
この問題に合わせて昇順ではなく降順でやろうとしてたのも混乱のもとだったかもしれない。
今回は一般的な昇順ソートで改めて理解しなおす。

まずLomuto's Partitionのアルゴリズムを要点だけ抽出して書くと以下になる。

```python
def lomutos_partition(a: list, left: int, right: int, index_pivot: int) -> int:
    # 区間[left, right]を分割して左側をpivotの値以下、右側をpivotの値より大きくする
    pivot = a[index_pivot]
    # まずpivotをrightの位置と入れ替える
    a[index_pivot], a[right] = a[right], a[index_pivot]
    leftmost_greater_than_pivot = left
    for i in range(left, right):
        if a[i] <= pivot:
            a[i], a[leftmost_greater_than_pivot] = a[leftmost_greater_than_pivot], a[i]
            leftmost_greater_than_pivot += 1
    a[leftmost_greater_than_pivot], a[right] = a[right], a[leftmost_greater_than_pivot]
    rightmost_at_most_pivot = leftmost_greater_than_pivot
    return rightmost_at_most_pivot
```

このとき返り値の範囲は left <= rightmost_at_most_pivot <= right になる。
そしてこのアルゴリズムが終わった後、
a[left:rightmost_at_most_pivot]の全ての要素はpivot以下
a[rightmost_at_most_pivot]はpivot自身、
a[rightmost_at_most_pivot:right + 1]の全ての要素はpivotより大きくなる。
ざっくり書くと
a[left:rightmost_at_most_pivot] <= a[rightmost_at_most_pivot] <= a[rightmost_at_most_pivot:right + 1]
となるように分けられる。

なのでLomuto's Partitionの場合は以下のように
[left, rightmost_at_most_pivot - 1],
[rightmost_at_most_pivot + 1, right]
いずれの区間に再帰させても区間が１つは狭まっていくので無限再帰になることは無いし、
また上記の不等式からrightmost_at_most_pivotを削っても最終的に正しい答えを求められていた。

一方でHoare's Partitionの場合

```python
def hoares_partition(a: list, left: int, right: int, index_pivot: int) -> int:
    # 区間[left, right]を分割して左側をpivotの値以下、右側をpivotの値以上にする
    pivot = a[index_pivot]
    leftmost_at_least_pivot = left - 1
    rightmost_at_most_pivot = right + 1

    while True:
        leftmost_at_least_pivot += 1
        while a[leftmost_at_least_pivot] < pivot:
            leftmost_at_least_pivot += 1

        rightmost_at_most_pivot -= 1
        while a[rightmost_at_most_pivot] > pivot:
            rightmost_at_most_pivot -= 1

        if leftmost_at_least_pivot >= rightmost_at_most_pivot:
            return rightmost_at_most_pivot

        a[leftmost_at_least_pivot], a[rightmost_at_most_pivot] = (
            a[rightmost_at_most_pivot], a[leftmost_at_least_pivot]
        )
```

こちらも返り値の範囲は left <= rightmost_at_most_pivot <= right になる。
そしてこのアルゴリズムでは最終的にrightmost_at_most_pivotの位置にpivotが来る保証がないため、
a[left:rightmost_at_most_pivot + 1] <= a[rightmost_at_most_pivot + 1:right + 1]
であることしか満たされない。その状態で左側に再帰して
[left, rightmost_at_most_pivot - 1]
としてしまうとa[rightmost_at_most_pivot]がa[left:rightmost_at_most_pivot]内のある要素より小さい場合があったときに、
正しく答えを求められないという状態が起きる。

昨日の私はこれを避けようとして、左側に再帰するときに
[left, rightmost_at_most_pivot]
としたが、これはこれでrightmost_at_most_pivot = rightとなるケースがあり、この場合は区間を狭められていないので
そういったケースで無限再帰になってしまう。
これに関してはLomutoの場合も同様で、むしろLomutoの場合は全てが同じ値のときにランダムにpivotを取っても必ず
rightmost_at_most_pivot = rightになるので分かりやすく昨日発覚したのもそれだった。


## どうすればよかったのか

Lomuto, Hoareでそれぞれ厳密には違う分け方をしているので別々に実装すべきだったかもしれない。

まずLomutoについては上述のようにrightmost_at_most_pivotを取り除いて
[left, rightmost_at_most_pivot - 1],
[rightmost_at_most_pivot + 1, right]
のどちらかに再帰させる方法で確実に狭まっていくので問題はない(全て同じ値のときにO(N^2)になる問題は依然としてあるが)

Hoareの場合。
rightmost_at_most_pivot = rightがどのようなケースかを考えてみると

最初のループで

1. rightmost_at_most_pivotがrightで止まる
2. leftmost_at_least_pivotがrightで止まる
3. leftmost_at_least_pivot >= rightmost_at_most_pivotなので、rightが返る

というケースしかないはず（次のループに行くとrightmost_at_most_pivot < rightになるため）

そしてこの状況がどういうことかというと

1. 1.よりa[right] <= pivot
2. 2.よりa[left:right-1]は全てpivotより小さく、a[right] >= pivot
3. よってa[left:right-1] < a[right] = pivot

ということになる。つまりpivotを選ぶときに右端から選び、そのほかが全てpivotより小さいときに区間が狭まらない。

この対策としては

1. Hoare's partitionでは右端をpivotに選ばないようにする
2. rightmost_at_most_pivot = rightとなった場合は、rightmost_at_most_pivotがピボットになっているため、
      左側に再帰するときにそこを削って[left, rightmost_at_most_pivot - 1]にする例外処理を行う

の２つが考えられる、シンプルなのは1だろうか。

改めて整理し直して、

1. Lomuto's partition(step4-lomuto.py)
2. Hoare's partition(step4-hoare.py)
3. Dutch natinal flag partition(step4-dnf.py)

の３パターンによる分割を実装した。
Dutch natinaol flagも出てくる変数は多いもののそこまで複雑なアルゴリズムではなかったため理解できた。
