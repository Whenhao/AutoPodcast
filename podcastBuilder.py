#!/usr/bin/python3.6

from arxivParser import parseRss
from textToAudioVisual import createAudioFiles, createWordCloudImages
from arxivFeedgen import generateRss

# you can take care of the rest...
baseurl='https://script.google.com/macros/s/AKfycby52onY9OX3abTGB9D3pPxm90a0qdEU13nSyC2iPisSbE_XCV0/exec?'
url='https://arxiv.org/rss/physics.optics'
Directory='public_files'
articlesList=parseRss(baseurl+url)
createAudioFiles(articlesList, Directory)
createWordCloudImages(articlesList, Directory)
generateRss(articlesList,'public_files','https://engn1931z29.pythonanywhere.com/serveRss')