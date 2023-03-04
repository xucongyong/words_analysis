pdf_file='/Users/xcy/Downloads/卡片笔记写作法.pdf'
import pdftotext
from save_file import save_text
from words_analysis import process_txt

from collections import Counter
import re

# 过滤不了\\ \ 中文（）还有————
r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'#用户也可以在此进行自定义过滤字符


# 者中规则也过滤不完全
r2 = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+"


# \\\可以过滤掉反向单杠和双杠，/可以过滤掉正向单杠和双杠，第一个中括号里放的是英文符号，第二个中括号里放的是中文符号，第二个中括号前不能少|，否则过滤不完全
r3 =  "[.!//_,$&%^*()<>+\"'?@#-|:~{}]+|[——！\\\\，。=？、：“”‘’《》【】￥……（）]+"


# 去掉括号和括号内的所有内容
r4 =  "\\【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\\\，。=？、：“”‘’￥……（）《》【】]"


import csv




def analysis(text):
    cnt = Counter()
    for word in text:
        cnt[word] += 1
    cnt.most_common()
    with open('counter_test.csv','w') as csvfile:
        writer=csv.writer(csvfile)
        for key, value in cnt.most_common():
            writer.writerow([key] + [value])
        
    # print(cnt)
    for x in cnt.most_common():
        print(x)

def deal_text(text):
    flag_array = ("n","t",'PER','ORG','ORG','TIME') # https://github.com/fxsjy/jieba
    text = text.replace("\n", " ")
    text = text.replace(" ", "")
    text = text.replace(" ", "")
    text = text.replace("，", "")
    text = text.replace("。", "")
    text = re.sub(r4, '', text)
    seg_list = pseg.cut(text,use_paddle=True)
    new_text = []
    for word, flag in seg_list:
        # print('%s %s' % (word, flag))
        if(flag.endswith(flag_array)):
            new_text.append(word)

    analysis(new_text)


def read_pdf():
    all_text = ''
    with open(pdf_file, "rb") as f:
        pdf = pdftotext.PDF(f)
        for page in pdf:
            all_text +=page
    save_text(all_text)
    process_txt(all_text) 
    #deal_text(text)

read_pdf()
