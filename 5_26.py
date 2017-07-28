
# coding: utf-8

# In[4]:

# http://flupy.org/data/flags/<code>/<code>.gif
CNTRY_CD ="BD BR CD CN DE EG ET FR ID IN IR JP KR MX NG PH PK RU TR US VN"
from urllib.request import urlopen
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def get_country_image(code):
#for code in CNTRY_CD.lower().split():
    url = f'http://flupy.org/data/flags/{code}/{code}.gif'
    with open(f'{code}.gif', 'wb') as f, urlopen(url) as u:
            f.write(u.read())
            print(f'{code} is processed.')
            
def multi_get_country_image(lst, option=None):
    if option == 'Thread':
        pool = ThreadPoolExecutor(max_workers=4)
        map_choosed = pool.map
    elif option == 'Process':
        pool = ProcessPoolExecutor(max_workers=4)
        map_choosed = pool.map
    else:
        map_choosed = map
        
begin = time.time()

#list(map_choosed(get_country_image, n))
multi_get_country_image(CNTRY_CD.lower().split(),option='Process')

print(time.time() - begin)


# In[ ]:

def word_combination():
    """단어조합 컴비네이션
    wc =word_combination()
    wc('한글','이름','테스트')
    


# In[ ]:



