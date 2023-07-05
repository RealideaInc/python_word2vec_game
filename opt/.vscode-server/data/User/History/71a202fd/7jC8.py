from gensim.models import KeyedVectors


model_dir = '../entity_vector/entity_vector.model.bin'
model: KeyedVectors = KeyedVectors.load_word2vec_format(model_dir, binary=True)

class Formula:
    def parsing(self):

    

while True:
    formula = Formula(input('式を入力'))
    print(model.most_similar(positive=['東京', 'イギリス'], negative=['日本']))

