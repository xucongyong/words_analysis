#!/usr/bin/python3 

from save_file import save_text
from words_analysis import process_txt
#draft_info.json
#windows路径：C:\Users\Administrator\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\202108091029
#macos路径：/Users/xcy/Movies/JianyingPro/User Data/Projects/com.lveditor.draft

import time
now = time.time()
import json


files="./draft_info.json"
# def save(all_text):
#   print('save file name:'+str(now)+'.md')
#   with open(str(now)+".md", "w") as outfile:
#       outfile.write(all_text)
def read():
  txt = open(files, "r", encoding="utf-8").read()
  json_object = json.loads(txt)
  texts = json_object['materials']['texts']
  all_text=""
  for i in texts:
    all_text+=i['content']
  return all_text
all_text=read()
save_text(all_text)
process_txt(all_text)


  # function popFileSelector(files) {
  #   if (files && files.length > 0) {
  #     const file = files[0]
  #     const reader = new FileReader()
  #     if (typeof FileReader === 'undefined') {
  #       alert('您的浏览器不支持文件读取,请使用最新版的Chrome浏览器进行此操作！')
  #       return
  #     }
  #     var status = document.getElementById("status");
  #     var program = document.getElementById("program");
  #     // 读取文件
  #     reader.readAsText(file, 'utf-8') // 设置编码格式
  #     reader.onload = () => { // 读取操作完成
  #       let str = reader.result;
  #       console.log(str); // 打印文件文本内容

  #       status.innerText = "状态：已读取文件，正在解析"
  #       try {
  #         const obj = JSON.parse(str)
  #         const list = obj.materials.texts.map((e) => e.content)
  #         console.log(list); // 打印解析出的内容
  #         program.value = list
  #         status.innerText = "状态：解析成功，请自行复制，再次导入请刷新页面"
  #         status.style.color = "green"

  #         for (var i = 0, len = list.length; i < len; i++) {
  #           var table = document.querySelector('table')
  #           var tr = document.createElement('tr')
  #           var text = document.createTextNode(list[i])
  #           tr.appendChild(text)
  #           table.appendChild(tr)
  #         }
  #         // alert('文件解析成功')
  #       } catch (error) {
  #         program.value = ""
  #         status.innerText = "状态：解析失败，请查看选择的是否是 draft_content.json 文件，再次导入请刷新页面"
  #         status.style.color = "red"
  #         alert('文件解析失败')
  #       }
  #     }
  #     reader.onerror = (e) => { // 读取失败
  #       status.innerText = "状态：文件读取失败，再次导入请刷新页面"
  #       console.error('文件读取失败:', e)
  #     }
  #   } else {
  #     status.value = "状态：文件读取失败，再次导入请刷新页面"
  #   }
  # }
