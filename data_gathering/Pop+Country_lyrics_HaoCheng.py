# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re

# # Pop songs

# In[8]:

url1 = 'https://genius.com/api/songs/chart?page='
url2 = '&per_page=10&tag_id=16&time_period=day'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

df_pop = pd.DataFrame(columns=['Song_Name', 'Artist', 'Genre', 'Lyrics'])

for x in range(1, 11):
    json_pop = requests.get(url1 + str(x) + url2, headers=headers).content

    con = json.loads(json_pop)

    #     for t in range(0,9):
    lyrics_List = con["response"]["chart_items"]

    for item in lyrics_List:

        url = item['item']['url']
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')

        lyrics_list_soup = soup.find('div', attrs={'class': 'lyrics'})

        if (lyrics_list_soup.p is not None):
            lyrics1_list_soup = lyrics_list_soup.find('p').getText()
            if (lyrics1_list_soup == ""):
                lyrics1_list_soup = "no lyrics"
        else:
            lyrics1_list_soup = "no lyrics"

        Song_Name = soup.find('h1', attrs={'class': 'header_with_cover_art-primary_info-title'}).getText()
        artist_list_soup = soup.find('h2')
        Artist = artist_list_soup.find('a',
                                       attrs={'class': 'header_with_cover_art-primary_info-primary_artist'}).getText()
        Genre = "Pop"
        Lyrics = lyrics1_list_soup

        #         lyrics_data = [Song_Name, Artist, Genre, Lyrics]
        #         print(lyrics_data)

        df_pop.loc[len(df_pop)] = [Song_Name, Artist, Genre, Lyrics]
df_pop

# output =  df_pop.to_json(orient='records')
# with open('lyrics_pop.json', 'w') as f:
#     f.write(output)


# In[9]:

# https://genius.com/api/songs/chart?page=1&per_page=10&tag_id=16&time_period=month
url1 = 'https://genius.com/api/songs/chart?page='
url2 = '&per_page=10&tag_id=16&time_period=month'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

df_pop1 = pd.DataFrame(columns=['Song_Name', 'Artist', 'Genre', 'Lyrics'])

for x in range(1, 11):
    json_pop1 = requests.get(url1 + str(x) + url2, headers=headers).content

    con = json.loads(json_pop1)

    #     for t in range(0,9):
    lyrics_List = con["response"]["chart_items"]

    for item in lyrics_List:

        url = item['item']['url']
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')

        lyrics_list_soup = soup.find('div', attrs={'class': 'lyrics'})

        if (lyrics_list_soup.p is not None):
            lyrics1_list_soup = lyrics_list_soup.find('p').getText()
            if (lyrics1_list_soup == ""):
                lyrics1_list_soup = "no lyrics"
        else:
            lyrics1_list_soup = "no lyrics"

        Song_Name = soup.find('h1', attrs={'class': 'header_with_cover_art-primary_info-title'}).getText()
        artist_list_soup = soup.find('h2')
        Artist = artist_list_soup.find('a',
                                       attrs={'class': 'header_with_cover_art-primary_info-primary_artist'}).getText()
        Genre = "Pop"
        Lyrics = lyrics1_list_soup

        #         lyrics_data = [Song_Name, Artist, Genre, Lyrics]
        #         print(lyrics_data)

        df_pop1.loc[len(df_pop1)] = [Song_Name, Artist, Genre, Lyrics]
df_pop1

# In[10]:

# https://genius.com/api/songs/chart?page=1&per_page=10&tag_id=16&time_period=all_time
url1 = 'https://genius.com/api/songs/chart?page='
url2 = '&per_page=10&tag_id=16&time_period=all_time'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

df_pop2 = pd.DataFrame(columns=['Song_Name', 'Artist', 'Genre', 'Lyrics'])

for x in range(1, 11):
    json_pop2 = requests.get(url1 + str(x) + url2, headers=headers).content

    con = json.loads(json_pop2)

    #     for t in range(0,9):
    lyrics_List = con["response"]["chart_items"]

    for item in lyrics_List:

        url = item['item']['url']
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')

        lyrics_list_soup = soup.find('div', attrs={'class': 'lyrics'})

        if (lyrics_list_soup.p is not None):
            lyrics1_list_soup = lyrics_list_soup.find('p').getText()
            if (lyrics1_list_soup == ""):
                lyrics1_list_soup = "no lyrics"
        else:
            lyrics1_list_soup = "no lyrics"

        Song_Name = soup.find('h1', attrs={'class': 'header_with_cover_art-primary_info-title'}).getText()
        artist_list_soup = soup.find('h2')
        Artist = artist_list_soup.find('a',
                                       attrs={'class': 'header_with_cover_art-primary_info-primary_artist'}).getText()
        Genre = "Pop"
        Lyrics = lyrics1_list_soup

        #         lyrics_data = [Song_Name, Artist, Genre, Lyrics]
        #         print(lyrics_data)

        df_pop2.loc[len(df_pop2)] = [Song_Name, Artist, Genre, Lyrics]
df_pop2

# In[11]:

frames = [df_pop, df_pop1, df_pop2]
result = pd.concat(frames)
result[:]

