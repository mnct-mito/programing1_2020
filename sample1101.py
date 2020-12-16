# スライド P4
list = [11, 23, 1, 45, 32, 78, 90, 7]
list.sort()
list

# スライド P6
list = [11, 23, 1, 45, 32, 78, 90, 7]
list.sort(reverse = True)
list

# スライド P8
t_list = [(3, 'y'), (2, 'x'), (1, 'z'), (4, 'u')]
t_list.sort(key = lambda x: x[1])
t_list

# スライド P10
x = 10
y = 20
y, x = x, y
print(x, y)

# スライド P12
data = [1, 2, 3, 4, 5]
data[2:4] = ['Three', 'Four', 'Five']
data => [1, 2, 'Three', 'Four', 5]

# スライド P16
dict1 = {"iPhone 12 Pro":"106,800円", "iPhone 12":"85,800円", "iPhone 12 mini":"74,800円"}
dict2 = {"iPhone 11":"64,800円", "iPhone XR":"54,800円", "iPhone SE (第2世代)":"44,800円"}
dict1.update(dict2)
print(dict1)

# スライド P17
# 英文はスティーブ・ジョブスの有名なスピーチより引用
data = "Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find yourself hitchhiking on if you were so adventurous. Beneath it were the words: Stay Hungry. Stay Foolish. It was their farewell message as they signed off. Stay Hungry. Stay Foolish. And I have always wished that for myself. And now, as you graduate to begin anew, I wish that for you."
words = {}
for word in data.split():
    words[word] = words.get(word, 0) + 1
d = [(v, k) for k, v in words.items()]
d.sort()
d.reverse()
for count, word in d[:100]:
    print(count, word)

# スライド P25
# ファイル名とファイルのパスは各自の環境に合わせて書き換える
file = open("/content/drive/My Drive/****/****.txt", "r", encoding="utf-8")
str = file.read()
words = {}
for word in str.split():
    words[word] = words.get(word, 0) + 1
d = [(v, k) for k, v in words.items()]
d.sort()
d.reverse()
for count, word in d[:100]:
    print(count, word)
file.close()