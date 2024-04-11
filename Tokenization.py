import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import font_manager



word_dic = {}
PUNC = ["።","፤","።","."]
num = ["፪","፫","፬","፭","ዕፀ","፮","፯","፰","፱","",".","?",":","1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
sorted_dict_values = {}


def Tokenization(f):
    global sorted_dict_values
    for line in f:
        words = line.lower().split(" ")
        for word in words:
            if word in num:
                words.remove(word)
            else:
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
    

    custom_font_entry = font_manager.FontEntry(fname="C:\\Windows\\Fonts\\nyala.ttf", name='CustomFont')
    font_manager.fontManager.ttflist.insert(0, custom_font_entry)
    plt.rcParams['font.family'] = 'CustomFont'


    print(sorted_dict_values)
    word_rank  = []               

    """ for key, value in sorted_dict_values.items():
        print(key, value) """

    word_rank = list(range(1, len(sorted_dict_values) + 1))

    kale = list(sorted_dict_values.values())

    wordRankMini = []
    for i in range(1):
        wordRankMini.append(word_rank[i])

    kaleMini = []
    for i in range(1):
        kaleMini.append(kale[i])

    plt.figure(figsize=(24, 12))
    plt.bar(wordRankMini, kaleMini, align='center', tick_label=sorted_dict_values.keys())
    plt.xlabel('ራንክ')
    plt.ylabel('ቃል') 
    plt.grid(True)
    plt.show() 
    