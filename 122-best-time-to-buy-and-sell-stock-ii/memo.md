# ステップ１

前の問題は１回しか買いと売りができなかったが今回は複数回取引できる。

> you can sell and buy the stock multiple times on the same day

この条件がよく意味が分からなかった。同じ日に複数回売り買いしても利益は0ではないのか。

とりあえず最初に買って売り時を逃さないタイミングで売るということをやればいいのではないかと考えた。
今まで見た最小金額min_priceと最大金額max_priceを両方持っておいて、
priceがmin_price未満になったら持っていた株が損になってしまうのでmax_priceのタイミングで
売ったことにすればよい。
そしてもう一度min_price = max_price = priceと再度買い直して同じことを繰り返す。
この方法だとprice < min_priceとなるpriceが来たタイミングでしか更新されないので、
ループが終わった後に最後にmax_price - min_priceを足しこむ必要がある。

あるいは配列の末尾に-1という番兵を置いておくとループ内でも処理が完結するが、
まあそこまでしなくてもいいだろうか。新しい配列を作るor既存の配列に-1を付け加えることをやるので
どちらにしてもそこまでするうまみは無い気もする。

上記の解法で行けると思ったが、これはWAになってしまうやり方だった。
例えば`[1,9,2,10]`のような大きくギザギザした推移を考えると明らかに(9-1)+(10-2)=16の
利益を出せるが上の解法だと10-1=9の利益しか出せていなかった。

以下のように

```
dp[i][0] = i日目に売ったときの最大利益
dp[i][1] = i日目に買ったときの最大利益
```

としてDPで解く方法も考えたが、これは一回のループでO(N)の計算量がかかるので
全体としてO(N^2)になってしまい`N = 3*10^4`のような最大ケースではTLEする。
C++やJavaのような速い言語であればギリギリこれでもいけるかもしれない?

```python
class SolutionWithTLE:
    def maxProfit(self, prices: list[int]) -> int:
        num_days = len(prices)
        dp = [[0] * 2 for _ in range(num_days)]
        for i in range(1, num_days):
            dp[i][0] = max(dp[j][1] + prices[i] - prices[j] for j in range(i))
            dp[i][1] = max(dp[j][0] for j in range(i))

        return max(dp[num_days - 1])
```

上のコードを見ると

```python
dp[i][1] = max(dp[j][0] for j in range(i))
```

こっちは今まで見たdp[i][0]の最大値を別途保存しておけばいいのでO(1)にはできそう。
もう一つのほうも上手く整理してO(1)にできないだろうか。

ループの中でiは関係無いので

```python
dp[i][0] = prices[i] + max(dp[j][1] - prices[j] for j in range(i))
```

と形式的に外に出すことができ、dp[j][1] - prices[j]のほうも今まで見た最大値を持っておけばいい
のでO(1)にすることが可能だということが分かる。
これは意味としてはj日目に買ったのでその支出をマイナスとして計上しておくということか。

dpの値を「利益」だと思ったのが良くなかったかもしれない。「所持金」だと思うと以下のように書ける。
最後にちょっとつじつまを合わせているのがややこしいが、うまく

```python
max(dp[j][1] for j in range(i))
```

の部分を切りだせる形になった。

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        num_days = len(prices)
        dp = [[0] * 2 for _ in range(num_days)]
        dp[0][1] = -prices[0]
        for i in range(1, num_days):
            dp[i][0] = prices[i] + max(dp[j][1] for j in range(i))
            dp[i][1] = -prices[i] + max(dp[j][0] for j in range(i))

        return max(dp[num_days - 1][0], dp[num_days - 1][1] + prices[-1])
```

ここまでするとようやくO(N)の正当な解が見えてくる。

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_bought_previous = -prices[0]
        max_sold_previous = 0
        for price in prices[1:]:
            max_bought_previous, max_sold_previous = (
                max(max_bought_previous, max_sold_previous - price),
                max(max_sold_previous, max_bought_previous + price),
            )
        # 最後の買いは損なだけなので無かったことにする
        result = max(max_bought_previous + prices[-1], max_sold_previous)
        return result
```

ステップ１で紆余曲折して時間はかかったが何とか動くコードは書けた。
最後のつじつま合わせはちょっと見栄えが悪いので適当にmax_profitを持っておいて
都度max_sold_previousで更新していけばよかったかも（最後は必ずどこかの時点での売りになるはずなので）。

# ステップ２

他の人のコードを見る。

https://github.com/akmhmgc/arai60/pull/33/files#diff-c9aa1c5b61c5250a4c53daa1e280a676cb3bb625c859013cecd9dbcd932c000bR4

> ある時点を考えると、一つ前の値段が安い時はその時に買って、ある時点で売れば良いだけであることに気づいた。

確かにそうだ。自分の解法よりずっと簡単でびっくりしてしまった。

https://github.com/Yoshiki-Iwasa/Arai60/pull/53#discussion_r1730194725

上記解法は「一日ごとに前の日から値上がりしていたら前の日に戻って買ったことにして売る」
ということだったが「最小売買回数」を求めるには値上がりが終わったタイミングで売買を行えば
最小売買回数も求められる。
値上がりが続いてる状態をアップトレンドというらしい。株などをやったことがほぼ無く勉強になった。

https://github.com/h1rosaka/arai60/blob/d159bdc08bdbbe4c58ef0c44da58b75ea65c559e/122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.md

上記のステップ１のコメントの付け方が自然な表現で分かりやすいと思った。

https://github.com/hayashi-ay/leetcode/pull/56/files

こちらの方はDP的なアプローチで最終自分が書いた解と同じ形になっていそう。
よく考えると最後は `max_sold_previous` を返すだけでよかった。
また、「買いで終わったか売りで終わったか」よりも「株を持ってるか持ってないか」のほうが
変数名も分かりやすくて良いなと思った。

この前知ったitertools.pairwiseを使えばワンライナーも可能か。
https://docs.python.org/ja/3.13/library/itertools.html#itertools.pairwise

スマートには見えるが可読性が低いので実際これはあまり使わなさそう。

# ステップ３

シンプルな解法でやった。
ここで初めてpricesが空の場合の例外処理をやってないことに気づいた。
prices[0]で初期化する方針でやっているのでそれはやるべきだった。
