import time
now = time.time()
def save_text(all_text):
    print('save file name:'+str(now)+'.md')
    with open(str(now)+".md", "w") as outfile:
      outfile.write(str(all_text))
