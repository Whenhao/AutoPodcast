import os
from feedgen.feed import FeedGenerator

exampleArticlesList=[{'abstract':'Cracked Pots Lecture','authors':'J. Carberry','articleId':'1801.99999','title':'Pyschoceramics','url':'https://arxiv.org/abs/1801.99999'}]
exampleDirectory='public_files'
def generateRss(articlesList=exampleArticlesList,directoryPath='public_files',baseUrl='https://engn1931z29.pythonanywhere.com/rss'):

    CWF=os.path.split(os.getcwd())[1]
    if CWF!=directoryPath:
        os.chdir('/home/engn1931z29/mysite/'+directoryPath)
    Article=articlesList[0]
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.podcast.itunes_category('Technology', 'Podcasting')
    fg.logo("http://engn1931z29.pythonanywhere.com/serveFile/MV.jpg")
    fg.link( href=baseUrl, rel='alternate' )
    fg.description('This is a description.')
    fg.language('en')
    fg.contributor( name='Wenhao Li', email='wenhao_li@brown.edu' )
    fg.title('Arxiv news')

    for i in range(len(articlesList)):
        Article=articlesList[i]
        fe = fg.add_entry()
        fe.id('http://engn1931z29.pythonanywhere.com/serveFile/A'+str(i)+".mp3")
        fe.title(Article['title'])
        fe.description('Title: '+Article['title']+'  Abstract: '+Article['abstract'])
        fe.podcast.itunes_image('http://engn1931z29.pythonanywhere.com/serveFile/A'+str(i)+".jpg")
        fe.podcast.itunes_explicit('no')
        size=os.path.getsize('A'+str(i)+".mp3")
        fe.enclosure('http://engn1931z29.pythonanywhere.com/serveFile/A'+str(i)+".mp3", str(size), 'audio/mpeg')
    fg.rss_file('rss.xml')