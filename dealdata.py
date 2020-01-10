import random
def quchong(dirpath):
    a = 0
    readDir = dirpath + "\\node_type.txt"  # old
    writeDir = dirpath + "\\node_type_mapings.txt"  # new
    # txtDir = "/home/Administrator/Desktop/１"
    lines_seen = set()
    outfile = open(writeDir, "w")
    f = open(readDir, "r")
    for line in f:
        if line not in lines_seen:
            a += 1
            outfile.write(line)
            lines_seen.add(line)
            # print(a)
            # print('\n')
    outfile.close()
    print("success")

def train_testdata():
    delnum = 30#删除少于delnum 个签到的用户
    a = 0.8 #80%作为训练集
    data = '.\\data\\foursquare\\checkin.txt'
    train = '.\\data\\foursquare\\train.txt'
    test = '.\\data\\foursquare\\test.txt'

    #打开原文件
    f = open(data, 'r', encoding='UTF-8', errors='ignore')
    line = f.readline()

    fa = open(train, 'w')
    fb = open(test, 'w')
    fa.write(line)  #写列名
    fb.write(line)

    # 统计user_poi dict
    user_poilist = dict()
    while line:
        line = f.readline()
        toks = line.strip().split("\t")
        if len(toks) == 4: #17
            u, tl, p, c = toks[0], toks[1], toks[2], toks[3]
            # u, t, l, p, c = toks[0], toks[8], toks[9], toks[13], toks[16]
            # if u is not None and t is not None and l is not None and p is not None and c is not None:
            if u not in user_poilist:
                user_poilist[u] = []
            user_poilist[u].append(str(line))
    f.close()

    # #地点少于delnum的删除
    # for user in list(user_poilist):
    #     if len(user_poilist[user]) <= delnum:
    #         user_poilist.pop(user)

    #写入train&test，并且每一项不为空
    for user in user_poilist:
        num = round(a*len(user_poilist[user])) #训练集  每个用户的签到数量, 四舍五入
        l = user_poilist[user]
        for i in range(0,num):
            fa.write(str(l[i]))

        for i in range(num,len(user_poilist[user])):
            fb.write(str(l[i]))

    fa.close()
    fb.close()

def xieleibie(dirpath):
    f = open(dirpath + '\\random_walks.txt','r', encoding='UTF-8', errors='ignore')
    line = f.readline()              		 # 调用文件的 readline()方法
    with open(dirpath + '\\node_type.txt', 'w') as fb:
        while line:
            list = line.strip().split(" ")
            for i in range(0,len(list)):
                if list[i].startswith('u'):
                    fb.write(list[i] + " user\n")
                    #print(list[i]+" user")
                elif list[i].startswith('p'):
                    fb.write(list[i] + " poi\n")
                    #print(list[i]+" poi")
                elif list[i].startswith('t'):
                    fb.write(list[i] + " time\n")
                    #print(list[i] + " t")
                elif list[i].startswith('l'):
                    fb.write(list[i] + " loc\n")
                    # print(list[i] + " l")
                elif list[i].startswith('c'):
                    fb.write(list[i] + " category\n")
                    # print(list[i] + " category")
            line = f.readline()
        f.close()

# train_testdata()

# ucu = ".\\data\\ucu\\vector"
# xieleibie(ucu)
# quchong(ucu)

utlc= ".\\data\\utlc\\vector"
xieleibie(utlc)
quchong(utlc)