# ステップ１

連結した島の最大数を数える問題

前回やった[Number of Islands](https://leetcode.com/problems/number-of-islands/)同様、

1. 再帰を使う/使わない深さ優先探索(DFS)
2. 幅優先探索(BFS)
3. UnionFind

などの解き方がある。

前回は再帰を使わないDFSをやったので今回は再帰を使ったDFSで解いてみることにする。
盤面のサイズが最大2500なので、デフォルトのrecursionlimitだと1000なので再帰上限エラーになるが
LeetCode上では550000に引き上げられているので再帰でも解けるはず。
実務上では1000を超える再帰はなるべくループで書き直したほうがよいと思う。
何気に今回の問題ではinputが整数の0/1になっていることに注意（前回は文字列だった）。

# ステップ２

他の方のコードを見る。

https://github.com/akmhmgc/arai60/pull/15/files

名前についてnumber_islandsよりarea_islandsなどのほうが良いかも。
外側とのmax_areaとの一貫性も取れる。

https://github.com/akmhmgc/arai60/pull/15/files#r2347265871

分岐するタイミングでチェックするのではなく、投げた先で水上or既に見た奴なら0を返すとする方法もあるか。
そちらのほうが再帰関数の停止条件が分かりやすくよいかもしれない。

https://github.com/Kazuryu0907/LeetCode_Arai60/pull/12/files

私は各(row, col)についてis_visitedフラグを持つ方針でやっていたが、setでvisitedな点を管理する方法もあるか。
setを使うのでhash化・rehash・collision解決などの処理が加わり重くなりそうだが、
盤面サイズに対してislandsが少ない場合などはsetを使ったほうがメモリや計算時間を抑えられるパターンもありそう？

https://github.com/Kaichi-Irie/leetcode-python/pull/14/files#r2265202569

frontier, exploredという命名もある。なんかかっこいい。

https://github.com/Kaichi-Irie/leetcode-python/pull/14/files#diff-391c3d74247119fbe22d578e7083cbe4e2390802ebeae45a1e1c7000c21fba1aR138-R141

height = 0, width = 0のエッジケースに対する意識。
どうしても「問題を解く」という意識が抜けきれずどちらも1以上が保証されているからいいかと思ってしまいがちなので
見習いたいと思った。
今回の場合は何も無いときはエラーを出すか何も無いので0を返すか。

https://github.com/Kaichi-Irie/leetcode-python/pull/14/files#r2266898843

`is_water(next_row, next_col) or is_visited[next_row][next_col]`
これが複数回出てくるのでまとめてしまってもいいかもしれない。

count_connected_islandsよりサイズを測定するという意味でmeasure_islandとかのほうがいいかな？
countのほうが離散的な感じがして整数だと分かりやすい気もするけど…どうだろう。

今までinner functionは関数の頭に全て定義するようにしていたが今回は使う直前で定義してみる形にした。
このあたりGoogleのスタイルガイドとかPEP8とかに「こうしたほうがよい」みたいな指針が無く、
GPT的には関数の頭に定義するのがおすすめだと言われたのでそれに従っていたが、読む人的にはどうなんだろう。

あれ…そういえばitertools.productのimport書くの忘れてたけどちゃんと動いてるな…。

> Most libraries are already imported automatically for your convenience, such as array, bisect, collections. If you need more libraries, you can import it yourself.
https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages

へえ～、そうだったのか。いちいちimport書かなくてもよかったんだ…

# ステップ３

３回連続で書けるようになったので一旦完了。
書いている途中にmeasure_islandの最初にnot is_frontierで0を返すようにしたので、
回すときにis_frontierのif分岐が要らないことに気づいた。
再帰の終了条件が分かりやすくなるという以外にもメリットがあった。
