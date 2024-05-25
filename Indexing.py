import Tokenization as token
import stmmer as stem
import os
import json

directoryCorpus = ""

def Indexing():
    global directoryCorpus
    # Read the file
    diction_dict = {}
    directoryCorpus = os.getcwd() + "\\Corpus"
    corpus = os.listdir(directoryCorpus)


    for file in corpus:
        with open(directoryCorpus + "\\" + file, "r",encoding= "utf-8") as f:
            diction_dict[file] = stem.geez_stemmer((token.Tokenization(f)))
            

    with open ("Inverted file.txt", "w") as IFile:
        json.dump(diction_dict, IFile)

    IFile.close()

def showRankedBarChart():
    token.RankedBarChart()

Indexing()
