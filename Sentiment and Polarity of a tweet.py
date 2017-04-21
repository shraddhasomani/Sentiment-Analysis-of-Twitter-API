
# coding: utf-8

# In[1]:

import pip
pip.main(["install","twitter"])
pip.main(["install","textblob"])
from textblob import TextBlob
import nltk
import numpy as np
import pandas as pd
import json
import twitter
from twitter import Twitter 
from twitter import OAuth 
from twitter import TwitterHTTPError 
from twitter import TwitterStream
from pandas.io.json import json_normalize
from matplotlib import pyplot as plt
from collections import Counter


# In[3]:

ACCESS_TOKEN = '3151548164-KGXKM6vZipCfBfIA16bUxBaNhIcg7CmfiYb6iWU'
ACCESS_SECRET = '8qKGbi5JRnrZb3yKcKijbYxVHVZ4lFonuQDsN3dWonzao'
consumer_key = 'nqn05e7YWcj57FBzJhu2vJpQU'
consumer_secret = 'a3Y1S2DXVkbRoGaO3NMgstbGm4LSAyRnKSeShseZFrFqWmTwJo'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, consumer_key, consumer_secret)
twitter = Twitter(auth=oauth)


# In[4]:

# Search for a term
# Normalize the results into pandas table.
# Take the tweet messages in the "text" column (row by row) and break it into words
search_results = twitter.search.tweets(q = 'SuperBowl', count = 250)
statuses = search_results['statuses']
df = json_normalize(search_results, 'statuses')
status_texts = df["text"]
status_texts


# In[5]:

# Loop through each row run the sentiment analysis on each sentence
polarity = []
subjectivity = []
for sen in status_texts:
    polarity.append(TextBlob(sen).sentiment.polarity)
    subjectivity.append(TextBlob(sen).sentiment.subjectivity)


# In[6]:

# Store the polarity and subjectivity into another data table
df_final = pd.DataFrame({'Polarity' : polarity, 'Subjectivity' : subjectivity})
df_final


# In[7]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# In[8]:

# Plot polarity and subjectivity
df_final[['Polarity','Subjectivity']].plot()


# In[ ]:



