
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import numpy as np
import time
import requests
import bs4


# In[62]:


raplistURL = [
    "https://www.billboard.com/charts/rap-song/2016-06-24",
    "https://www.billboard.com/charts/rap-song/2016-01-24",
    "https://www.billboard.com/charts/rap-song/2017-01-24",
    "https://www.billboard.com/charts/rap-song/2018-01-24"
]

rocklistURL = [
    "https://www.billboard.com/charts/rock-songs/2016-03-24",
    "https://www.billboard.com/charts/rock-songs/2017-03-24"
]


# In[69]:


Song_Names = []
Artist_Names = []


# In[2]:


def pageQuery(URL_List, numberPerPage):
    driver = webdriver.Chrome(executable_path='./chromedriver')
    time.sleep(3)
    for each in URL_List:
        n=1
        driver.get(each)
        time.sleep(5)
        print(each)
        while (n<=numberPerPage):
            try:
                element = (driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/article['+str(n)+']'))
            except:
                element = (driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/article['+str(n)+']'))
            Artist_Names.append(element.find_element_by_class_name("chart-row__artist").text)
            Song_Names.append(element.find_element_by_class_name("chart-row__song").text)
            n+=1
        print("done "+each)
#Song titles either are not being added to the list or they throw an error so I can't just use if statements.
#In TryExcept It doesn't seem like I can store variables.


# In[66]:


pageQuery(raplistURL, 25)


# In[70]:


pageQuery(rocklistURL, 50)


# In[71]:


RockArtists = Artist_Names


# In[72]:


RockSongs = Song_Names


# In[67]:


RapArtists = Artist_Names


# In[68]:


RapSongs = Song_Names


# In[73]:


rapdata = {'Song': RapSongs, 'Artist': RapArtists, 'Lyrics': songLyrics}


# In[74]:


rockdata = {'Song': RockSongs, 'Artist': RockArtists}


# In[61]:


rapDf = pd.DataFrame(data = rapData)
rockDf = pd.DataFrame(data = rockData)


# In[75]:


df1


# In[65]:


df.to_csv("rap.csv")


# In[76]:


df1.to_csv("rock.csv")


# In[131]:


songLyrics = []


# In[132]:


def getSongLyrics(songName, songURL):
    driver = webdriver.Chrome(executable_path='/Users/Brennan/Desktop/Classes/BIA-660/RocknRapScraping/chromedriver')
    time.sleep(3)
    driver.get(songURL)
    time.sleep(5)
    lyricList = []
    
    element = driver.find_element_by_class_name('lyrics')
    element.find_element_by_tag_name('p')
    
    lyrics = element.find_elements_by_tag_name('a')
    for line in lyrics:
        lyricList.append(line.text)
    songLyrics.append(lyricList)
    
    


# In[133]:


def songURL(artist, song):
    baseURL = "https://genius.com/"
    artist = artist.replace(" ","-")
    artist = artist.replace("&","and")
    artist = artist.replace("'","")
    artist = artist.replace("!","")
    artist = artist.replace(".","")
    artist = artist.replace(":", "")
    artist = artist.replace(",", "")
    artist = artist.replace("!", "")
    artist = artist.replace("-Featuring-Drake", "")
    artist = artist.replace("-Featuring-Kiiara", "")
    artist = artist.replace("-Featuring-The-Weeknd","")
    artist = artist.replace("Fat-Joe-Remy-Ma-and-Jay-Z-Featuring-French-Montana-and-Infared","Fat-joe-and-remy-ma")
    artist = artist.replace("G-Eazy-x-Bebe-Rexha","G-eazy")
    artist = artist.replace("-Featuring-Rihanna","")
    artist = artist.replace("BORNS","brns")
    artist = artist.replace("Lil-Wayne-Wiz-Khalifa-and-Imagine-Dragons-With-Logic-and-Ty-Dolla-$ign-Feat-X-Ambassadors","Atlantic-records")
    artist = artist.replace("-Featuring-Young-Dolph","")
    artist = artist.replace("-Featuring-The-Throne","")
    artist = artist.replace("-Featuring-Enrique-Iglesias","")
    artist = artist.replace("-Featuring-Future","")
    artist = artist.replace("-Featuring-E-40","")
    artist = artist.replace("-Featuring-Remy-Boyz","")
    artist = artist.replace("-Featuring-Nicki-Minaj","")
    artist = artist.replace("-Featuring-Big-Sean","")
    artist = artist.replace("-Featuring-Pharrell-Williams","")
    artist = artist.replace("-Featuring-Fetty-Wap-and-Rich-Homie-Quan","")
    artist = artist.replace("-and-DeJ-Loaf","")
    artist = artist.replace("-Featuring-TI-Young-Dolph-and-Ricco-Barrino","")
    artist = artist.replace("-Featuring-Lil-Uzi-Vert","")
    artist = artist.replace("-Featuring-Gucci-Mane","")
    artist = artist.replace("-x-Camila-Cabello","")
    artist = artist.replace("-and-Zayion-McCall","")
    artist = artist.replace("-Featuring-Future","")
    artist = artist.replace("-$tone-Featuring-J-Davi$-and-Spooks","-Stone")
    artist = artist.replace("-Featuring-Lil-Yachty","")
    artist = artist.replace("-Featuring-Future-and-Lil-Uzi-Vert","")
    artist = artist.replace("-Featuring-Nicki-Minaj-Chris-Brown-August-Alsina-Jeremih-Future-and-Rick-Ross","")
    artist = artist.replace("-Featuring-A$AP-Rocky","")
    artist = artist.replace("-Chris-Brown-August-Alsina-Jeremih-Future-and-Rick-Ross","")
    artist = artist.replace("-Featuring-21-Savage","")
    artist = artist.replace("-Featuring-Nicki-Minaj-Chris-Brown-August-Alsina-Jeremih-Future-and-Rick-Ross","")
    artist = artist.replace("-and-Lil-Uzi-Vert","")
    artist = artist.replace("-Featuring-Lil-Wayne","")
    artist = artist.replace("-and-Cardi-B","")
    artist = artist.replace("-and-2-Chainz","")
    artist = artist.replace("-Nicki-Minaj","")
    artist = artist.replace("-Featuring-XXXTENTACION","")
    artist = artist.replace("-Featuring-Migos","")
    artist = artist.replace("-Featuring-Zacari","")
    artist = artist.replace("-Featuring-Ed-Sheeran","")
    artist = artist.replace("-Featuring-Yo-Gotti-A-Boogie-Wit-da-Hoodie-and-Kodak-Black","")
    artist = artist.replace("-Featuring-Ed-Sheeran","")
    artist = artist.replace("-Featuring-Kesha","")
    artist = artist.replace("*","")
    artist = artist.replace("A$AP-Ferg","A-ap-ferg")
    artist = artist.replace("-Featuring-Landon-Cube","")
    
  
    song = song.replace("-pt-1","")
    song = song.replace("&","and")
    song = song.replace(" ","-")
    song = song.replace("'","")
    song = song.replace(",","")
    song = song.replace("(","")
    song = song.replace(")","")
    song = song.replace("!","")
    song = song.replace(".","")
    song = song.replace("$ave-Dat","ave-dat")
    print(baseURL+artist+"-"+song+"-lyrics")
    return baseURL+artist+"-"+song+"-lyrics"


# In[134]:


def geniusQuery(songList, artistList):
    n=0
    for each in songList:
        getSongLyrics(each,songURL(artistList[n], each))
        n+=1
        


# In[123]:


geniusQuery(RapSongs, RapArtists)


# In[135]:


geniusQuery(RockSongs, RockArtists)


# In[124]:


rapdata = {'Song': RapSongs, 'Artist': RapArtists, 'Lyrics': songLyrics}
rapDf = pd.DataFrame(data = rapdata)


# In[126]:


rapDf.to_csv("rapLyrics.csv")

rockdata = {'Song': RockSongs, 'Artist': RockArtists, 'Lyrics': songLyrics}

# In[137]:


rockDf = pd.DataFrame(data = rockdata)


# In[138]:


rockDf


# In[139]:


rockDf.to_csv("rockLyrics.csv")


# # Scraping Chinese Lyrics Part 1
# 

# In[ ]:


driver = webdriver.Firefox(executable_path=r"E:\geckodriver-v0.19.1-win64\geckodriver.exe")
driver.get("https://music.163.com")
time.sleep(5)


# In[ ]:


song_list_bar = [t for t in driver.find_elements_by_tag_name("em") if t.text == "歌单"][0]


# In[ ]:


song_list_bar.click()
time.sleep(5)


# In[3]:


# genre_selector = driver.find_element_by_id('g_top')
driver.switch_to_frame('g_iframe')


# In[ ]:


genre_selector = driver.find_element_by_id('cateToggleLink')


# In[ ]:


genre_selector.click()
time.sleep(5)


# In[ ]:


Gufeng_bar = [t for t in driver.find_elements_by_tag_name("a") if t.text == "古风"][0]


# In[ ]:


Gufeng_bar.click()

time.sleep(5)


# In[ ]:


album_list = [t for t in driver.find_elements_by_tag_name('li') if len(t.text) > 5]
len(album_list)


# In[ ]:



album = album_list[5]
album.click()
time.sleep(5)
# print(i.text)


# In[ ]:


song_list = driver.find_elements_by_tag_name('b')[3:]
print(len(song_list))
for i in song_list:
    print(i.text,"\n")


# In[ ]:


EC.visibility_of_element_located(song_list[13])


# In[ ]:


coordinate = "(0,800)"
driver.execute_script('window.scrollBy'+coordinate)


# In[ ]:


driver.fullscreen_window()
time.sleep(5)
df_lyrics = pd.DataFrame(columns= ['Song Name', 'Genre', 'Lyrics'])
lyrics_genre = "古风"
lyrics_count = 0
for num in range(len(song_list)):
    print(num)
    if(num >= 11):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 38):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 64):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 91):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 118):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 144):
        driver.execute_script('window.scrollBy(0,800)')
    song_list = driver.find_elements_by_tag_name('b')[3:]
    first_song_bar = song_list[num]
    first_song_bar.click()
    
    time.sleep(2)
    
    if("纯音乐，无歌词" in driver.find_element_by_id('lyric-content').text or "暂时没有歌词" in driver.find_element_by_id('lyric-content').text  ):
        driver.back()
        time.sleep(2)
        continue
    
    for t in driver.find_elements_by_tag_name("a"):
        if "展开" in t.text:
            unfold_bar = t
            unfold_bar.click() 

    
    time.sleep(1)
    lyrics = driver.find_element_by_id('lyric-content').text
    lyrics_name = driver.find_element_by_class_name('tit').text
    song_data = [lyrics_name,lyrics_genre,lyrics]
    df_lyrics.loc[lyrics_count]=song_data
    lyrics_count = lyrics_count+1
