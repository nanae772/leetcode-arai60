# ステップ１

文字列の中に１つだけある文字のうち一番左にあるものを見つける

aからzまで一文字ずつ、sの中に１つしかないかを判定し１つしかないならそのインデックスを返して、
その中の最小のものを取る、というやり方(O(N))

dictで
文字 → (最初のindex, 文字のカウント)
を保持しておき、最後に文字のカウントが1であるものについてのみ、最初のindexのminを取るやり方(O(N))

sの文字を左から見ていってs[i]を見たときにs[i+1:]に同じ文字があるかループを回してチェックする方法(O(N^2))

などのやり方がありそうだと考えた。

一番シンプルかつ拡張性の高い(a-z以外の文字が来てもそのまま使える)２番目のやり方でやることにする。

書けた。values()にすべきところをitems()にしてしまって1WA。
max, minのdefault引数については他の人のコードレビューなどを見て知った。

# ステップ２

他の人の解法を見る。

https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.dofnod9ahqqt

文字コードは魔境という話があった。

https://github.com/tarinaihitori/leetcode/pull/15/files

最初にsをCounterにぶち込んでからもう一度sを前から見てcount=1のものがあったらそれを返す、という方法があった。
そのほうがシンプルで分かりやすいかも。

https://github.com/tarinaihitori/leetcode/pull/15/files#r1831269678

上でodaさんがコメントしているNFC/NFD正規化の違いによって「が」が同じに見えるのに違う判定になったりする奴、最近あったなあ。
Macで作ったファイルがWindowsで見ると濁点が分かれててなんかおかしくなってるとか、MacからGoogle Driveにあげたファイル名の文字列を
取得して一致判定すると一致してるように見えるのに一致してないことになってるとか…。
NFD正規化とUTF-8-MAC正規化はまた違うものらしくあまりちゃんと理解できていないが、そのあたりが絡んでて難しい話だった。

[誤解の多い「NFD問題とUTF-8-MAC問題」を解説する - macOSの濁点を含むファイル名の扱い](https://qiita.com/ko1nksm/items/3a66197efd1c096a801f)
[ファイルアップロードではNFC/NFD問題に気をつけろ！~MacファイルシステムにおけるUnicode正規化の闇~](https://zenn.dev/hacobell_dev/articles/68ccc92bffd6cc)

Pythoの公式ドキュメントにPythonで文字列がどのように扱われているかが書かれていた。
Pythonでは文字列はUnicode文字列、すなわちUnicodeコードポイントのシーケンスとして扱っているとのこと。
https://docs.python.org/3/howto/unicode.html

文字のインデックスを扱う場合、特に合字には気をつけなければいけないかなと思った。
例えば"ÁÁa"という文字列が与えられたとき、見た目として2番目にあるaがfirst uniqueなので
`firstUniqChar("ÁÁa") = 2` となりそうだが、実際はÁがAと結合アクセント (U+0301)の合字なので
この文字列におけるaのインデックスは4になり、`firstUniqChar("ÁÁa") = 4`である。

「１文字に見えるなら１文字とする」とするにはどうすればいいんだろうと思ってGPTに聞いてみたら、
書記素クラスタ(grapheme cluster, 見た目１文字の塊のこと)を扱えるライブラリを使うとよいとのこと。

# ステップ３

３回連続で書けるようになったので一旦完了。
