# ステップ１

根から最短の葉までのノード数を求める

前回の問題同様、再帰で書くのが一番簡単なので再帰で書いて、
その後は最短経路問題とみなして幅優先探索で書くことにする。

```python
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

再帰でこのように書いてしまったが、これだとサンプルケースのように片側がNoneでもう片方に伸びるノードがあったときに1を
返してしまうので適切でないことに気づいた。
この問題はちゃんと葉かどうかを判定する必要がありそう。

# ステップ２

他の人の解法を見る。

https://github.com/Mike0121/LeetCode/pull/11/files/f860146586f3c4ccd0dbb81fc0302b513862eeda#r1597468459

上から配るDFSだと今見ているノードのdepthが既にmin_depthを超えていたらそれ以上見なくてよいという枝狩りができる。

https://github.com/ryosuketc/leetcode_arai60/pull/22/files#r2119682625

Googleのスタイルガイドでは特定の関数やクラスをimportするために`from foo import bar`のように書かないらしい。
名前空間が分かりづらくなったり名前の衝突を防ぐためかな。

> Use import statements for packages and modules only, not for individual types, classes, or functions.
https://google.github.io/styleguide/pyguide.html#22-imports

# ステップ３

3回連続で通せるようになったので一旦完了。
