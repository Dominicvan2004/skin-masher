import json
import os

elements: dict = {}
skin_path: str = 'C:\\Users\\Owner\\AppData\\Local\\osu!\\Skins'
jason = open('test.json', mode='r')

# for skin in os.listdir(skin_path):
#   for ele in os.listdir(skin_path + '\\' + skin):
#     try:
#       elements[ele].append(skin_path + '\\' + skin + '\\' + ele)
#     except:
#       elements[ele] = [skin_path + '\\' + skin + '\\' + ele]

elements = json.load(jason)
for i in zip(elements['cursor.png'],elements['cursortrail.png']) :
  print(i)
  



