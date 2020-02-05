from gensim.models import Word2Vec
from sklearn.cluster import KMeans
from sklearn import metrics
from pylab import *

dirpath = ".\\data\\utlp2\\vector"
model = Word2Vec.load(dirpath+'\\word2vec.model')

# 存放poi和user的id
poilist = list()
userlist = list()
def indata():
    # 读取用户和poi列表
    f = open(dirpath + '\\node_type_mapings.txt', 'r')
    line = f.readline()
    while line:
        list = line.strip().split(" ")
        if (len(list) == 2):
            if (list[1].__eq__("poi")):
                poilist.append(list[0])
            elif (list[1].__eq__("user")):
                userlist.append(list[0])
        line = f.readline()
    f.close()

    # 读取原始数据
    X = []
    for u in userlist:
        v = model[u]
        X.append(v)

    #转化为numpy array
    X = np.array(X)
    # print(X)
    return X

def Kmeans(X,n_clusters):   # 参数簇的数量
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
    X = range(3, 15)
    plt.xlabel('k clusters', size=20)
    plt.ylabel('Silhouette Coefficient', size=20)
    plt.plot(X, S, 'o-')
    plt.show()

def drawchi(S):
    X = range(3, 15)
    plt.xlabel('k clusters', size=20)
    plt.ylabel('Calinski-Harabasz Index', size=20)
    plt.plot(X, S, 'o-')
    plt.show()

def drawsse(S):
    X = range(3, 15)
    plt.xlabel('k clusters', size=20)
    plt.ylabel('SSE', size=20)
    plt.plot(X, S, 'o-')
    plt.show()

def draw(n_clusters):
    # 输出X中每项所属分类的一个列表
    # print(cls.labels_)
    X = indata()
    cls = KMeans(n_clusters).fit(X)
    # 画图
    markers = []
    a = ['*', 'o', '+', 's', 'v', '.', ',', '^', '<', '>', '1', '2', '3', '4', 'p', 'h', 'H', 'x', 'D', 'd', '|', '-']
    for i in range(n_clusters):
        markers.append(a[i])

    for i in range(n_clusters):
        members = cls.labels_ == i
        plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c='b', alpha=0.5)  # 画与menbers数组中匹配的点

    plt.title('cluster')
    plt.show()

S,CHI,SSE = [],[],[]
X = indata()
for i in range(3, 15):
    cls,s,chi,sse = Kmeans(X,i)
    S.append(s)
    CHI.append(chi)
    SSE.append(sse)
draws(S)
drawchi(CHI)
drawsse(SSE)
# draw(10)

