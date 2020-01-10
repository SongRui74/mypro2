import numpy as np
import json
import csv
#生成csv文件用于聚类
# 路径要改！！！！！！！！！！！！！！！
dir = ".\\data\\utlc\\recommend"
dirpath = ".\\data\\utlc\\vector"

index2nodeid = json.load(open(dir +"\\log\\index2nodeid.json"))
index2nodeid = {int(k): v for k, v in index2nodeid.items()}
nodeid2index = {v: int(k) for k, v in index2nodeid.items()}
node_embeddings = np.load(dir +"\\log\\node_embeddings.npz")['arr_0']
# 100维的向量
# 存放poi和user的id
poilist = list()
userlist = list()
poi_cate = dict()

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

def poi_category():
    f = open(dirpath+"\\poi_cate_index.txt", 'r')
    line = f.readline()
    while line:
        list = line.strip().split("\t")
        if (len(list) == 2):
            if (list[0] not in poi_cate):
                poi_cate[list[0]] = list[1]
        line = f.readline()
    f.close()
def poi2csv():
    readnodetype()  # 构造poilist
    poi_category()  # 构造poi_cate字典
    with open(dir+"\\vector.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name # 写入多行用writerows
        row = []
        row.append('index')
        for i in range(0, 100):
            row.append('n' + str(i))
        row.append('category')
        writer.writerow(row)

        for poi in poilist:
            cate = poi_cate[poi]
            vec = np.array(node_embeddings[nodeid2index[poi]])
            temp = []
            temp.append(poi)
            for i in range(0, len(vec)):
                temp.append(vec[i])
            temp.append(cate)
            writer.writerow(temp)

def user2csv():
    readnodetype()  # 构造userlist

    with open(dir+"\\vector.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name # 写入多行用writerows
        row = []
        row.append('index')
        for i in range(0, 100):
            row.append('n' + str(i))
        writer.writerow(row)

        for u in userlist:
            vec = np.array(node_embeddings[nodeid2index[u]])
            temp = []
            temp.append(u)
            for i in range(0, len(vec)):
                temp.append(vec[i])
            writer.writerow(temp)

user2csv()
