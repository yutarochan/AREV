'''
AREV - Model Management Class
Author: Yuya Jeremy Ong (yuyajeremyong@gmail.com)
'''
import gensim
import logging

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

class Model:
    def __init__(self, model_path):
        print 'Initializing Model: ' + model_path
        self.model_path = model_path
        self.model = gensim.models.Word2Vec.load(model_path)

        # Load Corpus
        print 'Loading Corpus...'
        self.vectors = []
        for i in self.model.index2word:
            self.vectors.append(self.model[i])
        print 'Done'

    def get3DModel(self):
        print 'Perform PCA for 3 Components'
        pca = PCA(n_components=3, whiten=True)
        return pca.fit(self.vectors).transform(self.vectors)

    def get2DModel(self):
        print 'Perform PCA for 2 Components'
        pca = PCA(n_components=2, whiten=True)
        return pca.fit(self.vectors).transform(self.vectors)

if __name__ == '__main__':
    m = Model('../data/sample.model')
