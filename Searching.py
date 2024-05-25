import json
import Tokenization as token
import math

diction_dicts = json.load(open("Inverted File.txt"))
rankedSearch = []

def Search(query, diction_dict: dict[str, dict[str, int]]):
    numerator = 0
    denomDoc = 0
    denomQuery = 0
    searchedDocument = {}
    with open("Query.txt", "w", encoding="UTF-8") as queryFile:
        queryFile.write(query)
        queryFile.close()

    with open("Query.txt", "r", encoding="UTF-8") as queryFile:
        query_dict = token.Tokenization(queryFile)
    
    for document, termDict in diction_dict.items():
        
        for term, tf in termDict.items():
            if term in query_dict.keys():
                numerator += query_dict[term] * tf
                denomDoc += tf * tf
                denomQuery += query_dict[term] * query_dict[term]
        try:
            similarity = numerator/math.sqrt(denomDoc * denomQuery)
        except ZeroDivisionError:
            similarity = 0
            
        print(document,similarity)
        searchedDocument[document] = similarity
        numerator = 0
        denomDoc = 0
        denomQuery = 0
    return searchedDocument


def RankedDocument(searchQuery):
    global rankedSearch
    rankedSearch_dict = dict(sorted(Search(searchQuery, diction_dicts).items(), key=lambda item: item[1],reverse= True))
    rankedSearch = list(rankedSearch_dict.keys())
    return rankedSearch_dict.keys()



def QueryFromGUI(query):
    print(query)
    print(RankedDocument(query))

