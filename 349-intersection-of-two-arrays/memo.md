# ステップ１

整数配列nums1, nums2の共通部分、すなわちどちらにも入っている整数を求めるタスク

とりあえず思いつく解法は２つ

1. setを使う
2. sortしてuniqしてマージする

## setを使う方法

Pythonだとsetを使えばワンライナーで解けてしまう

```python
set(nums1).intersection(nums2)
```

ここは

```python
set(nums1) & set(nums2)
```

とも書ける。intersectionのほうはnums2をsetに変換しなくてもよい。
公式ドキュメントでは&はエラーを引き起こしやすいということでintersectionを推奨している。

> Note, the non-operator versions of union(), intersection(), difference(), symmetric_difference(), issubset(), and issuperset() methods will accept any iterable as an argument. 
> In contrast, their operator based counterparts require their arguments to be sets. 
> This precludes error-prone constructions like set('abc') & 'cbs' in favor of the more readable set('abc').intersection('cbs').

https://docs.python.org/3/library/stdtypes.html#frozenset.intersection

なお、間違えて

```python
set(nums1) and set(nums2)
```

と書いてしまうと

- `set(nums1)`が空なら短絡評価で空集合が返る
- そうでないなら`set(nums2)`の値が返ってくる。

となってしまうというミスを１回やらかした。

## ソートしてuniqする方法

手間はかかるがsetを使わない方法もある。
sortしてuniq（重複を除く処理）した配列を作り、それらを前から見ていって両方に入っていれば
それを返り値のリストに加えるというようなアルゴリズム。マージソートのマージに近いことをやる。

こちらもひとまず書けた。連結リストから重複を除く問題を先にやっていたおかげで
uniqする処理の実装にあまり悩まずにできたのは良かった。
もう少しうまいやり方はあるかもしれない…

調べてみたところ、itertools.groupbyがそれに近いことをやってくれるようだ。
https://docs.python.org/ja/3.13/library/itertools.html#itertools.groupby

ステップ２ではそれを使ってリファクタリングしてみることにする。

# ステップ２

## setを使う方法

setを使っているのでこちらの手法では返り値の順序が保証されていない…と思ったんだけど
試しに手元でsetをリストに変換すると昇順に並んでいる気がする…？
→気のせいでした。

```
>>> list({5,1,3,9,8,11,3234,0,-11})
[0, 1, 3234, 3, 5, 8, 9, 11, -11]
```

これもライブラリを使う側からすると昇順に並んでいてほしいなと思う気がするので、sortedしたものを返してもよいかなと思った。
時間計算量はO(N)からO(NlogN)になるが組み込みのソートを使うだけなのでそれがボトルネックになるようなことは無いと思う。
numsをsetに変換してintersectionする処理のほうが時間かかりそう、という感覚。

たまには実測もしてみようということで実際にintersectionする操作とsortする操作、どちらの方が時間がかかるかを計測した。
測定に使ったコードはsokutei-gpt.py(GPTに作ってもらった)

この問題における最大サイズを入力として計測してみた結果は以下のようになった。

Dataset: N=1,000, MAX_VALUE=1,000, NUMBER_OF_ITERATION=1,000

intersection(set(a), b)       total:  45.97 ms   per-op:  45.97 µs   n=1,000
sorted(c)                     total:   3.71 ms   per-op:   3.71 µs   n=1,000

Sizes -> |a|=1,000, |b|=1,000, |c|=388

intersectionを取った後は要素数が減るからというのはあるかもしれないが、
sortにかかる時間はintersectionを求める時間の約1/10で済むので大した問題では無いことが分かる。

N = 10^5, MAX_VALUE = 10^5 と問題の制約から上げてみても約10倍の差だった。

Dataset: N=100,000, MAX_VALUE=100,000, NUMBER_OF_ITERATION=1,000

intersection(set(a), b)       total:   9.386 s   per-op:   9.39 ms   n=1,000
sorted(c)                     total: 777.27 ms   per-op: 777.27 µs   n=1,000

Sizes -> |a|=100,000, |b|=100,000, |c|=40,021

## ソートしてuniqする方法

itertools.groupbyを使ってみた。

groupbyで何が返ってくるかあんまりちゃんと分かってなかったが「(key, groupイテレータ)のイテレータ」が返ってきているようだ。
今回のように代表値だけ欲しい場合はkeyだけを取ってgroupイテレータを捨てるとuniqができる。

## 他の人のコードを見る

https://github.com/akmhmgc/arai60/pull/10/files

rubyだとa.sort.uniqが出来るらしい

> Setへの変換はハッシュ値の計算、そしてハッシュ値の衝突時のバケットの探索、負荷率上昇に伴うrehashなど

上でsetへの変換のほうが重そうだなと書いたけど裏ではこういう理由があるから、というのを考えられているとより良かった。

https://github.com/skypenguins/coding-practice/pull/21/files

そういえばO(N^2)の全探索が頭に無かった。書くかどうかはともかく選択肢として挙げておきたかった。

https://github.com/tarinaihitori/leetcode/pull/13/files#r1826602904

setに変換する方法で、小さい方だけを持てば空間計算量をO(min(n, m))に出来るのは確かにと思った。

# ステップ３

setのほうは一行なのであまり練習にならないと思い、ソートする方でやった。
3回連続で通せるようになったので一旦完了。
