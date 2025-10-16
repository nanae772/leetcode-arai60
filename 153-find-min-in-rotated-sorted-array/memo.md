# ステップ１

何回かrotatedされたソート配列からO(logn)で最小値を見つける

front = nums[0] とするとrotatedされた配列は
`[front以上の要素],[front未満の要素]`
と２つに分割できるはずである。
「front以上であるかどうか」をtrue/falseで表すと
`true, true, ..., true, false, false, ..., false`
とどこかで境界がある形になっているのでこのような問題では二分探索が効果的に使える。

そして求めたい最小値に関しては`[front未満の要素]`はソートされているのでこの先頭を取ればよい。
つまり、上のtrue/falseでいうと「falseになる一番左」が求めたいものである。

ただし一点注意したいのがfalseが全くない(=front未満の要素が全くない)場合である。
これに関しては一周されてまたソートした状態に戻ってきているという状態になっているので
このときに関してはfrontを返せばよい。

前回、閉区間に対応する書き方の実装をやっていなかったので今回はそれでやることにする。
つまり不変条件を

left = これより下はfront以上
right = これより上はfront未満

としてleft,rightがクロスするまでやる（終了条件はright + 1 == left）。
これは`(-∞, left)`, `(right, +∞)`に分けるイメージでこれをひっくりかえすと
未探索区間が`[left, right]`と閉区間に対応する。

書けた。`right + 1`の部分は上記の終了条件より`left`と書いてもよかったが、
`right = これより上はfront未満`としているので`right + 1`のほうが意図がより伝わりやすいか
と思いそのように書いてみた。

# ステップ２

他の人のコードを読む。

https://github.com/h1rosaka/arai60/pull/44/files#diff-856251eccb601f9962fc7fdd308675f5690975413b45fe6be0950672570bc6caR9

分け方をlast=nums[-1]として`[lastより大きい要素], [last以下の要素]`にすれば
`[last以下の要素]`が空になることはなく、そうすると最後の場合分け無しで自然にrightを返せるのか。確かに。
未探索区間を`(L, R]`の半開区間にしているのはあまり見たことが無いパターンでちょっと読むのに時間がかかりそう。

https://github.com/h1rosaka/arai60/pull/44/files#diff-856251eccb601f9962fc7fdd308675f5690975413b45fe6be0950672570bc6caR103

bisect_leftを使うと上記のようにも書けるのか。
`key=lambda x: x <= nums[-1]`を渡すことで元の配列を`[False,..., False, True, ...]`
のような配列とみなしてその中でTrueが挿入される最も左端を見ればよいということを意味している。
https://docs.python.org/ja/3/library/bisect.html#bisect.bisect_left

他にもいろいろな書き方がされていて勉強になった。

https://github.com/h1rosaka/arai60/pull/44/files#diff-856251eccb601f9962fc7fdd308675f5690975413b45fe6be0950672570bc6caR130-R134

```python
nums[bisect_right(nums, False, key=lambda x: x < nums[0]) - len(nums)]
```

の最後の`- len(nums)`に関する解説。なるほど…分からなかった。
私の最後の場合分けに対しても適用はできそうだけど、分かりづらいので実際にはやらないかと思った。

https://github.com/seal-azarashi/leetcode/blob/0c50204ca7f9fa0116c33c52f635d28343c7aa79/arai60/Binary_Search/find-minimum-in-rotated-sorted-array.md

こちらの解法が「先頭と比較」「最後と比較」のどちらでもないやり方の二分探索で解かれていた。

```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] <= nums[right]) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return nums[left];
    }
}
```

midをチェックするときにleft, rightの状態も使う二分探索を見るのは初めてだった。
確かにこのような書き方もできるのか。
しかしよくよく考えてみるとnums[right]はnums[nums.length - 1]でもよく、そうすると最終的には
「最後と比較する」と同じことをやっていることになっているというのが、以下の議論でも述べられていた。
https://github.com/seal-azarashi/leetcode/pull/39/files/0c50204ca7f9fa0116c33c52f635d28343c7aa79#r1851140547

# ステップ３

未探索区間を閉区間とみなすパターンで３回。

left, rightという変数名もよく考えるとちょっとどうなんだという気持ちがある。
`(-∞, left)`, `(right, +∞)`とみなすとむしろleftが右端なのでrightだし、
rightが左端なのでleftだしという気持ちもある。
ただ二分探索にleft, rightとかlo, hiなどはよく使われるので慣れておいた方がよいのかな。
