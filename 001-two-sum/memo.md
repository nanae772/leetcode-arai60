# ステップ１

整数配列numsと整数targetが与えられるので、nums[i] + nums[j] = targetとなる(i, j)(i < j)を求める問題
これを満たす(i, j)は唯一であることが保証されている

1. 全てのペアを試す全探索解,O(n^2)
2. dictを使う解法,O(n)
3. ソート＋二分探索を使う解法,O(nlogn)

が思いついた。

1は最大でn=10^4になり、ペアの個数はn(n-1)/2=約5*10^7回のループが回り、１回のループで１回の足し算と１回の比較を行う。
練習会の前にこの問題をテストとしてやっており、そのときはO(n^2)の解を提出して1800msほどで通っていた。
これは通らないと思っていたが意外と通るらしい。
参考までにC++で同じO(n^2)解を書くと約50msだった。Pythonはコンパイラ言語と比較して2~3桁遅いとのことなのでこんなものだろうか。

dictを使う解について。jを見ているときに
nums[i] = target - nums[j]
となるi(i < j)があるかどうか分かればよいので、左から順に見ていくときに
value -> index となるように保存しておけば上を満たすiがあるかをO(1)で判定できるので
全体としての計算量がO(n)になる。

ソートを使う解は、まずa = (value, index)のタプルのリスト に変換してvalueの昇順にソートしておく。
a[i]を見るときに、a[i+1:]の中から target - a[i].value となるものを二分探索で探せばO(logN)なので
全体としての計算量はO(NlogN)になる。
久しぶりにbisectライブラリを使った。
https://docs.python.org/ja/3.11/library/bisect.html

問題ではtargetになる(i,j)があると保証されていたが無い場合がある。
エラーを投げるのも一つの手だろうけど今回は[-1, -1]を返すことにした。
例えばPythonのstr.findは見つからない場合は-1を返すことになっているため、indexを探す際に見つからなかったら
-1を返すというのはそんなにおかしくなさそうだと思った。
https://docs.python.org/ja/3/library/stdtypes.html#str.find

ちなみにstr.indexは見つからなかったらValueError
https://docs.python.org/ja/3/library/stdtypes.html#str.index

# ステップ２

naive解はこれでよいだろう。

dict解もこれで良い気がする、`target - nums[i]`を`diff`という変数に入れてもいいかも、くらい。

bisect解はbisect_leftした後のvalue_index_pairs[left_at_least_diff]の名前が良いものが思い浮かばず
step1では適当にしてしまった。
そのままvalue_at_least_diff, index_at_least_diff とかだろうか。
min_value_at_least_diff, min_index_at_least_diffのほうが分かりやすいか？
日本語で言うと「diff以上の最小の値」になるだろうし。

bisect解は返り値のインデックスが逆順になってしまうことがある。
この問題では

> You can return the answer in any order.

と書いているので問題無いと言えば問題無いが確かに気持ちが悪いし、このライブラリを使う側の気持ちになると順序がバラバラだと
変なバグを起こしそうになり嫌な気持ちになりそう。
一応sortedにしておこう。

https://github.com/locol23/leetcode/pull/1/files#r2249246805

# ステップ３

３回連続で通せるようになったので一旦完了。
