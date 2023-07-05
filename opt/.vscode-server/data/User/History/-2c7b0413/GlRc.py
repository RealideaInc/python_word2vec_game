from gensim.models import KeyedVectors
model_dir = './jawiki.entity_vectors.300d.txt'
w2v_model = KeyedVectors.load_word2vec_format(model_dir, binary=False)
w2v_model.save_word2vec_format('./jawiki.entity_vectors.300d.bin', binary=True)