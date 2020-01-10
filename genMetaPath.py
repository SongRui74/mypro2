import sys
import os
import random
from collections import Counter

class MetaPathGenerator:
    def __init__(self):
        self.id_user = dict()
        self.id_loc = dict()
        self.id_cate = dict()
        self.id_time = dict()
        self.cate_userlist = dict()
        self.user_catelist = dict()
        self.time_userlist = dict()
        self.user_timelist = dict()
        self.time_catelist = dict()
        self.cate_timelist = dict()
        self.loc_userlist = dict()
        self.user_loclist = dict()
        self.loc_catelist = dict()
        self.cate_loclist = dict()
    # def readtestdata(self, dirpath):
    #     self.id_poi.clear()
    #     self.id_user.clear()
    #     self.poi_userlist.clear()
    #     self.user_poilist.clear()
    #
    #     with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
    #         for line in adictfile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 self.id_user[toks[0]] = toks[1].replace(" ", "")
    #
    #     with open(dirpath + "\\id_poi.txt",'r', encoding='ISO-8859-1') as cdictfile:
    #         for line in cdictfile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 self.id_poi[toks[0]] = toks[0]
    #
    #     with open(dirpath + "\\user_poi.txt",'r', encoding='ISO-8859-1') as pafile:
    #         for line in pafile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 u, p = toks[0], toks[1]
    #                 #u:'37',p:'4e3e097552b1a04aff2139ff'
    #                 if u not in self.user_poilist:
    #                     self.user_poilist[u] = []
    #                 self.user_poilist[u].append(p)
    #                 if p not in self.poi_userlist:
    #                     self.poi_userlist[p] = []
    #                 self.poi_userlist[p].append(u)

    #构造
    def read_ucudata(self, dirpath):
        self.id_cate.clear()
        self.id_user.clear()
        self.cate_userlist.clear()
        self.user_catelist.clear()

        with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_user[toks[1].replace(" ", "")] = toks[1].replace(" ", "")

        with open(dirpath + "\\id_category.txt",'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_cate[toks[0].replace(" ", "").replace("\n", "")] = toks[1].replace(" ", "")

        with open(dirpath + "\\user_category.txt",'r', encoding='UTF-8') as pafile:
            for line in pafile:
                toks = line.split("\t")
                if len(toks) == 2 and len(toks[1]) != 0:
                    u, c = toks[0].replace(" ", ""), toks[1].replace(" ", "").replace("{", "").replace("}", "").replace("\"", "").replace("\n", "")
                    #u:'37',p:'4e3e097552b1a04aff2139ff'
                    cate = c.split(',')

                    if u not in self.user_catelist:
                        self.user_catelist[u] = []
                    for i in range(0,len(cate)):
                        self.user_catelist[u].append(cate[i])

                    for i in range(0,len(cate)):
                        if cate[i] not in self.cate_userlist:
                            self.cate_userlist[cate[i]] = []
                        self.cate_userlist[cate[i]].append(u)

    def generate_random_ucu(self, outfilename, numwalks, walklength):
        outfile = open(outfilename, 'w', encoding="ISO-8859-1")
        for user in self.user_catelist:
            user0 = user
            for j in range(0, numwalks):
                outline = self.id_user[user0]
                for i in range(0, walklength):
                    cates = self.user_catelist[user]
                    numa = len(cates)
                    cateid = random.randrange(numa)
                    cate = cates[cateid]
                    #outline += " " + self.id_cate[cate]    #优化

                    users = self.cate_userlist[cate]
                    numa = len(users)
                    userid = random.randrange(numa)
                    user = users[userid]
                    outline += " " + self.id_user[user]
                outfile.write(outline + "\n")
        outfile.close()

    def read_utlcdata(self, dirpath):
        self.id_cate.clear()
        self.id_user.clear()
        self.id_time.clear()
        self.id_loc.clear()
        self.user_timelist.clear()
        self.time_userlist.clear()
        self.time_catelist.clear()
        self.cate_timelist.clear()
        self.user_loclist.clear()
        self.loc_userlist.clear()
        self.loc_catelist.clear()
        self.cate_loclist.clear()

        with open(dirpath + "\\id_user.txt", 'r', encoding='ISO-8859-1') as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_user[toks[1].replace(" ", "")] = toks[1].replace(" ", "")

        with open(dirpath + "\\id_category.txt", 'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_cate[toks[0].replace(" ", "").replace("\n", "")] = toks[1].replace(" ", "")    #cate ,cate_id

        with open(dirpath + "\\id_time.txt",'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_time[toks[1]] = toks[1]  #time ,time_id

        with open(dirpath + "\\id_loc.txt", 'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_loc[toks[1]] = toks[1]  #loc_content loc_id

        with open(dirpath + "\\checkin.txt",'r', encoding='ISO-8859-1') as pafile:
            for line in pafile:
                toks = line.strip().split("\t")
                if len(toks) == 4:
                    u, t, l, c = toks[0], toks[1], toks[2], toks[3].replace(" ", "").replace("{", "").replace("}", "").replace("\"", "").replace("\n", "")
                    #u:'37',p:'4e3e097552b1a04aff2139ff'

                    if u not in self.user_timelist:
                        self.user_timelist[u] = []
                    self.user_timelist[u].append(t)
                    if t not in self.time_userlist:
                        self.time_userlist[t] = []
                    self.time_userlist[t].append(u)

                    if u not in self.user_loclist:
                        self.user_loclist[u] = []
                    self.user_loclist[u].append(l)
                    if l not in self.loc_userlist:
                        self.loc_userlist[l] = []
                    self.loc_userlist[l].append(u)

                    cate = c.split(',')
                    if t not in self.time_catelist:
                        self.time_catelist[t] = []
                    for i in range(0, len(cate)):
                        self.time_catelist[t].append(cate[i])

                    for i in range(0, len(cate)):
                        if cate[i] not in self.cate_timelist:
                            self.cate_timelist[cate[i]] = []
                        self.cate_timelist[cate[i]].append(t)

                    if l not in self.loc_catelist:
                        self.loc_catelist[l] = []
                    for i in range(0, len(cate)):
                        self.loc_catelist[l].append(cate[i])

                    for i in range(0, len(cate)):
                        if cate[i] not in self.cate_loclist:
                            self.cate_loclist[cate[i]] = []
                        self.cate_loclist[cate[i]].append(l)

    def generate_random_utlc(self, outfilename, numwalks, walklength):
        outfile = open(outfilename, 'w', encoding="ISO-8859-1")
        for user in self.id_user:
            user0 = user
            for j in range(0, numwalks):
                outline = self.id_user[user0]  #路径U

                # 随机一个t0
                ts0 = self.user_timelist[user0]
                t0 = ts0[random.randrange(len(ts0))]
                # 随机一个l0
                ls0 = self.user_loclist[user0]
                l0 = ls0[random.randrange(len(ls0))]

                for i in range(0, walklength):
                    r = random.randrange(2)
                    cates = list()
                    users = list()
                    if r == 0:  # 随机选择，0表示选择时间
                        ts = self.user_timelist[user]
                        for i in range(1000):
                            tid = random.randrange(len(ts))
                            t = ts[tid]
                            if abs(int(t[1:]) - int(t0[1:])) < 3:
                                # outline += " " + self.id_time[t]  # 路径U T
                                t0 = t
                                cates = self.time_catelist[t]
                                break

                    else:    # 随机选择，1表示选择位置
                        ls = self.user_loclist[user]
                        for i in range(1000):
                            lid = random.randrange(len(ls))
                            l = ls[lid]
                            if str(l).__eq__(l0):
                                # outline += " " + self.id_loc[l]  # 路径U L
                                l0 = l
                                cates = self.loc_catelist[l]
                                break

                    if not cates:
                        break
                    else:
                        cateid = random.randrange(len(cates))
                        cate = cates[cateid]
                        # outline += " " + self.id_cate[cate]  # 路径U X C

                    r = random.randrange(2)
                    if r == 0:
                        ts = self.cate_timelist[cate]
                        for i in range(1000):
                            tid = random.randrange(len(ts))
                            t = ts[tid]
                            if abs(int(t[1:]) - int(t0[1:])) < 3:
                                # outline += " " + self.id_time[t]  # 路径U X C T
                                t0 = t
                                users = self.time_userlist[t]
                                break

                    else:
                        ls = self.cate_loclist[cate]
                        for i in range(1000):
                            lid = random.randrange(len(ls))
                            l = ls[lid]
                            if str(l).__eq__(l0):
                                # outline += " " + self.id_loc[l]  # 路径U X C L
                                l0 = l
                                users = self.loc_userlist[l]
                                break

                    if not users:
                        break
                    else:
                        userid = random.randrange(len(users))
                        user = users[userid]
                        outline += " " + self.id_user[user]  # 路径U X C L U

                outfile.write(outline + "\n")
        outfile.close()

dirpath = ".\\data\\ucu\\input"
upuoutfilename = ".\\data\\ucu\\vector\\random_walks.txt"

utlc_dirpath = ".\\data\\utlc\\input"
utlc_outfilename = ".\\data\\utlc\\vector\\random_walks.txt"

if __name__ == "__main__":
    numwalks = 50  #同一个起点开始的路径的数量
    walklength = 10  #路径长度
    mpg = MetaPathGenerator()

    # mpg.read_ucudata(dirpath)
    # mpg.generate_random_ucu(upuoutfilename, numwalks, walklength)

    mpg.read_utlcdata(utlc_dirpath)
    mpg.generate_random_utlc(utlc_outfilename, numwalks, walklength)

