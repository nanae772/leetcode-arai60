# ステップ１

ソート済みの連結リストから重複を削除する問題。

単に前から順番に見ていって同じ値のノードがあったら飛ばしていって、同じ値でなくなるノードに
繋ぎかえるということをすればよいだけかな？

1. 与えられた連結リストを直接書き換えて重複削除する
2. 新たに重複の無い連結リストを作る

2パターン考えられるけどどっちだろうか。
こういう問題はなんとなく1かなという気もするけど、関数定義がOptional[ListNode]を返すようになっているので2かもしれない。
1だったら返り値はNoneになっていそう。

とりあえず2の方針で実装をする。

5回もエラーを出してしまった後にやっと通った。
簡単だと思ったけどコードを書くのが下手で結構バグらせてしまった。

# ステップ２

`node.next`と`next_node`が個人的にこんがらがるため、`next_node`は別の名前にしたい。
１つ後という意味で`successor`がよく使われるので`succ_node`はどうだろうか。
と思ってGPTに相談したがsuccessorは直後のノード(=node.next)を指すので辞めたほうが良いと言われた。
代わりに提案されたのが `next_distinct, lookahead, runner` あたり。

あともう一個は、これはそもそもちゃんと新しい連結リストを作れているのか？というのが自信が無い。

nodeやnext_nodeに代入する際にクラスのインスタンスのコピーが渡っているならできていそうだが、
参照が渡っているならこれは参照先のインスタンスを書き換えているので元のリストを壊してしまう。
そのあたりどうなっているのかちゃんと調べ直さないといけない。

簡単なコードを書いて確かめる。

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


a = Person("Bob", 20)
b = a
b.age = 30

print(id(a), id(b))
print(a is b)
print(a.name, a.age)
print(b.name, b.age)
```

結果は以下。

```
139810823707728 139810823707728
True
Bob 30
Bob 30
```

単に代入しただけでは同じインスタンスを指しているので、元のインスタンスを書き換えてしまうことが分かった。
このことはPythonの公式ドキュメントにも書いていた。

> Python において代入文はオブジェクトをコピーしません。代入はターゲットとオブジェクトの間に束縛を作ります。

https://docs.python.org/ja/3.11/library/copy.html

そもそも新しい連結リストを作りたいならListNodeの新しいインスタンスを１個ずつ作っていくべきだった。

ステップ１で「関数の返り値がOptional[ListNode]だから新しいリストを作る」と言っていたが、
それだとメソッド名がdeleteDuplicatesなのはおかしい気がする。createSortedUniqListとかになっていそう。
やっぱり元のリストを上書きしていく方法がよかったのかもしれない。
そっちも実装することにする（といってもstep1.pyは結果的に上書きになってしまっていた）。

ちょっとChatGPTと話していると

```python
while node is not None:
    while node.next is not None and node.val == node.next.val:
        node.next = node.next.next
    node = node.next
```

これは

```python
while node:
    while node.next and node.val == node.next.val:
        node.next = node.next.next
    node = node.next
```

こう書けるということが分かった。そういえばこのような書き方も出来たな。

確かに下の方がコードが短く簡潔なのだけど、nodeがNone以外のfalthyな値を取ってしまったときにバグるというのが
少し怖い。Pythonだと0,空文字列,空のリストなどがそれに当たる。

今回はnodeの型がListNode|Noneなのでそのあたりのfalthyな値は入らないので大丈夫ではあるけど、
基本的にPythonは何の型でも変数に入れられてしまうので怖いなという気持ちはある。
プロジェクトによってはmypy, pyrightなどの型チェックを入れていることもあるのでそういった場面ではいいかもしれない。

あとpythonに慣れていない人が読んだ時に`while node:`というコードを見て初見で理解しづらいのではないかという懸念もある。

なのでちょっと長くなるが`node is not None`と明示的に条件を書く方を採用することにする。

# ステップ3

２パターンどちらも３回連続で書けるようになった。

docstringをつけてみるとやはり新しい連結リストを作る方はdeleteDuplicatesというメソッド名と食い違うので、
in-placeで行うほうが正しい気がした。
