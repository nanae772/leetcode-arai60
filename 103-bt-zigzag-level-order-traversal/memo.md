# ステップ１

前の問題を少し変形させたような問題。今何段目かを記録しておいて、奇数段なら右から左に見ていくようにすればよさそう。
というより、「反転させるかどうか」というフラグを交互に切り替えていけばいいかな。

```python
        node_vals_by_level = []
        is_reverse = True
        nodes = [root]
        while nodes:
            node_vals_by_level.append([node.val for node in nodes])
            next_nodes = []
            if is_reverse:
                for node in reversed(nodes):
                    if node.right is not None:
                        next_nodes.append(node.right)
                    if node.left is not None:
                        next_nodes.append(node.left)
            else:
                for node in nodes:
                    if node.left is not None:
                        next_nodes.append(node.left)
                    if node.right is not None:
                        next_nodes.append(node.right)

            nodes = next_nodes
            is_reverse ^= True
```

最初このように書いていたが、よく考えると前の段のを引き継いでいるからnodesは常に反転した順序で見なきゃいけなくて、
右から左か、左から右かの際に分岐するようにしなければいけないか。

とりあえず書けたが、「Noneチェックしてからappend」とか「左から右に詰める」とかは関数化したほうがよいかも。

他のやり方としては、毎回左から右に詰めるようにしてnode_vals_by_levelに突っ込むときだけ逆順にするというやり方がある
ということを他の人のコードを見て知ったのでそっちでも書いてみる。
node_vals_by_levelへのappendのときだけひっくりかえせばよいというのはだいぶ分かりやすくてスマートな解法。

ただ結果だけでは無く訪問順自体が重要になるアルゴリズムであるならstep1-1.pyのように書くのが汎用性が高いのかなという気がする。

# ステップ２

リファクタリング案

- is_reverseよりis_left_to_rightなどのほうが適切？
- 「Noneチェックしてからappendする」を関数化する
- 「左から右に詰める」「右から左に詰める」を関数化する(やりすぎ？)

あるいはNoneチェックはせずに全部入れてしまって次のループで非Noneをフィルターするというのでもよいかもしれない。

他の人のPRを読む。

https://github.com/akmhmgc/arai60/pull/23/files

訪問順は左から右に固定して、奇数段のときにdequeを使って先頭に詰めていくという方法でもやれる。

https://github.com/h1rosaka/arai60/pull/30/files#diff-8408720477e1fa6f21dd1fc886a99aa3a937252dddfe9a431516bbb8e258e6fdR28

細かい点だが`is_reverse ^= True`より`is_reverse = not is_reverse`のほうが分かりやすいかも。

https://github.com/Kaichi-Irie/leetcode-python/pull/22/files#diff-ad68d20314949f2174792c5efdbb815b46267933bfdaf06fd60239d559bbbd94R56-R83

dequeを使う解法であり、今のレベルのnodeを結果に追加する処理と次のレベルのノード群を構築する処理を同時にやるという方法もある。

https://github.com/Kaichi-Irie/leetcode-python/pull/22/files#diff-ad68d20314949f2174792c5efdbb815b46267933bfdaf06fd60239d559bbbd94R136-R153

queueに(ノード, レベル)のペアを入れるBFSで、次の階層のノード群を作らずにネストを減らす方法。
自分でも書いてみて結構コードがすっきりしていて、これもなかなか分かりやすいなと思った。

うーん、やっぱりstep1-1.pyのようにforループではreversedで回しているのにその中で左から右か、右から左かを
気にしなきゃいけないのが不自然なように感じる…。
自前でジェネレータを作って何も考えずに左から右、右から左にとれるようにしてみるか。

ジェネレーターだのenumだのを使って書いてみた(step2-next.py)が、流石にこれだけの問題を解くのにここまでするのは
ちょっとどうなんだという気持ちになった…。これならまだstep1-1.pyのままのほうがよかった。
ジェネレーターはともかくDirectionのenumは二値だしわざわざ作らなくてもboolでいい気がした。

# ステップ３

訪問順を重視する方法(step1-1.pyのやり方)でやる。

３回連続で書けなかった、やっぱり毎ターンreverseするところがすんなり入ってこない感じがある。
reversedした上で左→右、右→左を切り替えるところが。

時間を置いて再チャレンジして３回連続で書けるようになったので一旦完了。

細かい部分でいろいろ書き方に差が出て難しい問題だった。
