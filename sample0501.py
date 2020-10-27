# サンプルコード1
# ディクショナリの例
address = {"学校名" : "舞鶴高専", "郵便番号" : "625-8511", "住所" : "舞鶴市字白屋234"}
address


# サンプルコード2
# 例えば「住所」を取り出したい場合（表示したい場合）
print(address["住所"])


# サンプルコード3
# 例えば「住所」の内容を修正したい場合
address["住所"] = "京都府舞鶴市字白屋234"
address


# サンプルコード4
# 例えば「代表番号」を新しい要素として追加したい場合
address["代表番号"] = "0773-62-5600"
address


# サンプルコード5
# 例えば「郵便番号」を削除したい場合
del address["郵便番号"]
address


# サンプルコード6
# for文を使いディクショナリの要素を表示することも可能
for key in address:
    print(key,address[key])


# サンプルコード7
# Fizz Buzz問題(詳しくは以下を参照)
# https://ja.wikipedia.org/wiki/Fizz_Buzz
count = 1
while count <= 20:
    if count % 3 == 0 and count % 5 == 0:
        print("Fizz Buzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count = count + 1


# サンプルコード8
# continue文の使い方
for val in range(10):
    # valが5のとき繰り返しの先頭に戻る
    if val == 5:
        continue
    print(val)


# サンプルコード9
# break文の使い方
for val in range(10):
    # valが5のとき繰り返しを終了する
    if val == 5:
        break
    print(val)


# サンプルコード10
# 関数にデフォルト引数を定義する
def fizzbuzz(count = 20, fizz_mod = 3, buzz_mod = 5):
    for count in range(1, count + 1):
        if count % fizz_mod == 0 and count % buzz_mod == 0:
            print("Fizz Buzz")
        elif count % fizz_mod == 0:
            print("Fizz")
        elif count % buzz_mod == 0:
            print("Buzz")
        else:
            print(count)
fizzbuzz()

# サンプルコード11
# 関数とローカル変数の確認
# fizzbuzz関数の外で変数に代入
count = 0
# 関数内で繰り返し変数といて同じ変数名の変数を利用
def fizzbuzz(count = 20, fizz_mod = 3, buzz_mod = 5):
    for count in range(1, count + 1):
        if count % fizz_mod == 0 and count % buzz_mod == 0:
            print("Fizz Buzz")
        elif count % fizz_mod == 0:
            print("Fizz")
        elif count % buzz_mod == 0:
            print("Buzz")
        else:
            print(count)
print(count) # 関数の外では変数の値は変化しないことを確認