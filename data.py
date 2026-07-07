import json
import os

#soimething to scrape the skin directroy and store the entire skin folder into a json file
#each 
def scrape(skin_path: str, json_path: str):
  """
  Used to scrape the elements from skins in your skin folder

  skin_path: str - Path to your osu skin folder
  json_path: str - Path the apps json file 
  """
  elements: dict = {}
  jason = open(json_path, mode='w')

  for skin in os.listdir(skin_path):
    for ele in os.listdir(skin_path + '\\' + skin):
      try:
      #this works if the key already exsits
        elements[ele].append(skin_path + '\\' + skin + '\\' + ele)
      except:
      #if it doesnt then make a new key 
        elements[ele] = [skin_path + '\\' + skin + '\\' + ele]

    jason = open(json_path, mode='w')
    json.dump(elements, jason)
    jason.close()


  



