from gensim.models import KeyedVectors
model_dir = '/root/jawiki.entity_vectors.100d.txt'
w2v_model = KeyedVectors.load_word2vec_format(model_dir, binary=False)
w2v_model.save_word2vec_format('/root/jawiki.entity_vectors.100d.bin', binary=True)