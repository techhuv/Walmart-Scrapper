#!/usr/bin/env python
# coding: utf-8

# In[1]:


#system libraries
import os
import random
import time

#selenium libraries
from datetime import date
import pyautogui
import webbrowser


# In[2]:


path = os.getcwd()


# In[196]:


# var chromeOptions = new ChromeOptions();
# chromeOptions.AddUserProfilePreference("download.default_directory", "Your_Path");
# chromeOptions.AddUserProfilePreference("intl.accept_languages", "nl");
# chromeOptions.AddUserProfilePreference("disable-popup-blocking", "true");
# var driver = new ChromeDriver("Driver_Path", chromeOptions);


# In[38]:


import pyautogui
import asyncio
import random

head = 'https://www.walmart.com/search/?cat_id=1085666&grid=true&page='
tail='&query='

def save(i):
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.typewrite(r'C:\Users\STARK\Desktop\Harshit\Web site projects\Walmart Scrapper\DownData\Beauty'+str(i)+ '.html')
    
#     pyautogui.typewrite(r'C:\Users\STARK\Desktop')
#     pyautogui.typewrite(r'\Harshit\Web site projects\Walmart Scrapper')
#     pyautogui.typewrite(r'\DownData\Beauty'+str(i)+ '.html')
    time.sleep(2)
    pyautogui.hotkey('alt','s')
    time.sleep(1)
    
def load(url,i):
    webbrowser.open_new_tab(url)
    time.sleep(9)
    return i


try:
    #create chrome driver
    #driver = webdrivC:\Users\visha\Desktop\Harshit\Web site projects\NSE Freelancing Project\24-Dec-2017.ziper.Chrome(ChromeDriverManager().install())
    # for i in range(1,26):
    #     save(load(head+str(i)+tail,i))
              
except:
    print("[-] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")


# In[3]:


from selenium import webdriver
import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup, NavigableString, Tag


# In[4]:


with open(r'C:\Users\STARK\Desktop\Harshit\Web site projects\Walmart Scrapper\DownData\Beauty1.html', 'r',encoding='utf8') as f:
    contents = f.read()
    soup = BeautifulSoup(contents)


# In[5]:


temp = soup.find('div',attrs = {'class':'search-product-result'})


# In[6]:


temp = temp.findAll('div',attrs = {'class':'search-result-gridview-item clearfix arrange-fill'})


# In[7]:


# temp[0]


# In[ ]:





# In[8]:


name=print(temp[0].find('a',attrs = {'class':'product-title-link line-clamp line-clamp-2 truncate-title'}).text)



# In[9]:


price=temp[6].find('span',attrs = {'class':'price display-inline-block arrange-fit price price-main'}).text
price = price[:len(price) // 2]


# # Image Link

# In[10]:


image = temp[0].find('img')['data-image-src']
print(image)


# # Image from Local File System

# In[11]:


image = temp[0].find('img')['src']
print(image)


# In[12]:


pnames=[]
pprices=[]
pimages=[]


# In[13]:


for i in range(0,len(temp)):
    
    name=temp[i].find('a',attrs = {'class':'product-title-link line-clamp line-clamp-2 truncate-title'}).text
    pnames.append(name)
    
    if temp[i].find('span',attrs = {'class':'price price-range'}):
        price=temp[i].find('span',attrs = {'class':'price price-range'}).text
        price_temp=price.split(' - ')
        a=price_temp[0][:len(price_temp[0]) // 2]
        b=price_temp[1][:len(price_temp[1]) // 2]
        price=a+'-'+b
    else:
        price=temp[i].find('span',attrs = {'class':'price display-inline-block arrange-fit price price-main'}).text
        price = price[:len(price) // 2]
        
    pprices.append(price)
    image = temp[i].find('img')['data-image-src']
    pimages.append(image)
    
#     print(i,price)


# In[14]:


pprices


# In[15]:


import pandas as pd
df=pd.DataFrame()
df['Product Name']=pnames
df['Price']=pprices
df['Link']=pimages


# In[22]:


print(df)


# In[ ]:




