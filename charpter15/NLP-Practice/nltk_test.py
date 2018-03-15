import urllib.request
import nltk
response = urllib.request.urlopen(u'http://php.net')
html = response.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html5lib")
#这里需要安装html5lib模块
text = soup.get_text(strip=True)
tokens = text.split()
freq = nltk.FreqDist(tokens)
from nltk.corpus import stopwords
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if not token in sr:
        clean_tokens.append(token)
freq = nltk.FreqDist(clean_tokens)
for key ,val in freq.items():
    print(str(key)+':'+str(val))
freq.plot(20,cumulative = False)
