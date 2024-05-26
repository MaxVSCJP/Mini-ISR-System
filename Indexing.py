import os
import json
import Tokenization as token
import Stopword as SR
import stmmer as stem
import Normalizer as normal


directoryCorpus = os.getcwd() + "\\Corpus"

def Indexing():
    global directoryCorpus
    diction_dict = {}
    directoryCorpus = os.getcwd() + "\\Corpus"
    corpus = os.listdir(directoryCorpus)


    for file in corpus:
        with open(directoryCorpus + "\\" + file, "r",encoding= "utf-8") as f:
            diction_dict[file] = SR.SWRLower(normal.charnorm(stem.geez_stemmer(SR.SWRUpper(token.Tokenization(f)))))
            

    with open ("Inverted file.txt", "w") as IFile:
        json.dump(diction_dict, IFile)

    IFile.close()

def showRankedBarChart():
    print("Hello showRandedBarchart")
    token.RankedBarChart()
