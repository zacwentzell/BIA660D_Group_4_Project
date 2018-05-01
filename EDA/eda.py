# coding: utf-8

# In[32]:

import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud

# In[2]:

pop_lyrics = pd.read_csv('lyrics_pop_300.csv')
del (pop_lyrics['Unnamed: 0'])
pop_lyrics

# In[3]:

country_lyrics = pd.read_csv('lyrics_country_299.csv')
del (country_lyrics['Unnamed: 0'])
country_lyrics

# In[4]:

general_lyrics = pop_lyrics.append(country_lyrics)

# In[5]:

general_lyrics


# In[6]:

def StopStem(df):
    stop = []

    df['Lyrics'] = df['Lyrics'].apply(lambda x: re.sub(r'\[.*?\]', ' ', x))

    df['Lyrics'] = df['Lyrics'].apply(lambda x: re.sub('[’‘!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+', ' ', x))
    #     df["Lyrics"] = re.sub(r'[.*?]', '', df['Lyrics'].string)
    df["Lyrics"] = df['Lyrics'].str.lower().replace('[^\w\s]', ' ')
    df["Lyrics"] = df['Lyrics'].str.replace('\r\n', ' ')
    df['Lyrics'] = df['Lyrics'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    return df


# In[7]:

general_lyrics = StopStem(general_lyrics)

# In[8]:

general_lyrics

# In[9]:

import matplotlib.pyplot as plt

# In[10]:

general_lyrics['Lyrics_length'] = general_lyrics.Lyrics.apply(lambda x: len(x))

# In[13]:

general_lyrics.Lyrics_length.describe()

# In[15]:

general_lyrics.Lyrics_length.plot(kind='kde', logx=True)
plt.show()

# In[16]:

general_lyrics['Genre_type'] = general_lyrics.Genre.apply(lambda x: 0 if 'Pop' in x else 1)

# In[19]:

general_lyrics.plot(kind="scatter", x="Genre_type", y="Lyrics_length", alpha=0.2)
plt.show()

# In[20]:

pop_lyrics.Artist.value_counts()

# In[21]:

country_lyrics.Artist.value_counts()


# In[33]:

def cleanText(corpus):
    preprocessed_sentences = []
    word_bag = []
    stop_words = common_terms
    pos_to_keep = ('NOUN', 'PROPN', 'ADJ', 'VERB')
    for doc in nlp.pipe(corpus, n_threads=8):
        keep_tokens_string = ' '.join([t.lemma_ for t in doc if t.pos_ in pos_to_keep and t.lemma_ not in stop_words])
        #         doc = nlp(lyrics)
        #         lyrics = ' '.join([t.lemma_ for t in doc if t.pos_ in pos_to_keep and t.lemma_ not in stop_words])
        preprocessed_sentences.append(keep_tokens_string)
    preprocessed_sentences = [z.lower().replace('\n', ' ').split() for z in preprocessed_sentences]
    for sentence in preprocessed_sentences:
        for word in sentence:
            word_bag.append(word)
    return word_bag


# In[34]:

from sklearn.feature_extraction import stop_words

common_terms = list(stop_words.ENGLISH_STOP_WORDS) + ["m", "re", "ll", "s", "ve", "d", 'ca', 'is', '-PRON-', 't', 'g',
                                                      'don', 'ain', 'b', 'r']


def StopStem(df):
    stop = common_terms

    df['Lyrics'] = df['Lyrics'].apply(lambda x: re.sub(r'\[.*?\]', ' ', x))

    df['Lyrics'] = df['Lyrics'].apply(lambda x: re.sub('[’‘!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+', ' ', x))
    #     df["Lyrics"] = re.sub(r'[.*?]', '', df['Lyrics'].string)
    df["Lyrics"] = df['Lyrics'].str.lower().replace('[^\w\s]', ' ')
    df["Lyrics"] = df['Lyrics'].str.replace('\r\n', ' ')
    df['Lyrics'] = df['Lyrics'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    return df


# In[35]:

pop_lyrics = StopStem(pop_lyrics)

# In[36]:

country_lyrics = StopStem(country_lyrics)

# In[37]:

import spacy

nlp = spacy.load('en')

# In[38]:

X = pop_lyrics.loc[:, 'Lyrics']

# In[39]:

X

# In[40]:

pop_word_bag = cleanText(X)

# In[41]:

pop_word_bag

# In[47]:

wordcloud_pop = WordCloud(background_color="white", width=5000, height=3000, max_words=200).generate(
    ' '.join(pop_word_bag))

# In[50]:

import matplotlib.pyplot as plt

plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_pop)
plt.axis("off")
plt.show()

# In[51]:

X = country_lyrics.loc[:, 'Lyrics']

# In[54]:

country_word_bag = cleanText(X)

# In[55]:

country_word_bag

# In[56]:

wordcloud_country = WordCloud(background_color="white", width=5000, height=3000, max_words=200).generate(
    ' '.join(country_word_bag))

# In[57]:

plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_country)
plt.axis("off")
plt.show()

# In[ ]:



