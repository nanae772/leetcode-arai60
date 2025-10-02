# ステップ１

階層ごとに、左から右にノードをリストに格納していく

幅優先探索のような形で書くのが自然かと思うのでそれで書いてみる(step1-bfs.py)

あまり自然じゃない気もするが一応深さ優先探索でも書いてみた(step1-dfs.py)

# ステップ２

他の人のコードを見る

https://github.com/akmhmgc/arai60/pull/22/files#r2359290153

rubyならではの簡潔な書き方。Pythonも頑張れば似たようなことはできそうなので挑戦してみる。

```python
            nodes_by_level.append([node.val for node in nodes])
            next_nodes = [
                node
                for node in itertools.chain(
                    *([node.left, node.right] for node in nodes)
                )
                if node is not None
            ]
```

やってることは同じはずだが全然分かりやすくは無い。
pythonだとflattenがそんなに簡単に出来ないということが分かった。

https://github.com/hayashi-ay/leetcode/pull/32/files#diff-f64e64b98ee3e79b1af4864eb48c186566221d5e613381a9102b5069412dd01eR76

DFSで段を拡張する際はwhileを使ったほうがよいという話。
少し考えるとwhileにしても１回だけになることが分かるが、そのパズルを読者にわざわざ解かせる必要は無いということ。
whileを使うことはちょっとだけ考えて、どの道1回しか実行されないからifのほうが自然かなと思ったけどwhileのほうがよかったか。

https://github.com/Kaichi-Irie/leetcode-python/pull/19/files

自分でフォローアップ質問を考えてBFS, DFSそれぞれのメモリ使用量の違いの深掘りなどをしていてとても勉強になった。
DFSだと縦に掘っていくので平衡二分木のような高さが低い場合に効率的で、
BFSは木に偏りがある場合や全ての木がメモリに乗らず各レベルで取得しなければならない場合などに有効という理解をした。

# ステップ３

3回連続で通せるようになったので一旦完了。
