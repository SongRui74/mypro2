import numpy as np
import json
#生成向量文件，向量可视化作用
dir = ".\\data\\utlc\\recommend"
dirpath = ".\\data\\utlc\\vector"

index2nodeid = json.load(open(dir+"\\log1\\index2nodeid.json"))
index2nodeid = {int(k): v for k, v in index2nodeid.items()}
nodeid2index = {v: int(k) for k, v in index2nodeid.items()}
node_embeddings = np.load(dir+"\\log1\\node_embeddings.npz")['arr_0']
# 100维的向量

# 存放poi和user的id
poilist = list()
userlist = list()

#读取用户和poi列表
def readnodetype():
    f = open(dirpath+'\\node_type_mapings.txt', 'r')
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

id_cate = dict()
poi_cate = dict()
def poi_category():
    #读id_cate
    with open(".\\data\\100user\\id_category.txt", 'r', encoding='ISO-8859-1') as cdictfile:
        for line in cdictfile:
            toks = line.strip().split("\t")
            if len(toks) == 2:
                id_cate[toks[0]] = toks[1]
    #构造poi-cate
    with open(".\\data\\100user\\train.txt", 'r', encoding='ISO-8859-1') as pafile:
        for line in pafile:
            toks = line.strip().split("\t")
            if len(toks) == 4:
                p, c = toks[2], toks[3]
                if p not in poi_cate:
                    poi_cate[p] = id_cate[c]

def poi2csv():
    readnodetype()  # 构造poilist
    #print(poilist)
    poi_category()  # 构造poi_cate字典
    #print(poi_cate)

    fvec = open(dir+'\\vec.txt', 'w')
    findex = open(dir+'\\index.txt', 'w')

    findex.write("poi"+"\t"+"category"+'\n')
    for poi in poilist:
        cate = poi_cate[poi]
        vec = np.array(node_embeddings[nodeid2index[poi]])

        findex.write(poi+"\t"+cate+'\n')

        temp = str(vec[0])
        for i in range(1,len(vec)):
            temp = temp + '\t' + str(vec[i])
        temp = temp + '\n'
        fvec.write(temp)

#不写属性标题，用于向量可视化
def user2csv():
    readnodetype()  # 构造userlist

    fvec = open(dir+'\\vec.txt', 'w')
    findex = open(dir+'\\index.txt', 'w')
    findex.write("user"+'\n')

    for u in userlist:
        vec = np.array(node_embeddings[nodeid2index[u]])
        findex.write(u+'\n')

        fvec.write(u + '\t')
        temp = str(vec[0])
        for i in range(1,len(vec)):
            temp = temp + '\t' + str(vec[i])
        temp = temp + '\n'
        fvec.write(temp)

if __name__ == "__main__":

    user2csv()  # id向量类别信息写入csv文件 可以用weka进行聚类分类
