import Assign as assign
import os

diction_list = []

directoryCorpus = os.getcwd() + "\\Corpus"
corpus = os.listdir(directoryCorpus)

for file in corpus:
    with open(directoryCorpus + "\\" + file, "r",encoding= "utf-8") as f:
        diction_list.append(assign.Tokenization(f))
        
assign.RankedBarChart()