import numpy as np
from gensim.models import Word2Vec

#生成向量文件，向量可视化作用
dirpath = ".\\data\\utlp2\\vector"
model = Word2Vec.load(dirpath+'\\word2vec.model')

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

#不写属性标题，用于向量可视化
def user2csv():
    readnodetype()  # 构造userlist

    fvec = open(dirpath+'\\U_vec.txt', 'w')
    findex = open(dirpath+'\\U_index.txt', 'w')
    findex.write("user"+'\n')

    for u in userlist:
        vec = np.array(model[u])
        findex.write(u+'\n')

        fvec.write(u + '\t')
        temp = str(vec[0])
        for i in range(1,len(vec)):
            temp = temp + '\t' + str(vec[i])
        temp = temp + '\n'
        fvec.write(temp)

if __name__ == "__main__":

    user2csv()  # id向量类别信息写入csv文件 可以用weka进行聚类分类
