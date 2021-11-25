import pandas as pd
from pandas import DataFrame,Series
import json
import csv
from tqdm.notebook import tqdm


dx=pd.read_csv("C:/profile_movie.csv")

Thriller=dx.loc[(dx['label'] == 'Thriller') & (dx['popularity']>100)].head(25)
print(Thriller)
Thriller
#Action
Action=dx.loc[(dx['label'] == 'Action') & (dx['popularity']>1)].head(25)
Action
Adventure=dx.loc[(dx['label'] == 'Adventure') & (dx['popularity']>1)].head(25)
Adventure
Animation=dx.loc[(dx['label'] == 'Animation') & (dx['popularity']>1)].head(25)
Animation
Comedy=dx.loc[(dx['label'] == 'Comedy') & (dx['popularity']>1)].head(25)
Comedy




History=dx.loc[(dx['label'] == 'History') & (dx['popularity']>1)].head(25)
Horror=dx.loc[(dx['label'] == 'Horror') & (dx['popularity']>1)].head(25)
Music=dx.loc[(dx['label'] == 'Music') & (dx['popularity']>1)].head(25)
Mystery=dx.loc[(dx['label'] == 'Mystery') & (dx['popularity']>1)].head(25)
Romance=dx.loc[(dx['label'] == 'Romance') & (dx['popularity']>1)].head(25)
Science_Fiction =dx.loc[(dx['label'] == 'Science Fiction') & (dx['popularity']>1)].head(25)
TV_Movie=dx.loc[(dx['label'] == 'TV Movie') & (dx['popularity']>1)].head(25)
Thriller=dx.loc[(dx['label'] == 'Thriller') & (dx['popularity']>1)].head(25)
War=dx.loc[(dx['label'] == 'War') & (dx['popularity']>1)].head(25)
Western=dx.loc[(dx['label'] == 'Western') & (dx['popularity']>1)].head(25)
