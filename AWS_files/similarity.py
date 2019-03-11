import pandas as pd
import numpy as np
import pickle

import MeCab
m = MeCab.Tagger ("-Ochasen")

from pykakasi import kakasi
kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

def mecab_list(text,ctr=0):
    tagger = MeCab.Tagger("-Ochasen")
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_class = []
    result = []
    while node:
        word = node.surface
        wclass = node.feature.split(',')
        if (conv.do(word).isalpha() == True or conv.do(wclass[6]).isalpha() == True) and \
            (wclass[0] == '名詞' or (wclass[0] == '動詞' and wclass[1] == '自立') or wclass[0] == '形容詞' or wclass[0] == '`副詞'):
            p1 = ''
            p2 = ''
            if wclass[0] == '名詞':
                p1 = 'no'
                p2 = 'g'
            elif wclass[0] == '動詞':
                p1 = 've'
                if wclass[1] == '自立':
                    p2 = 'i'
            elif wclass[0] == '形容詞':
                p1 = 'aj'
                p2 = 'g'
            else:
                p1 = 'av'
                p2 = 'g'
                
            try:
                word_class.append((word,wclass[0],wclass[1],wclass[6],wclass[7],conv.do(wclass[6])))
                result.append(conv.do(wclass[6]) + '_' + p1 + '_' + p2 + '_' + wclass[6])
            except:
                word_class.append((word,wclass[0],wclass[1],wclass[6],word,conv.do(word)))
                result.append(conv.do(word) + '_' + p1 + '_' + p2 + '_' + wclass[6])
        node = node.next
    if ctr == 0:
        return result
    elif ctr == 1:
        return word_class

from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

df_clean = pickle.load(open('./similarity_data/df_clean.pkl', 'rb'))
vectorizer = pickle.load(open('./similarity_data/vectorizer.pkl', 'rb'))
corpus_vectorized = pickle.load(open('./similarity_data/corpus_vectorized.pkl', 'rb'))

def generate_similarity(sample,disnum=5):
    sample_mecabed = mecab_list(sample)
    sample_vec = vectorizer.transform([' '.join(sample_mecabed).replace('*','_')]).toarray()

    df_res = df_clean.copy()
    df_res['similarity'] = np.dot(corpus_vectorized.toarray(), sample_vec.T) 
    # Cosine similarity = cosine values since the tf-idf vectors are l2 normed.
    df_res.columns = ['DMM uknow URL','Question Line', 'Similarity']

    return df_res[df_res['Similarity']>0].sort_values(by='Similarity', ascending=False).head(disnum)