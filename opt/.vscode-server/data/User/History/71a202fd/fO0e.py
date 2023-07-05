from gensim.models import KeyedVectors
from pprint import pprint

model_dir = '../entity_vector/entity_vector.model.bin'
model: KeyedVectors = KeyedVectors.load_word2vec_format(model_dir, binary=True)
# model_dir = './jawiki.entity_vectors.300d.txt'
# model: KeyedVectors = KeyedVectors.load_word2vec_format(model_dir, binary=False)

def parsing(formula: str):
    pos = []
    neg = []
    formula = formula.replace(' ', '')
    formula = formula.replace('　', '')
    formula = formula.replace('＋', '+')
    formula = formula.split('+')
    formula = list(map(lambda x: x.split('-'), formula))
    for x in formula:
        if len(x) == 1:
            pos += x
        else:
            pos += x[0:1]
            neg += x[1:]
    return pos, neg

while True:
    formula = input('\n式を入力\n')
    pos, neg = parsing(formula)
    print(pos)
    print(neg)
    try:
        pprint(model.most_similar(positive=pos, negative=neg, topn=20))
    except KeyError as e:
        print('そんな単語は私は知りません：', e)

