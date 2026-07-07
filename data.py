import json
import os

#soimething to scrape the skin directroy and store the entire skin folder into a json file
#each 

elements: dict = {}
skin_path: str = 'C:\\Users\\Owner\\AppData\\Local\\osu!\\Skins'
jason = open('test.json', mode='r')

for skin in os.listdir(skin_path):
  for ele in os.listdir(skin_path + '\\' + skin):
    try:
    #this works if the key already exsits
      elements[ele].append(skin_path + '\\' + skin + '\\' + ele)
    except:
    #if it doesnt then make a new key 
      elements[ele] = [skin_path + '\\' + skin + '\\' + ele]

elements = json.load(jason)

print(elements['cursor.png'])

  



