### 解説用です
import matplotlib.pyplot as plt

# 事前にx, yを定義
plt.scatter(x,y)

# ただのタイトル
plt.title("Sample")

# X軸のラベル
plt.xlabel("X-label")

# Y軸のラベル
plt.ylabel("Y-lael")

# グリッドを付ける
plt.grid()

# 出力
plt.show()

### 株の前日の終値のデータをグラフにしてみた ###
import matplotlib.pyplot as plt
stock = sp.genfromtxt("stock_test.tsv", delimiter="\t")
a = stock[:,0]
b = stock[:,2]
a = a[~sp.isnan(a)]
b = b[~sp.isnan(b)]
plt.scatter(a,b)
plt.title("Stock data 8/10-10/10")
plt.xlabel("prev_closing_price")
plt.ylabel("No.")
plt.grid()
plt.show()
