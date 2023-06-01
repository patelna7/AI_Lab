import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 
import numpy as np
from sklearn.cluster import AgglomerativeClustering

#x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]

#y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

N = 1000

min = -8
max = 8
  
x = min + (max - min) * np.random.rand(N)
y = min + (max - min) * np.random.rand(N)

data = list(zip(x, y))
#kmeans = KMeans(n_clusters=4)
#kmeans.fit(data)

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)


plt.scatter(x, y, c=cluster.labels_)
plt.show()