#     time.sleep(2)
    driver.back()
    time.sleep(1)


# In[ ]:


lyrics_count


# In[ ]:


df_lyrics


# In[ ]:


df_lyrics.to_csv('Chinese_Gufeng_lyrics.csv', encoding='utf_8_sig', index=False)


# In[ ]:


lyrics_data = pd.read_csv('Chinese_Gufeng_lyrics.csv')


# In[ ]:


lyrics_data


# In[ ]:


driver.back()
time.sleep(2)
album_list = [t for t in driver.find_elements_by_tag_name('li') if len(t.text) > 5]

album = album_list[8]
album.click()
time.sleep(5)
len(album_list)


# In[ ]:


print(lyrics_count)
song_list = driver.find_elements_by_tag_name('b')[2:]
print(len(song_list),lyrics_count)
for i in song_list:
    print(i.text,"\n")


# In[ ]:


for num in range(len(song_list)):
    print(num)
    print(lyrics_count)
    if(num >= 7):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 35):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 61):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 88):
        driver.execute_script('window.scrollBy(0,800)')
#     if(num >= 117):
#         driver.execute_script('window.scrollBy(0,800)')
#     if(num >= 144):
#         driver.execute_script('window.scrollBy(0,800)')
    song_list = driver.find_elements_by_tag_name('b')[3:]
    first_song_bar = song_list[num]
    first_song_bar.click()
    
    time.sleep(4)
    
    if("纯音乐，无歌词" in driver.find_element_by_id('lyric-content').text or "暂时没有歌词" in driver.find_element_by_id('lyric-content').text  ):
        driver.back()
        time.sleep(2)
        continue
    
    for t in driver.find_elements_by_tag_name("a"):
        if "展开" in t.text:
            unfold_bar = t
            unfold_bar.click() 

    
    time.sleep(1)
    lyrics = driver.find_element_by_id('lyric-content').text
    lyrics_name = driver.find_element_by_class_name('tit').text
    song_data = [lyrics_name,lyrics_genre,lyrics]
    df_lyrics.loc[num+148]=song_data
    lyrics_count = lyrics_count+1
