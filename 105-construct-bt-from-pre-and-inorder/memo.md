# ステップ１

preorderとinorderから二分木を復元する問題

そもそもpreorderかinorderだけから二分木は一意に決まらないのか。
例えばpreorder = [1,2,3]とだけ渡されても

  1
 / \
2   3

なのか

    1
   /
  2
 /
3

か定まらなくて（他にもある）、ここにinorder=[2,1,3]が加わることによって上の木だと一意に定まる？
本当に一意になるのかはちょっと自信が無いけど多分そういうことなのだろう。
10分弱考えても解き方が全然検討がつかなかったので、まず一つ他の人の解法を見ることにする。

https://github.com/akmhmgc/arai60/pull/25/files#diff-aae20e12dc4b3b1c2b927b0ca9556fdcd7158bc00a436ad59b91077b1c0537c5R23-R45

1. 最初にvalに対してそれがinorderでどこにあるかをdictで対応づけておく(各値がuniqueなので必ず決まる)
2. globalにpreorder_indexを管理し、再帰関数はinorderの区間 `[left, right)` を引数とする
  a. left == right なら区間が空なのでスキップする
  b. TreeNode(preorder[preorder_index])をセットして、preorder_index += 1する
  c. preorder[preorder_index]がどこにあるかを上で作った対応付けで探し、それをroot_val_indexなどとする
  d. 左側に`[left, root_val_index)`で再帰、右側に`[root_val_index + 1, right)`で再帰する

という手順だった。なるほど。完全に腹落ちしたかと言われると怪しいが、何となく理解はできる。
とりあえずそれを実装してみる。

top-downだったのでスタックでも書いてみた。

```python
stack.append((node_val_index_inorder + 1, end, node, False))
stack.append((begin, node_val_index_inorder, node, True))
```

ここを逆に書いてしまうと右側が先にされてしまい上手く動かなかった。
普通のDFSだとあまり訪問順を意識しなかったが、これは自分、左、右という訪問順が大事だったのでそこをちゃんとしていないとダメなのか。

# ステップ２

もう少しいろんな人のコードを見る。

https://github.com/akmhmgc/arai60/pull/25/files#diff-aae20e12dc4b3b1c2b927b0ca9556fdcd7158bc00a436ad59b91077b1c0537c5R50-R54

> preorderでのrootの隣がleft_nodesの再帰でのrootになるし、
> preorderでrootにinorderのleft_nodesの数を足したものがright_nodesでのrootになるので、その値をそのまま使えば良いと思った。

preorder_indexをグローバルで管理せずに直接求めて再帰関数の引数にする工夫。
確かにこっちのほうがいいかもしれない。このやり方だとstack解法でも積む順番を気にしなくてよくなる。

https://github.com/garunitule/coding_practice/pull/29/files#diff-4812460128cd912d69b469b7b776700478c1709f119b53e754cf62dab5fe47e6R44

val_to_inorder_indexは内包表記を使えば一行で書ける。

https://github.com/garunitule/coding_practice/pull/29/files#diff-4812460128cd912d69b469b7b776700478c1709f119b53e754cf62dab5fe47e6R76-R86

O(n^2)になるが辞書を使わずにindexでroot_valの位置を求め、かつスライスを使うことで元の関数を再帰にするだけで解くこともできる。

https://github.com/h1rosaka/arai60/pull/32/files#diff-e9b6f8cf3e6bf93b2177690b6fb60c6eaa153a33e3acaf7bad26c23ebd604dcaR63-R70

preorder_indexをグローバルで管理しない方法その２。
自分で求めるのではなく、子の返り値にそれを含めてもらってそれを利用するという方法。
自分で計算しなくていい分こちらのほうが分かりやすいか？
とはいえ

```python
preorder_index += 1
root.left, preorder_index = build_tree(begin, inorder_index, preorder_index)
root.right, preorder_index = build_tree(inorder_index + 1, end, preorder_index)
return root, preorder_index
```

を見て結局preorder_indexの値どうなってるのかやや想像がつきにくい感じもある。
一長一短かもしれない。

https://github.com/h1rosaka/arai60/pull/32/files#r2296919898

valueが同じノードがあったら、という懸念。そもそも同じ値がある場合は一意な復元が出来なさそう。

preorder = [1,1,2], inorder = [1,1,2]は
preorder[0] = 1がinorder[0]に対応しているのか、inorder[1]に対応しているのか分からないので

  1
 / \
1   2

1
 \
  1
   \
    2

上記のどちらでも成立するが、その場合はどちらか成立するほうを出力できるようにしておくのかな。
何らかの方法でpreorderとinorderの数が一対一に対応するような下準備をする必要があり、ちょっと面倒そうだなと思った。
出現した回数でラベルを貼っていくようなイメージで重複に対応するコードも書いてみた(step2-dup.py)。

# ステップ３

３回連続で書けるようになったので一旦完了。
