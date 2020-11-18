# サンプルコード1
x = 10				# 代入する値は適当に設定する
if x%2 == 0:
    print('Even')	# 偶数
else:
    print('Odd')	# 奇数


# サンプルコード2
x = 10				# 代入する値は適当に設定する
if x%2 == 0:		# 2で割り切れる場合
    if x%3 == 0:	# 3で割り切れる場合
        print('Divisible by 2 and 3')	
    else:			# 3で割り切れない場合
        print('Divisible by 2 and not by 3')
elif x%3 == 0:		# 3で割り切れる場合
    print('Divisible by 3 and not by 2')


# サンプルコード3
x = 1			# xの初期値
while True:		# Trueの間ループ
    if x%11 == 0 and x%12 == 0:
        break	# 11と12で割り切れる場合ループを抜ける
    x = x + 1	# xの値を1増やす
print(x, 'is divisible by 11 and 12')