#     time.sleep(2)
    driver.back()
    time.sleep(1)
    if lyrics_count==200:
        break
    


# In[ ]:


df_lyrics


# In[ ]:


df_lyrics.to_csv('Chinese_Gufeng_lyrics_1.csv', encoding='utf_8_sig', index=False)


# In[ ]:


lyrics_data = pd.read_csv('Chinese_Gufeng_lyrics_1.csv')


# In[ ]:


lyrics_data


# # Scraping Chinese Lyrics Part 2

# In[ ]:


driver = webdriver.Firefox(executable_path=r"E:\geckodriver-v0.19.1-win64\geckodriver.exe")
driver.get("https://music.163.com")
time.sleep(5)


# In[ ]:


song_list_bar = [t for t in driver.find_elements_by_tag_name("em") if t.text == "歌单"][0]


# In[ ]:


song_list_bar.click()
time.sleep(5)


# In[ ]:


# genre_selector = driver.find_element_by_id('g_top')
driver.switch_to_frame('g_iframe')


# In[ ]:


genre_selector = driver.find_element_by_id('cateToggleLink')


# In[ ]:


genre_selector.click()
time.sleep(5)


# In[ ]:


Minyao_bar = [t for t in driver.find_elements_by_tag_name("a") if t.text == "民谣"][0]