# In[12]:

result.to_csv('lyrics_pop_300.csv', sep=',')

# # Country

# In[18]:

# https://genius.com/api/songs/chart?page=1&per_page=10&tag_id=413&time_period=day
url1 = 'https://genius.com/api/songs/chart?page='
url2 = '&tag_id=413&time_period=day'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

df_country = pd.DataFrame(columns=['Song_Name', 'Artist', 'Genre', 'Lyrics'])

for x in range(1, 15):
    json_country = requests.get(url1 + str(x) + url2, headers=headers).content

    con = json.loads(json_country)

    #     for t in range(0,9):
    lyrics_List = con["response"]["chart_items"]

    for item in lyrics_List:

        url = item['item']['url']
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')

        lyrics_list_soup = soup.find('div', attrs={'class': 'lyrics'})

        if (lyrics_list_soup.p is not None):
            lyrics1_list_soup = lyrics_list_soup.find('p').getText()
            if (lyrics1_list_soup == ""):
                lyrics1_list_soup = "no lyrics"
        else:
            lyrics1_list_soup = "no lyrics"

        Song_Name = soup.find('h1', attrs={'class': 'header_with_cover_art-primary_info-title'}).getText()
        artist_list_soup = soup.find('h2')
        Artist = artist_list_soup.find('a',
                                       attrs={'class': 'header_with_cover_art-primary_info-primary_artist'}).getText()
        Genre = "country"
        Lyrics = lyrics1_list_soup

        lyrics_data = [Song_Name, Artist, Genre, Lyrics]
        #         print(lyrics_data)

        df_country.loc[len(df_country)] = [Song_Name, Artist, Genre, Lyrics]
df_country

# In[14]:

# https://genius.com/api/songs/chart?page=1&per_page=10&tag_id=413&time_period=all_time
url1 = 'https://genius.com/api/songs/chart?page='
url2 = '&per_page=10&tag_id=413&time_period=all_time'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

df_country1 = pd.DataFrame(columns=['Song_Name', 'Artist', 'Genre', 'Lyrics'])

for x in range(1, 11):
    json_country1 = requests.get(url1 + str(x) + url2, headers=headers).content

    con = json.loads(json_country1)

    #     for t in range(0,9):
    lyrics_List = con["response"]["chart_items"]

    for item in lyrics_List:

        url = item['item']['url']
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')

        lyrics_list_soup = soup.find('div', attrs={'class': 'lyrics'})

        if (lyrics_list_soup.p is not None):
            lyrics1_list_soup = lyrics_list_soup.find('p').getText()
            if (lyrics1_list_soup == ""):
                lyrics1_list_soup = "no lyrics"
        else:
            lyrics1_list_soup = "no lyrics"

        Song_Name = soup.find('h1', attrs={'class': 'header_with_cover_art-primary_info-title'}).getText()
        artist_list_soup = soup.find('h2')
        Artist = artist_list_soup.find('a',
                                       attrs={'class': 'header_with_cover_art-primary_info-primary_artist'}).getText()
        Genre = "country"
        Lyrics = lyrics1_list_soup

        lyrics_data = [Song_Name, Artist, Genre, Lyrics]
        #         print(lyrics_data)

        df_country1.loc[len(df_country1)] = [Song_Name, Artist, Genre, Lyrics]
df_country1

# In[19]:

# https://genius.com/api/songs/chart?page=1&per_page=10&tag_id=413&time_period=month
url1 = 'https://genius.com/api/songs/chart?page='
url2 = '&per_page=10&tag_id=413&time_period=month'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

df_country2 = pd.DataFrame(columns=['Song_Name', 'Artist', 'Genre', 'Lyrics'])

for x in range(1, 15):
    json_country2 = requests.get(url1 + str(x) + url2, headers=headers).content

    con = json.loads(json_country2)

    #     for t in range(0,9):
    lyrics_List = con["response"]["chart_items"]

    for item in lyrics_List:

        url = item['item']['url']
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')

        lyrics_list_soup = soup.find('div', attrs={'class': 'lyrics'})

        if (lyrics_list_soup.p is not None):
            lyrics1_list_soup = lyrics_list_soup.find('p').getText()
            if (lyrics1_list_soup == ""):
                lyrics1_list_soup = "no lyrics"
        else:
            lyrics1_list_soup = "no lyrics"

        Song_Name = soup.find('h1', attrs={'class': 'header_with_cover_art-primary_info-title'}).getText()
        artist_list_soup = soup.find('h2')
        Artist = artist_list_soup.find('a',
                                       attrs={'class': 'header_with_cover_art-primary_info-primary_artist'}).getText()
        Genre = "country"
        Lyrics = lyrics1_list_soup

        lyrics_data = [Song_Name, Artist, Genre, Lyrics]
        #         print(lyrics_data)

        df_country2.loc[len(df_country2)] = [Song_Name, Artist, Genre, Lyrics]
df_country2

# In[20]:

frames = [df_country, df_country1, df_country2]
result = pd.concat(frames)
result[:]

# In[22]:

result.to_csv('lyrics_country_299.csv')