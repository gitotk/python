from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt

#データ作成
data, label = datasets.make_blobs(n_samples=500, n_features=2, centers=5)

#インスタンス取得
e = cluster.KMeans(n_clusters=5)
#クラスタリング
e.fit(data)

print(e.labels_)
print(e.cluster_centers_)

#データを散布図に作成
plt.scatter(data[:, 0], data[:, 1], marker="o", c=e.labels_, edgecolor="k")
#クラスタの中心を散布図に作成s
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker="x")

plt.show()
