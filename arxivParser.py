import feedparser
import re
# from bs4 import BeautifulSoup

def parseRss(url='https://arxiv.org/rss/physics.optics'):

  """ RSS Feed URL -> list of dictionaries for first five articles

  This function returns a list of dictionaries with the keys 'abstract', 'articleId', 'authors', 'title', and 'url'
  for the first five articles on the specified arXiv RSS Feed url.

  The values for each of the five keys must be strings.

  The string for the authors key should parse the list of authors received from the feed into one single string.

  The default argument url='https://arxiv.org/rss/physics.optics' shows an example of the expected input.
  """

  #YOUR CODE HERE: programmatically producing the articleList of dictionaries described above
  res=feedparser.parse(url)
  articlesList=[]
  for i in range(5):
      entries1=res['entries'][i]
      cleantitle=re.sub('_','',re.sub('$','',re.sub('\([A-Za-z0-9 .:\-\[\]]+\)','',entries1['title'])))
      cleanabstract=re.sub('_','',re.sub('$','',re.sub('\\n',' ',entries1['summary'][3:-5])))
      Articlesum={'abstract':cleanabstract,'articleId':re.findall('/([0-9.]+)',entries1['id'])[0],'authors':(", ").join(re.findall('>([A-Za-z .]+)</a>',entries1['author'])),'title':cleantitle,'url':entries1['link']}
      articlesList.append(Articlesum)
  return articlesList


# url='https://arxiv.org/rss/physics.optics'
# res=feedparser.parse(url)
# res.keys()
# len(res['entries'])
# entries1=res['entries'][2]
# entries1.keys()
# entries1['author']
# (", ").join(re.findall('>([A-Za-z .]+)</a>',entries1['author']))
# entries1['id']
# re.findall('/([0-9.]+)',entries1['id'])
#
# entries1['link']
#
# entries1['title']
# re.sub('\([A-Za-z0-9 .:\-\[\]]+\)','',entries1['title'])
#
# re.sub('\\n',' ',entries1['summary'][3:-5])
#
# Articlesum={'abstract':re.sub('\\n',' ',entries1['summary'][3:-5]),'articleId':re.findall('/([0-9.]+)',entries1['id'])[0],'authors':(", ").join(re.findall('>([A-Za-z .]+)</a>',entries1['author'])),'title':re.sub('\([A-Za-z0-9 .:\-\[\]]+\)','',entries1['title']),'url':entries1['link']}
# Articlesum
