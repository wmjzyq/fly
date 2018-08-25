from time import time
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

"""
加载训练集news
"""
print('loading train dataset ...')
news_train = load_files(r'G:\news')
print('summary:{0} document in {1} categories.'.format(len(news_train.data),len(news_train.target_names)))

"""
向量化、特征提取
"""
print('Vectorizing train dataset ...')
t = time()
vectorizer = TfidfVectorizer(encoding='utf-8')
X_train = vectorizer.fit_transform(d for d in news_train.data)
print('n_samples: %d, n_features: %d' % X_train.shape)
print("number of non-zero features in sample [{0}]:{1}".format(news_train.filenames[0], X_train[0].getnnz()))
print("done in {0} seconds".format(time()-t))
print(X_train.todense().shape)

"""
训练朴素贝叶斯算法
"""
print("training models ...".format(time()-t))
t = time()
y_train = news_train.target
clf = MultinomialNB(alpha=0.0001)
clf.fit(X_train, y_train)
joblib.dump(clf,'Bayesian.pkl')
joblib.dump(vectorizer, 'vector')
train_score = clf.score(X_train, y_train)
print("train score:{0}".format(train_score))
print("done in {0} seconds".format(time()-t))