from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import time
import pandas as pd
import requests
import bs4

# In[2]:


driver = webdriver.Firefox(executable_path=r"E:\geckodriver-v0.19.1-win64\geckodriver.exe")
driver.get("https://music.163.com")
time.sleep(5)

# In[3]:


song_list_bar = [t for t in driver.find_elements_by_tag_name("em") if t.text == "歌单"][0]

# In[4]:


song_list_bar.click()
time.sleep(5)

# In[5]:


# genre_selector = driver.find_element_by_id('g_top')
driver.switch_to_frame('g_iframe')

# In[6]:


genre_selector = driver.find_element_by_id('cateToggleLink')

# In[7]:


genre_selector.click()
time.sleep(5)

# In[8]:


Minyao_bar = [t for t in driver.find_elements_by_tag_name("a") if t.text == "民谣"][0]

# In[9]:


Minyao_bar.click()

# In[10]:


time.sleep(5)

# In[16]:


album_list = [t for t in driver.find_elements_by_tag_name('li') if len(t.text) > 5]
len(album_list)

# In[17]:


# for i in album_list:
album = album_list[0]
album.click()
time.sleep(5)
# print(i.text)


# In[23]:


song_list = driver.find_elements_by_tag_name('b')[2:]
print(len(song_list))
for i in song_list:
    print(i.text, "\n")

# In[27]:


driver.execute_script('window.scrollBy(0,800)')

# In[16]:


coordinate = "(0,800)"
driver.execute_script('window.scrollBy' + coordinate)
# driver.execute_script(js)
# ((JavascriptExecutor) driver).executeScript("window.scrollBy(0, 800)")


# In[28]:


driver.fullscreen_window()
time.sleep(5)
df_lyrics = pd.DataFrame(columns=['Song Name', 'Genre', 'Lyrics'])
lyrics_genre = "民谣"
lyrics_count = 0
for num in range(len(song_list)):
    print(num)
    if (num >= 6):
        driver.execute_script('window.scrollBy(0,800)')
    if (num >= 33):
        driver.execute_script('window.scrollBy(0,800)')
    if (num >= 60):
        driver.execute_script('window.scrollBy(0,800)')
    if (num >= 87):
        driver.execute_script('window.scrollBy(0,800)')
    if (num >= 114):
        driver.execute_script('window.scrollBy(0,800)')
    if (num >= 141):
        driver.execute_script('window.scrollBy(0,800)')
    if (num >= 168):
        driver.execute_script('window.scrollBy(0,800)')
    if (num >= 195):
        driver.execute_script('window.scrollBy(0,800)')

    song_list = driver.find_elements_by_tag_name('b')[2:]
    first_song_bar = song_list[num]
    first_song_bar.click()

    time.sleep(4)

    if ("纯音乐，无歌词" in driver.find_element_by_id('lyric-content').text or "暂时没有歌词" in driver.find_element_by_id(
            'lyric-content').text):
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
    song_data = [lyrics_name, lyrics_genre, lyrics]
    df_lyrics.loc[lyrics_count] = song_data
    lyrics_count = lyrics_count + 1
    #     time.sleep(2)
    driver.back()
    time.sleep(1)

# In[29]:


lyrics_count

# In[30]:


df_lyrics

# In[31]:


df_lyrics.to_csv('Chinese_Minyao_lyrics.csv', encoding='utf_8_sig', index=False)

# In[33]:


lyrics_data = pd.read_csv('Chinese_Minyao_lyrics.csv')

