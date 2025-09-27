# ステップ１

２つの木を足し算してくっつける

まずボトムアップの再帰で書くのが一番分かりやすいと思ったのでそれを書き、
それをスタックを用いた実装に書き直すことをやってみる。

再帰のほうはさくっと書けたがスタックのほうは難しかった…
Pythonはポインタを持てない（多分）ので他の人のPRを見て学んだlistで疑似的にポインタを持つ方法でやった。
どのポインタを持つ必要があって、スタックに積んだときにどれをどこに渡すかがすらすらと書けなかった。
あと
result_ref.append(merged_node)
と書くべきところを
result_ref = [merged_node]
と書いてしまうと上から引き継いだポインタを別のポインタで上書きしてしまう形になり、
全然left_ref, right_refが埋まらずに無限ループになるというミスをしていた。

トップダウンの再帰とスタックの実装もやってみた。
上からの引継ぎに親とどっち側の子かという情報も必要になりその辺で少しコードがややこしくなっている。
その一方で再帰からスタックに書き直すときはボトムアップのときに必要だった子から親に伝播させるポインタなどが
要らなくなるので翻訳が容易だった。

あとenum型を作っているのにget_left, get_rightという関数が手書きで分かれているのが微妙かもしれない。
get_childという関数にまとめてChildDirectionを引数で渡してその中で分岐させるようにしたほうがスマート？

# ステップ２

他の人のPRを見る。

https://github.com/h1rosaka/arai60/pull/26/files#diff-1ede2b2a752e6743ca4d35b115594d80caecd186a464943ab76618d8d1811252R32-R33

スタック解法のときに地味にrootをどう取るかを悩んで

- bottom-upなら最後にmergeしたノードがroot
- top-downなら最初にmergeしたノードがroot

というやり方でやったのだけど、dummyを作ってその左がrootを指すようにしておけば
dummy.leftでrootが取れるという方法もあるか。

https://github.com/h1rosaka/arai60/pull/26/files#diff-1ede2b2a752e6743ca4d35b115594d80caecd186a464943ab76618d8d1811252R58-R62

copy.deepcopyの挙動について、objectの中にobjectがあったら再帰的にコピーをしてくれるらしい。
それを利用した解法もあった。

簡単なコードを書いて試してみると確かにそのように動いてくれることが分かった。

```python
import copy
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

a, b = ListNode(0), ListNode(0)
a.next = b
c = copy.copy(a)
assert a.next is c.next # bはコピーされず、c.nextはbを参照している

d = copy.deepcopy(a)
assert a.next is not d.next # bもコピーされ、d.nextはbをコピーした別のインスタンスを参照している
```

https://github.com/hayashi-ay/leetcode/pull/12/files#diff-9bdf6ea146707cd300caa32b58d1af7701eda07a7d2e9802408cd8ce1cc70720R30-R41

破壊的に実装するか非破壊的に実装するかについては、今回は一貫して非破壊的実装にした。
破壊的に実装する場合どちらの木にmergeするかが定かでは無く、また問題文にも以下のように書かれていたので
元の木は残して新しい木を構築する方が自然だと考えた。

> You need to merge the two trees into a new binary tree.

https://github.com/garunitule/coding_practice/pull/23/files#r2255583216
https://x.com/nodchip/status/1932263139762229448

`list(filter(None, a))` という書き方があることを知った。
要するにaの中のtruthyな値だけをフィルターしたときにこのような書き方ができるとのこと。
自分だったら`[x for x in a if x]`と書きそうだと思った。

https://github.com/garunitule/coding_practice/pull/23/files#diff-6bccc15d67ba50e16236690521e469bdab288491a8782eb191cbe1e1fe85ce80R113-R127

top-downでも親が子のノードを作ってあげてそれを自分でつないでから子に渡す（子はそのノードに足した値を入れるだけ）と
parent, child_directionなどの引数を持たなくてもよくなる。ただ個人的にはちょっと非自明的な処理な気もする。

https://github.com/quinn-sasha/leetcode/pull/22/files#diff-1ede2b2a752e6743ca4d35b115594d80caecd186a464943ab76618d8d1811252R8-R31

BFSはあまり考えなかったけど、こういう書き方もあるのかと勉強になった。

https://github.com/quinn-sasha/leetcode/pull/22/files#diff-1ede2b2a752e6743ca4d35b115594d80caecd186a464943ab76618d8d1811252R65-R79

こちらはtop-downで親が子のノードを作って足し算までする。

enumってforループで回せるっけと思ったら回せるようなのでそれも使ってみる
https://docs.python.org/ja/3.13/library/enum.html#enum.EnumType.__iter__

stackの良い変数名が思いつかない。「再帰関数として見たときの引数群」みたいな感じなんだけど…。

https://github.com/h1rosaka/arai60/pull/26/files#diff-1ede2b2a752e6743ca4d35b115594d80caecd186a464943ab76618d8d1811252R33

愚直に表すならこちらのコードのように`node_pair_parent_direction`になる？
直後にstack.pop()したときに何が入ってるかが一目で分かるようになってるから、`stack`だけでもいいのかなという気がしなくもない。

# ステップ３

どれを選ぶか、個人的に一番書きやすいのはbottom-upの再帰関数だけど再帰深さが2000くらいになるので
LeetCodeでは大丈夫ではあるが、実務的な観点からは深い再帰は避けたほうがよいかなという気持ち。
仕様が変わってより深い木が来るようになる可能性もある。

stack解法だとbottomupよりtopdownのほうが書きやすいのでそちらを採用してみる。

3回連続で通せるようになったので一旦完了。
