import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import pairwise_kernels

train_movies_1 = pd.read_csv('C:/final.csv')
#print(type(train_movies_1))
train_movies_1.dtypes
train_movies_1.isnull().sum(axis=0)
train_movies_1.dropna()
train_movies_1.drop(["Unnamed: 0","Unnamed: 0.1",'genre_ids'], axis = 1,inplace = True)
#train_movies_1
train_movies_1=train_movies_1.drop_duplicates()
#train_movies_1
train_movies_1=train_movies_1.reset_index(drop=True)
#train_movies_1
train_movies_1.loc[(train_movies_1['id'] == 639721)]
train_movies_1.loc[(train_movies_1['id'] == 11508)]
tf=TfidfVectorizer(stop_words="english")
tf_matrix= tf.fit_transform(train_movies_1['overview'])
consine_sim= pairwise_kernels(tf_matrix,tf_matrix)
indeces= pd.Series(train_movies_1.index, index=train_movies_1["id"])
idx= indeces[774021]

def get_recomendation(id, semilar= consine_sim):
    idx= indeces[id]
    sim_score= enumerate(consine_sim[idx])
    sim_score= sorted (sim_score, key=lambda x: x[1], reverse= True)
    sim_score=sim_score[1:10]
    sim_index=[i[0] for i in sim_score]
    print(train_movies_1["id"].iloc[sim_index])
    print(type(train_movies_1["id"].iloc[sim_index]))

    for value  in train_movies_1["id"].iloc[sim_index]:
	    print(value)

    

get_recomendation(19995)


# train_credict = pd.read_csv('C:/final.csv')
# train_movies = pd.read_csv('C:/final.csv')
# train_movies
# tf=TfidfVectorizer(stop_words="english")
# train_movies['overview']= train_movies['overview'].fillna("")
# tf_matrix= tf.fit_transform(train_movies['overview'])
# consine_sem= pairwise_kernels(tf_matrix,tf_matrix)
# train_movies.index

# indeces= pd.Series(train_movies.index, index=train_movies["id"]).drop_duplicates()
# indeces

# def get_recomendation(id, semilar= consine_sem):
#     idx= indeces[id]
#     sem_score= enumerate(consine_sem[idx])
#     sem_score= sorted (sem_score, key=lambda x: x[1], reverse= True)
#     sem_score[1:11]
#     sem_index=[i[0] for i in sem_score]
#     print(train_movies["id"].iloc[sem_index])
