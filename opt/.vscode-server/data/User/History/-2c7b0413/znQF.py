from gensim.models import KeyedVectors

w2v_model = KeyedVectors.load_word2vec_format('Path to text file', binary=False)
w2v_model.save_word2vec_format('Path to output', binary=True)