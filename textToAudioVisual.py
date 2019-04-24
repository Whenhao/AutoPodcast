import os
from gtts import gTTS
from wordcloud import WordCloud
import matplotlib.pyplot as plt

exampleArticlesList=[{'abstract':'Cracked Pots Lecture','authors':'J. Carberry','articleId':'1801.99999','title':'Pyschoceramics','url':'https://arxiv.org/abs/1801.99999'}]
exampleDirectory='public_files'
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

# createWordCloudImages()
# createAudioFiles()
# os.getcwd()
# os.path.split(os.getcwd())[1]
# createAudioFiles()
# Article['abstract']
# wordcloud = WordCloud(max_font_size=40).generate(Article['abstract'])
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.savefig('A_'+str(1)+".jpeg")
# plt.show()
