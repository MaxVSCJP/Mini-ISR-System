import matplotlib.pyplot as plt
from matplotlib import font_manager


word_dic = {}
PUNC = {"።","፤","።","."}
num = {"፪","፫","፬","፭","ዕፀ","፮","፯","፰","፱","",".","?",":","1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n", "\t"}
sorted_dict_values = {}


def Tokenization(f):
    global sorted_dict_values
    for line in f:
        words = line.lower().split(" ")
        for word in words:
            word = word.replace("\n", "").replace("\t", "")
            if word not in num:
                if word:
                    if word[-1] not in PUNC:
                        if word  in word_dic:
                            word_dic[word] += 1
                        else:
                            word_dic[word] = 1
                    else:
                        if word  in word_dic:
                            word_dic[word[:-1]] += 1
                        else:
                            word_dic[word[:-1]] = 1

    sorted_dict_values = dict(sorted(word_dic.items(), key=lambda item: item[1],reverse= True))
    return sorted_dict_values

def RankedBarChart():

    # Sets a custom font because the default font doesn't show Ethiopic characters
    custom_font_entry = font_manager.FontEntry(fname="C:\\Windows\\Fonts\\nyala.ttf", name='CustomFont')
    font_manager.fontManager.ttflist.insert(0, custom_font_entry)
    plt.rcParams['font.family'] = 'CustomFont'

    # Creating the lists that will be the x and y axes of out graph
    word_rank  = []               
    word_rank = list(range(1, len(sorted_dict_values) + 1))

    frequency = list(sorted_dict_values.values())

    N = len(word_rank)
    print("Total Number of Tokens", N)

    # shortening the list becasue the graph would be anomalous if it was too long
    wordRankMini = []
    for i in range(1000):
        wordRankMini.append(word_rank[i])

    frequencyMini = []
    for i in range(1000):
        frequencyMini.append(frequency[i])

    # calculating the constant C for each word 
    print("\n\n")
    for i in range(20000):
        print("Constant C of Rank", i+1, ":  ", word_rank[i] * (frequency[i] / N))


    # making the graph
    plt.figure(figsize=(24, 12))
    plt.bar(wordRankMini, frequencyMini, align='center')
    plt.xlabel('Rank')
    plt.ylabel('Frequency') 
    plt.grid(True)
    plt.show() 
    
    