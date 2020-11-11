# サンプルコード1
# matplotlibの使い方
from pylab import plot, show
x_num = [1, 2, 3]
y_num = [2, 4, 6]
plot(x_num, y_num)
show()

# サンプルコード2
# matplotlibの使い方
from pylab import plot, show
x_num = [1, 2, 3]
y_num = [2, 4, 6]
plot(x_num, y_num, marker = 'o')
show()

# サンプルコード3
# matplotlibの使い方
from pylab import plot, show
point_rank = [12, 37, 63, 88, 107, 132, 157, 164, 190]
plot(point_rank, marker = 'o')
show()

# サンプルコード4
# matplotlibの使い方
from pylab import plot, show
point_rank = [12, 37, 63, 88, 107, 132, 157, 164, 190]
round = range(1,10)
plot(round, point_rank, marker='o')
show()

# サンプルコード5
# matplotlibの使い方
from pylab import plot, show
HAM = [12,37,63,88,107,132,157,164,190]
BOT = [25,43,58,58,73,89,107,117,135]
FER = [0,15,33,52,77,95,110,110,110]
NOR = [16,26,26,36,38,39,45,57,65]
round = range(1,10)
plot(round, HAM, round, BOT, round, FER, round, NOR, marker='o')
show()

# サンプルコード6
# matplotlibの使い方
from pylab import plot, show, legend
HAM = [12,37,63,88,107,132,157,164,190]
BOT = [25,43,58,58,73,89,107,117,135]
FER = [0,15,33,52,77,95,110,110,110]
NOR = [16,26,26,36,38,39,45,57,65]
round = range(1,10)
plot(round, HAM, marker='o', label="HAM")
plot(round, BOT, marker='o', label="BOT")
plot(round, FER, marker='o', label="FER")
plot(round, NOR, marker='o', label="NOR")
legend()
show()

# サンプルコード7
# matplotlibの使い方
!pip install japanize-matplotlib
from pylab import plot, show, legend, title, xlabel, ylabel
import japanize_matplotlib 
HAM = [12,37,63,88,107,132,157,164,190]
BOT = [25,43,58,58,73,89,107,117,135]
FER = [0,15,33,52,77,95,110,110,110]
NOR = [16,26,26,36,38,39,45,57,65]
round = range(1,10)
plot(round, HAM, marker='o', label="HAM")
plot(round, BOT, marker='o', label="BOT")
plot(round, FER, marker='o', label="FER")
plot(round, NOR, marker='o', label="NOR")
legend()
title("F1 2020 獲得ポイントの推移")
xlabel("ラウンド")
ylabel("獲得ポイント")
show()

# サンプルコード8
# matplotlibの使い方
from pylab import plot, show, legend, title, xlabel, ylabel, axis
import japanize_matplotlib 
HAM = [12,37,63,88,107,132,157,164,190]
BOT = [25,43,58,58,73,89,107,117,135]
FER = [0,15,33,52,77,95,110,110,110]
NOR = [16,26,26,36,38,39,45,57,65]
round = range(1,10)
axis([1,9,0,200])
plot(round, HAM, marker='o', label="HAM")
plot(round, BOT, marker='o', label="BOT")
plot(round, FER, marker='o', label="FER")
plot(round, NOR, marker='o', label="NOR")
legend()
title("F1 2020 獲得ポイントの推移")
xlabel("ラウンド")
ylabel("獲得ポイント")
show()

# サンプルコード9
# matplotlibの使い方
import matplotlib.pyplot as plt
def my_plot_sample():
    x_num = [1, 2, 3]
    y_num = [2, 4, 6]
    plt.plot(x_num, y_num)
    plt.show()
if __name__ == '__main__':
    my_plot_sample()

# サンプルコード10
# matplotlibの使い方
import matplotlib.pyplot as plt
import japanize_matplotlib 
HAM = [12,37,63,88,107,132,157,164,190]
BOT = [25,43,58,58,73,89,107,117,135]
FER = [0,15,33,52,77,95,110,110,110]
NOR = [16,26,26,36,38,39,45,57,65]
round = range(1,10)
plt.axis([1,9,0,200])
plt.plot(round, HAM, marker='o', label="HAM")
plt.plot(round, BOT, marker='o', label="BOT")
plt.plot(round, FER, marker='o', label="FER")
plt.plot(round, NOR, marker='o', label="NOR")
plt.legend()
plt.title("F1 2020 獲得ポイントの推移")
plt.xlabel("ラウンド")
plt.ylabel("獲得ポイント")
plt.savefig('output.png')
plt.show()

# サンプルコード11
# 万有引力の法則
import matplotlib.pyplot as plt
import japanize_matplotlib 
def plot_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel("距離[m]")
    plt.ylabel("引力[N]")
    plt.axis([0, 1000, 0, 6e-15])
    plt.show()
def make_newtons():
    r = range(100, 1001, 50)
    F = []
    G = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5
    for distance in r:
        F.append(G * (m1 * m2) / (distance**2))
    plot_graph(r, F)
if __name__ == '__main__':
    make_newtons()

# サンプルコード11
# 投射運動
# !pip install japanize-matplotlib      # japanize_matplotlibのインストール
from matplotlib import pyplot as plt
import japanize_matplotlib 
import math
def plot_trajectory(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel("距離")
    plt.ylabel("高さ")
    plt.axis([0, 100, 0, 50])
    plt.show()
def make_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8                             # 重力加速度
    time = 2 * u * math.sin(theta) / g  # ボールが地面に落ちるまでの時間
    intervals = []                      # プロット間隔
    idx = 0
    while idx < time:
        intervals.append(idx)
        idx = idx + 0.1
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t**2)
    plot_trajectory(x, y)
if __name__ == '__main__':
    make_trajectory(30, 60)