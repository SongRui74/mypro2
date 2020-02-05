import multiprocessing
from gensim.models import Word2Vec, word2vec

#https://blog.csdn.net/u011748542/article/details/85880852   参数说明
dirpath = ".\\data\\utlp2\\vector"
sentences = word2vec.LineSentence(dirpath+'\\random_walks.txt')
model = Word2Vec(sentences, sg=1, hs=0, negative=5, size=200, window=5, min_count=1, workers=multiprocessing.cpu_count())

model.save(dirpath+'\\word2vec.model')


# model = Word2Vec.load(dirpath+'\\word2vec.model')
# print(model['USER_1083'])
#
# for key in model.similar_by_word('USER_1083', topn=10):
#     print(key)
# print(model.similarity('u2099','u2099'))
# print(model.wv.doesnt_match(u"u2099 u650 u1".split()))
#