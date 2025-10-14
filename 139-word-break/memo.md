# ステップ１

単語の集合wordDictの単語を組合わせてsが作れるかどうかを判定する。
wordDict内の単語は何回でも使ってよい。
単語やsに含まれる文字は英小文字のみ。

wordDict内の単語が何回でも使えるので、各wordに対して
sのprefixがwordと一致するかを判定し一致するならprefixを削ってs'とし、
再度s'が各wordDictのwordのprefixと一致するかを判定し…
と最終的にs'が空になるまで再帰しつづければできそうだと思った。

sの長さをL, wordDictの要素数をN, wordDict[i]の最大長さをMとすると

状態としては`s[i:](0 <= i <= len(s))`、つまりO(L)。
各状態において遷移の数は`len(wordDict)`, O(N)で
各遷移においてprefixの一致判定にO(M)かかる。
よって、全体としての計算量はO(LNM)となる。

L = 300, N = 1000, M = 20の最大ケースを考えると6*10^6のオーダーとなる。
Pythonが1秒に10^7回の演算を行えると仮定し定数倍も加味すると、
だいたい1~2秒で終わるんじゃないかという見積り。

とりあえず最初に思いついたのが再帰だったのでメモ化再帰で書くことにする。
len(s) <= 300なので再帰深さは大丈夫そう。

どちらも書けた。

ちなみに「wordDictのwordが各々一回ずつ使えないとしたら」という発展形を考えると、
愚直に全ての並び方を試す方法で最低でもΩ(N!)、
上のDPに「wordDict[i]を既に使ったかどうか」という状態も保持させてそれでもΩ(N*2^N)となり、
一気に指数関数時間かかるようになってしまいそう。

N!とN*2^Nはどちらが速く漸近的に増加するかは`N!/N*2^N = (N-1)! / 2^N`を考えると、
N!のほうが圧倒的に速いということが分かる（ということをGPTに聞いた）。

# ステップ２

他の人のコードを見る。

https://github.com/akmhmgc/arai60/pull/34/files#diff-491ec1e4655be774b4eb4ad08f7b3f1944f4c507499bc1eb53ecf67628fec63eR14-R26

prefixではなくsuffixの一致を見ていくDPもある。
この場合DPのループは前からできるが個人的にはprefixを見る方が好み。

https://github.com/akmhmgc/arai60/pull/34/files#diff-491ec1e4655be774b4eb4ad08f7b3f1944f4c507499bc1eb53ecf67628fec63eR32

ローリングハッシュでも解けるらしい。昔ちょっと聞いたことがあるが実際どういうものかはあんまり知らなかった。
コードを読んだがなぜこれでうまくいくのかいまいちつかみきれなかった。
あとbase=29の29はどこから来たのだろうか？26ならアルファベットの文字数だと理解できるのだけど。
⇒調べたらbaseはmodと互いに素であるという条件が必要らしい。
ということはmod=10^9+7のような素数ならbaseは素数でなくてもよさそう？

そもそもローリングハッシュの基数baseは`2<=base<mod`だったら文字数以下でもなんでもいいんだろうか。
ローリングハッシュについて調べていろいろ見ているとそのように書いているような気がする。

https://github.com/h1rosaka/arai60/pull/41/files#diff-25f1226927fe56c505f4cbf2124534215d66f3c2ca0decf160a04dc095c93e83R69-R70

再帰のときにcan_generateでTrueが返ってきたら即時Trueをリターンすればよかった。
そのほうが分かりやすいしやや効率的でもある。

https://github.com/h1rosaka/arai60/pull/41/files#diff-25f1226927fe56c505f4cbf2124534215d66f3c2ca0decf160a04dc095c93e83R148-R152

ローリングハッシュの解説について、こちらのメモを見て理解できた。
wordListのほうも途中までのhashを都度hashlistに入れているからうまくいくのか。

https://github.com/SuperHotDogCat/coding-interview/pull/23#discussion_r1619249148

ローリングハッシュは

wordListのハッシュの構築: O(NM)
sのハッシュ探索: O(L^2)

で全体としてO(NM + L^2)でL <= NMであれば計算量としてはローリングハッシュのほうが優秀そうだが

- 入力文字が英小文字であることを期待している
- 確率は低いとはいえハッシュの衝突が起こりえる

などの問題があり、実際に使うのはやめておいた方がよさそう。
Aho–Corasickというアルゴリズムもあり（聞いたことはある）、そちらだと確実だが実装が大変らしい。

ローリングハッシュを実装しようとして

```python
        def get_index_letter(ch: str) -> int:
            return ord(ch) - ord("a")

        def calculate_next_hash(hash_: int, ch: str) -> int:
            return (hash_ * BASE + get_index_letter(ch)) % MOD
```

と書いていたがこれだとa,aa,aaa,...のハッシュ値が全て0になってしまうのでこれだとダメだった。

# ステップ３

シンプルなステップ１のDPの解でやった。
