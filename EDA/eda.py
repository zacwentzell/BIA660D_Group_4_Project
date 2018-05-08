# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# In[2]:


pop_lyrics = pd.read_csv('lyrics_pop_300.csv')
del (pop_lyrics['Unnamed: 0'])
pop_lyrics

# In[13]:


p = pop_lyrics.Artist.value_counts()
p

# In[14]:


plt.hist(p)
plt.show()

# In[16]:


country_lyrics = pd.read_csv(
    'lyrics_country_299.csv')
del (country_lyrics['Unnamed: 0'])
country_lyrics

# In[17]:


c = country_lyrics.Artist.value_counts()
c

# In[19]:


plt.hist(c)
plt.show()

# In[6]:


general_lyrics = pop_lyrics.append(country_lyrics)

# In[7]:


general_lyrics


# In[8]:


def StopStem(df):
    stop = []

    df['Lyrics'] = df['Lyrics'].apply(lambda x: re.sub(r'\[.*?\]', ' ', x))

    df['Lyrics'] = df['Lyrics'].apply(lambda x: re.sub('[’‘!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+', ' ', x))
    #     df["Lyrics"] = re.sub(r'[.*?]', '', df['Lyrics'].string)
    df["Lyrics"] = df['Lyrics'].str.lower().replace('[^\w\s]', ' ')
    df["Lyrics"] = df['Lyrics'].str.replace('\r\n', ' ')
    df['Lyrics'] = df['Lyrics'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    return df


# In[9]:


general_lyrics = StopStem(general_lyrics)

# In[10]:


general_lyrics

# In[11]:


import matplotlib.pyplot as plt

# In[12]:


general_lyrics['Lyrics_length'] = general_lyrics.Lyrics.apply(lambda x: len(x))

# In[13]:


general_lyrics.Lyrics_length.describe()

# In[32]:


general_lyrics.Lyrics_length.plot(kind='kde', logx=True)
plt.show()

# In[15]:


general_lyrics['Genre_type'] = general_lyrics.Genre.apply(lambda x: 0 if 'Pop' in x else 1)

# In[33]:


general_lyrics.plot(kind="scatter", x="Genre_type", y="Lyrics_length", alpha=0.2)
plt.show()


# In[17]:


def cleanText(corpus):
    preprocessed_sentences = []
    word_bag = []
    stop_words = common_terms
    pos_to_keep = ('NOUN', 'PROPN', 'ADJ', 'VERB')
    for doc in nlp.pipe(corpus, n_threads=8):
        keep_tokens_string = ' '.join([t.lemma_ for t in doc if t.pos_ in pos_to_keep and t.lemma_ not in stop_words])
        preprocessed_sentences.append(keep_tokens_string)
    preprocessed_sentences = [z.lower().replace('\n', ' ').split() for z in preprocessed_sentences]
    for sentence in preprocessed_sentences:
        for word in sentence:
            word_bag.append(word)
    return word_bag


# In[18]:


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


# In[48]:


pop_lyrics = StopStem(pop_lyrics)

# In[20]:


country_lyrics = StopStem(country_lyrics)

# In[21]:


import spacy

nlp = spacy.load('en')

# In[22]:


X = pop_lyrics.loc[:, 'Lyrics']

# In[23]:


X

# In[24]:


pop_word_bag = cleanText(X)

# In[25]:


pop_word_bag

# In[26]:


unique_words_pop = list(set(pop_word_bag))

freq_pop = []
for word in unique_words_pop:
    freq_pop.append((word, pop_word_bag.count(word)))

# sort
freq_pop.sort(key=lambda x: x[1], reverse=True)

# In[27]:


freq_pop

# In[28]:


pop_word_bag = []
for i in freq_pop:
    for w in range(i[1]):
        pop_word_bag.append(i[0])

pop_word_bag

# In[29]:


# wc = WordCloud(background_color="white",width=5000, height=3000, max_words=200,random_state=42)


# In[50]:


Y = country_lyrics.loc[:, 'Lyrics']
Y

# In[51]:


country_word_bag = cleanText(Y)
country_word_bag

# In[52]:


unique_words_country = list(set(country_word_bag))

freq_country = []
for word in unique_words_country:
    freq_country.append((word, country_word_bag.count(word)))

# sort
freq_country.sort(key=lambda x: x[1], reverse=True)

# In[53]:


freq_country

# In[54]:


country_word_bag = []
for i in freq_country:
    for w in range(i[1]):
        country_word_bag.append(i[0])

country_word_bag

# In[55]:


wordcloud_country = WordCloud(background_color="white", width=1000, height=1000, collocations=False, ).generate(
    ' '.join(country_word_bag))

# In[56]:


import matplotlib.pyplot as plt

plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_country)
plt.axis("off")
plt.show()

# In[57]:


wordcloud_pop = WordCloud(background_color="white", width=1000, height=1000, collocations=False, ).generate(
    ' '.join(pop_word_bag))

# In[58]:


import matplotlib.pyplot as plt

plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_pop)
plt.axis("off")
plt.show()

# In[59]:


common_word = []

for i in freq_pop:
    for j in freq_country:
        if i[0] == j[0]:
            common_word.append(i[0])
common_word

# In[60]:


pop_word_bag_unique = []
for i in pop_word_bag:
    if i not in common_word:
        pop_word_bag_unique.append(i)
pop_word_bag_unique

# In[61]:


country_word_bag_unique = []
for i in country_word_bag:
    if i not in common_word and i.isalpha():
        country_word_bag_unique.append(i)
country_word_bag_unique

# In[62]:


wordcloud_country = WordCloud(background_color="white", width=1000, height=1000, collocations=False).generate(
    ' '.join(country_word_bag_unique))

# In[63]:


plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_country)
plt.axis("off")
plt.show()

# In[64]:


wordcloud_pop = WordCloud(background_color="white", width=1000, height=1000, collocations=False, ).generate(
    ' '.join(pop_word_bag_unique))

# In[65]:


plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_pop)
plt.axis("off")
plt.show()

# In[68]:


X1 = pop_lyrics.loc[:, 'Artist']
X1.values

# In[69]:


wordcloud_pop_artists = WordCloud(background_color="white", width=1000, height=1000, collocations=False, ).generate(
    ' '.join(X1))

# In[70]:


plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_pop_artists)
plt.axis("off")
plt.show()

# In[71]:


Y1 = country_lyrics.loc[:, 'Artist']
Y1.values

# In[73]:


wordcloud_country_artists = WordCloud(background_color="white", width=1000, height=1000, collocations=False, ).generate(
    ' '.join(Y1))

# In[74]:


plt.figure(figsize=(20, 15))
plt.imshow(wordcloud_country_artists)
plt.axis("off")
plt.show()

