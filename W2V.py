import multiprocessing
from gensim.models import Word2Vec, word2vec

#https://blog.csdn.net/u011748542/article/details/85880852   参数说明
sentences = word2vec.LineSentence('.\\data\\ucu\\vector\\random_walks.txt')
model = Word2Vec(sentences, sg=1, hs=0, negative=5, size=200, window=5, min_count=1, workers=multiprocessing.cpu_count())

print(model['u2099'])
print(model.similarity('u2099','u2099'))
print(model.wv.doesnt_match(u"u2099 u650 u1".split()))

for key in model.similar_by_word('u2099', topn=10):
    print(key)
