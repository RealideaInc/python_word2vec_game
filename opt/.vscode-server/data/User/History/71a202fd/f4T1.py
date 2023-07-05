from gensim.models import KeyedVectors


model_dir = '../entity_vector/entity_vector.model.bin'
model: KeyedVectors = KeyedVectors.load_word2vec_format(model_dir, binary=True)


def parsing(formula: str):
    formula = formula.split('+')
    print(formula)
    formula = map(lambda x: x.split('-'), formula)
    print(formula)
    

# while True:
formula = input('式を入力')
print(formula)
print(parsing(formula))
# print(model.most_similar(positive=['東京', 'イギリス'], negative=['日本']))