# In[ ]:


Minyao_bar.click()


# In[ ]:


time.sleep(5)


# In[ ]:


album_list = [t for t in driver.find_elements_by_tag_name('li') if len(t.text) > 5]
len(album_list)


# In[ ]:


album = album_list[0]
album.click()
time.sleep(5)


# In[ ]:


song_list = driver.find_elements_by_tag_name('b')[2:]
print(len(song_list))
for i in song_list:
    print(i.text,"\n")


# In[ ]:


driver.execute_script('window.scrollBy(0,800)')


# In[ ]:


coordinate = "(0,800)"
driver.execute_script('window.scrollBy'+coordinate)


# In[ ]:


driver.fullscreen_window()
time.sleep(5)
df_lyrics = pd.DataFrame(columns= ['Song Name', 'Genre', 'Lyrics'])
lyrics_genre = "民谣"
lyrics_count = 0
for num in range(len(song_list)):
    print(num)
    if(num >= 6):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 33):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 60):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 87):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 114):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 141):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 168):
        driver.execute_script('window.scrollBy(0,800)')
    if(num >= 195):
        driver.execute_script('window.scrollBy(0,800)')
        
    song_list = driver.find_elements_by_tag_name('b')[2:]
    first_song_bar = song_list[num]
    first_song_bar.click()
    
    time.sleep(4)
    
    if("纯音乐，无歌词" in driver.find_element_by_id('lyric-content').text or "暂时没有歌词" in driver.find_element_by_id('lyric-content').text  ):
        driver.back()
        time.sleep(2)
        continue
    
    for t in driver.find_elements_by_tag_name("a"):
        if "展开" in t.text:
            unfold_bar = t
            unfold_bar.click() 

    
    time.sleep(1)
    lyrics = driver.find_element_by_id('lyric-content').text
    lyrics_name = driver.find_element_by_class_name('tit').text
    song_data = [lyrics_name,lyrics_genre,lyrics]
    df_lyrics.loc[lyrics_count]=song_data
    lyrics_count = lyrics_count+1
#     time.sleep(2)
    driver.back()
    time.sleep(1)


# In[ ]:


lyrics_count


# In[ ]:


df_lyrics


# In[ ]:


df_lyrics.to_csv('Chinese_Minyao_lyrics.csv', encoding='utf_8_sig', index=False)


# In[ ]:


lyrics_data = pd.read_csv('Chinese_Minyao_lyrics.csv')

