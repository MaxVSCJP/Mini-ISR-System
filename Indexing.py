import Tokenization as token
import os

diction_list = []

directoryCorpus = os.getcwd() + "\\Corpus"
corpus = os.listdir(directoryCorpus)

for file in corpus:
    with open(directoryCorpus + "\\" + file, "r",encoding= "utf-8") as f:
        diction_list.append(token.Tokenization(f))
        
token.RankedBarChart()