
from words_analysis import process_txt
def open_txt():
    file_path = '/Users/xcy/Downloads/video/gaoshou/text/高手习惯3.md'
    txt = open(file_path, "r", encoding="utf-8").read()
    process_txt(txt)
    return txt


open_txt()