from re import I
import jieba
import jieba.posseg as pseg
from save_file import save_text

def print_text(sort_counts):
    for name,number in sort_counts:
        print(name,'number:',str(number))
def analyse_text(sort_counts):
    n_all_number=0
    no_n_number=0
    for x in sort_counts['n_all']: n_all_number+=x[1]
    for x in sort_counts['no_n']:no_n_number+=x[1]
    
    print("名词占比:"+str(n_all_number/(n_all_number+no_n_number)))


def process_txt(txt):
    words = pseg.cut(txt) #jieba默认模式
    all_counts={}
    sort_counts={'n_all':{},'no_n':{}}
    for word, flag in words:
    #print('%s %s' % (word, flag))
        all_counts[word] = all_counts.get(word, 0) + 1
        if(sort_counts.__contains__(flag)==False):sort_counts[flag]={}
        sort_counts[flag][word] = sort_counts[flag].get(word, 0) + 1
        if(flag.__contains__('n')):
            sort_counts['n_all'][word] = sort_counts['n_all'].get(word, 0) + 1
        else:
            sort_counts['no_n'][word] = sort_counts['no_n'].get(word, 0) + 1

    all_counts = list(all_counts.items())
    all_counts.sort(key=lambda x:x[1], reverse=True)

    for x in sort_counts:
        sort_counts[x] = list(sort_counts[x].items())
        sort_counts[x].sort(key=lambda x:x[1], reverse=True)
    
    analyse_text(sort_counts)
    save_text(sort_counts['n_all'])