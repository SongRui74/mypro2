import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from pylab import *

def indata():
    # 读取原始数据
    dir = ".\\data\\ucu\\recommend"
    X = []
    f = open(dir+'\\vec.txt')
    for v in f:
        s = v.split('\t')
        temp = []
        for i in range(1,len(s)):
            temp.append(float(s[i].replace('\n','')))
        X.append(temp)

    #转化为numpy array
    X = np.array(X)
    # print(X)
    return X

def Kmeans(n_clusters):   # 参数簇的数量
    X = indata()
    # 开始调用函数聚类
    cls = KMeans(n_clusters).fit(X)
    # 轮廓系数Silhouette Coefficient取值为[-1, 1]，其值越大越好。
    # Calinski-Harabasz越大则聚类效果越好,数值越小可以理解为：组间协方差很小，组与组之间界限不明显
    # SSE 误差平方和越小越好
    s = metrics.silhouette_score(X, cls.labels_, metric='euclidean')
    chi = metrics.calinski_harabaz_score(X, cls.labels_)
    sse = cls.inertia_
    print("轮廓系数：", metrics.silhouette_score(X, cls.labels_, metric='euclidean'))
    print("Calinski-Harabasz Index：",metrics.calinski_harabaz_score(X, cls.labels_))
    print("SSE：", cls.inertia_)
    return cls,s,chi,sse

def draws(S):
    X = range(2, 22)
    plt.xlabel('k clusters', size=20)
    plt.ylabel('Silhouette Coefficient', size=20)
    plt.plot(X, S, 'o-')
    plt.show()

def drawchi(S):
    X = range(2, 22)
    plt.xlabel('k clusters', size=20)
    plt.ylabel('Calinski-Harabasz Index', size=20)
    plt.plot(X, S, 'o-')
    plt.show()

def drawsse(S):
    X = range(2, 22)
    plt.xlabel('k clusters', size=20)
    plt.ylabel('SSE', size=20)
    plt.plot(X, S, 'o-')
    plt.show()


S,CHI,SSE = [],[],[]
for i in range(2, 22):
    cls,s,chi,sse = Kmeans(i)
    S.append(s)
    CHI.append(chi)
    SSE.append(sse)

draws(S)
drawchi(CHI)
drawsse(SSE)


# def draw(n_clusters):
#     # 输出X中每项所属分类的一个列表
#     # print(cls.labels_)
#     X = indata()
#     cls = Kmeans()
#     # 画图
#     markers = []
#     a = ['*', 'o', '+', 's', 'v', '.', ',', '^', '<', '>', '1', '2', '3', '4', 'p', 'h', 'H', 'x', 'D', 'd', '|', '-']
#     for i in range(n_clusters):
#         markers.append(a[i])
#
#     for i in range(n_clusters):
#         members = cls.labels_ == i  # members是布尔数组
#         plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c='b', alpha=0.5)  # 画与menbers数组中匹配的点

#     plt.title('cluster')
#     plt.show()
