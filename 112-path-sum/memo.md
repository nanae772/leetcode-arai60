# ステップ１

根から葉まで行くパスの和がtargetSumになるものがあるかを判定する

まずは再帰で解いてみる。
再帰関数の引数にtargetを持たせて、target - node.valを左右で再帰させるときのtargetにして
左右どちらかからtrueが返ってきたらtrueであるという方針。

今回はNoneが渡されたときの例外処理はちゃんとしておく。
再帰関数の終了条件としてのNoneの返り値と、root=Noneの場合の返り値が異なるため。
…と思ったが考え方が間違っていた。

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def has_path_sum(node: TreeNode | None, target: int) -> bool:
            if node is None:
                return target == 0

            new_target = target - node.val
            return has_path_sum(node.left, new_target) or has_path_sum(
                node.right, new_target
            )

        return has_path_sum(root, targetSum)
```

これだと片方だけ部分木がある途中のノードでもそこへのpath sumを判定してしまうため正しくなかった。
例えば[1, 2], targetSum = 1 がTrueになってしまっていた。
このミスは前もやってしまったような気がする…。

何回かWAしてようやくACした。Noneの扱いがやや面倒…もう少しうまくできなかったか。

top-down式にも書けるのでそれを書いて、それをstack版に翻訳したものも書いた。
しかし何だか要領を得ない感じがする…path_sumに加算するタイミングが違和感。
めんどくさがらずに分岐するタイミングでNoneチェックをしたほうがこの場合は分かりやすくなるかもしれない。

# ステップ２

他の人のコードを見る

https://github.com/garunitule/coding_practice/pull/25/files#r2265474303

is_leafはTreeNodeのメソッドにしたい（LeetCodeの仕様として出来ない（無理やりsetattrなどすればできる？））、
ないしはSolutionから独立した関数としたほうがよいのではないかという意見があった。
確かにそうかもしれない。

https://github.com/garunitule/coding_practice/pull/25/files#r2265099783
https://github.com/quinn-sasha/leetcode/pull/24#discussion_r2172911737

「ここまでの」という意味で`so_far`をつけるという表現があるがあまり使わないとのこと。
自分はそもそもこの語彙が無かったが新しい視点で参考になった。

# ステップ３

３回連続で通せるようになったので一旦完了。
