# Following Example Adapted from following Medium.com article:
# https://medium.com/@antoinegrandiere/image-upload-and-moderation-with-python-and-flask-e7585f43828a

import os, json
from flask import Flask, render_template, request, Response, send_from_directory
from PIL import Image, ExifTags
import feedparser
import re
from gtts import gTTS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from feedgen.feed import FeedGenerator
#####################################################################################################################################
app = Flask(__name__)
baseurl='https://script.google.com/macros/s/AKfycby52onY9OX3abTGB9D3pPxm90a0qdEU13nSyC2iPisSbE_XCV0/exec?'
url='https://arxiv.org/rss/physics.optics'
exampleArticlesList=[{'abstract':'Cracked Pots Lecture','authors':'J. Carberry','articleId':'1801.99999','title':'Pyschoceramics','url':'https://arxiv.org/abs/1801.99999'}]
exampleDirectory='public_files'
# filename='A0.jpg'
def parseRss(url='https://arxiv.org/rss/physics.optics'):

    res=feedparser.parse(url)
    articlesList=[]
    for i in range(5):
        entries1=res['entries'][i]
        cleantitle=re.sub('_','',re.sub('$','',re.sub('\([A-Za-z0-9 .:\-\[\]]+\)','',entries1['title'])))
        cleanabstract=re.sub('_','',re.sub('$','',re.sub('\\n',' ',entries1['summary'][3:-5])))
        Articlesum={'abstract':cleanabstract,'articleId':re.findall('/([0-9.]+)',entries1['id'])[0],'authors':(", ").join(re.findall('>([A-Za-z .]+)</a>',entries1['author'])),'title':cleantitle,'url':entries1['link']}
        articlesList.append(Articlesum)
    return articlesList


def createAudioFiles(articlesList=exampleArticlesList, directoryPath=exampleDirectory):

    CWF=os.path.split(os.getcwd())[1]
    if CWF!=directoryPath:
        os.chdir('/home/engn1931z29/mysite/'+directoryPath)

    for i in range(len(articlesList)):
        Article=articlesList[i]
        tts = gTTS(text='title, '+Article['title']+'. Abstract, '+Article['abstract'], lang='en', slow=False)
        tts.save('A'+str(i)+".mp3")


def createWordCloudImages(articlesList=exampleArticlesList, directoryPath=exampleDirectory):

    CWF=os.path.split(os.getcwd())[1]
    if CWF!=directoryPath:
        os.chdir('/home/engn1931z29/mysite/'+directoryPath)
    for i in range(len(articlesList)):
        Article=articlesList[i]
        wordcloud = WordCloud(max_font_size=40).generate(Article['abstract'])
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.savefig('A'+str(i)+".jpg")


def generateRss(articlesList=exampleArticlesList,directoryPath='public_files',baseUrl='https://engn1931z29.pythonanywhere.com/'):

    CWF=os.path.split(os.getcwd())[1]
    if CWF!=directoryPath:
        os.chdir('/home/engn1931z29/mysite/'+directoryPath)
    Article=articlesList[0]
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.podcast.itunes_category('Technology', 'Podcasting')
    fg.logo("http://engn1931z29.pythonanywhere.com/serveFile/A0.jpg")
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
        fe.enclosure('http://engn1931z29.pythonanywhere.com/serveFile/A'+str(i)+".mp3", 0, 'audio/mpeg')
    fg.rss_file('rss.xml')


def updates():
    articlesList=parseRss(baseurl+url)
    createAudioFiles(articlesList, exampleDirectory)
    createWordCloudImages(articlesList, exampleDirectory)


@app.route('/serveFile/<path:filename>', methods=['GET'])
def serveFile(filename):

    extent=re.findall('\.([A-Za-z0-9]+)',filename)[-1]
    if extent=='mp3':
        mime='audio/mpeg'
    elif extent=='jpg':
        mime='image/jpeg'
    else:
        mime='text/xml'

    return send_from_directory('/home/engn1931z29/mysite/public_files/', filename, mimetype=mime)
    # return send_from_directory('/home/engn1931z29/mysite/public_files/',name,mimetype='text/plain')#,as_attachment=True
    # return Response('Done',mimetype='text/plain')


@app.route('/rss')
def serveRss():
    # articlesList=parseRss(baseurl+url)
    # createAudioFiles(articlesList, exampleDirectory)
    # createWordCloudImages(articlesList, exampleDirectory)
    # generateRss(articlesList,'public_files','https://engn1931z29.pythonanywhere.com/')
    # return Response('Done',mimetype='text/plain')
    return send_from_directory('/home/engn1931z29/mysite/public_files','rss.xml')


####################################################################################################################################
