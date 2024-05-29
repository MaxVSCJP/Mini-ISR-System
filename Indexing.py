import os
import json
import Tokenization as token
import Stopword as SR
import stmmer as stem
import Normalizer as normal


directoryCorpus = os.getcwd() + "\\Corpus"
corpus = os.listdir(directoryCorpus)
def Indexing():
    global directoryCorpus
    global corpus
    diction_dict = {}
    directoryCorpus = os.getcwd() + "\\Corpus"
    corpus = os.listdir(directoryCorpus)

    for file in corpus:
        with open(directoryCorpus + "\\" + file, "r",encoding= "utf-8") as f:
            diction_dict[file] = SR.SWRLower(normal.charnorm(stem.geez_stemmer(SR.SWRUpper(token.Tokenization(f)))))
            

    with open ("Inverted file.txt", "w") as IFile:
        json.dump(diction_dict, IFile)

    IFile.close()
    indexNum = 0
    for value in diction_dict.values():
        indexNum += len(value)
    print(indexNum)
    f.close()

def showRankedBarChart():
    token.word_dic_global = {}
    for file in corpus:
        with open(directoryCorpus + "\\" + file, "r",encoding= "utf-8") as f:
            token.Tokenization(f)
    print("Hello showRankedBarchart")
    token.RankedBarChart()
    