# ステップ１

足してkになる連続する部分配列がいくつあるかを数える。

これは似たような問題(k=0の場合)を解いたことがあるので解法自体はすぐ分かった。

まずシンプルな解法としては全ての区間について総和を取っていき、kに一致するかを判定する方法がある。
区間の数は長さNの場合、N(N-1)/2+N = N(N+1)/2個あり、その区間ごとにループを回して和を取っていく方法ではO(N^3)、
累積和で計算量を短縮してもO(N^2)となりN=2*10^4となる最大ケースではPythonではこの計算量では少し厳しそうである。

問題の制約により、配列内に負の整数も入っていることに注意する。
非負整数のみであれば単調性が担保されていて尺取り法などで解けるはずだが、負の整数が入っている場合はそれは使えない。

nums[0]からnums[i-1]の累積和をs[i]とすると、区間[l, r)の総和はs[r] - s[l]と表せる。
なのでこの問題はrを固定したときにs[l] = s[r] - kを満たすlがいくつ存在するかが分かれば解ける、ということになる。
これは辞書を使って(累積和 -> それが出た回数)を保存しておけば平均的にO(1)で求められ、全体でO(N)で解ける。

とりあえず書けた。最初`complement = prefix_sum - k`と書くべきところを
`complement = k - prefix_sum`と逆に書いてしまっていて１WAした。

# ステップ２

とりあえず空で書ける範囲で書いてみたが、defaultdictを使ったほうがシンプルになりそうなのでまずそこを変える。

defaultdictのドキュメントを読んでいるとdictにsetdefaultというメソッドがあることを知った。
> This technique is simpler and faster than an equivalent technique using dict.setdefault():
https://docs.python.org/3/library/stdtypes.html#dict.setdefault

defaultdictは何となくで使っていたが、keyが無いときに__missing__が呼ばれてその中で
default_factoryが設定されていたらそれを使って初期値(intなら0, listなら[])などがセットされるようになっている
というものだと理解した。
なのでint,listのような定番のもの以外でも自分でlambdaなどでdefault_factoryを定義すれば独自の初期値からスタートさせることも可能。

```
>>> from collections import defaultdict
>>> a = defaultdict(lambda : 2)
>>> a[0]
2
```

count_subarray_sum_equals_kという変数名は長すぎるだろうか。step1ではcount_subarray_sum_kとequalsを入れてなかったが、
それでも十分分かるかな？

他の方のPRを見る。

https://github.com/Shoichifunyu/shofun/pull/11/files#r2365544792

この自明な解法からスタートして変形していき、計算量を落とす方法を考えるところは勉強になった。

# ステップ３

３回連続で通せるようになったので一旦完了。
