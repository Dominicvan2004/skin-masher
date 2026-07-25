from PyQt5.QtWidgets import (
  QMainWindow, 
  QApplication, 
  QPushButton,
  QLineEdit,
  QVBoxLayout,
  QGroupBox,
  QComboBox
  )
from PyQt5 import uic
from masher import find_skin_element as fse
from classes import Image
import sys
import os
import json
from save_data import save_data


#add functionality to the images and fix centering 

class UI(QMainWindow):

  def __init__(self):
    super(UI, self).__init__()

    uic.loadUi("untitled.ui", self)
    self.UIinit()



    self.jason = open('test.json', mode='r')
    self.elements: dict = json.load(self.jason)
    self.jason.close()
    
    self.element_combo.addItems(self.elements.keys())

    self.skin_button.clicked.connect(lambda: self.scrape(
      skin_path=self.line1.text(),
      json_path='test.json'
    ))

    self.element_button.clicked.connect(lambda: self.populate_layout(
      layout=self.form,
      element=self.element_combo.currentText(),
      element_dict=self.elements
    ))

    self.group.setLayout(self.form)

    self.show()

  def populate_layout(self, layout: QVBoxLayout, element: str, element_dict: dict):
    """
    Populate the UI with the desired elements

    layout: QFormLayout - The layout your populating\n
    element: str - The element you want to populate the UI with\n
    element_dict: dict - The dict holding all of the elements
    """
    #clearing the layout if has more than 0 elements
    if layout.count() > 0:
      for i in reversed(range(layout.count())): 
        layout.itemAt(i).widget().deleteLater()
      
    for ele in element_dict[element]:
       layout.addWidget(Image(ele, (100,100), self.elements['folder_path']))
       

  def UIinit(self) -> None:
    self.line1 = self.findChild(QLineEdit, "skinFolder")
    self.element_combo = self.findChild(QComboBox, "elements")
    self.skin_button = self.findChild(QPushButton, "pushButton")
    self.element_button = self.findChild(QPushButton, "elementButton")

    self.form = self.findChild(QVBoxLayout, 'vLayout')
    self.group = self.findChild(QGroupBox, 'groupBox')

  def scrape(self, skin_path: str, json_path: str):
    """
    Used to scrape the elements from skins in your skin folder

    skin_path: str - Path to your osu skin folder\n
    json_path: str - Path to the apps json file 
    """

    #I am aware theres probably one to many variables but it works so lets move on ok?
    elements_place: dict = {}
    jason = open(json_path, mode='w')

    #saving the folder path in a key
    elements_place['folder_path'] = self.line1.text()

    #for each skin path scraping the name of skin and then each element and putting them into their own key 
    for skin in os.listdir(skin_path):
      for ele in os.listdir(skin_path + '\\' + skin):
        try:
        #this works if the key already exsits
          elements_place[ele].append(skin_path + '\\' + skin + '\\' + ele)
        except:
        #if it doesnt then make a new key 
          elements_place[ele] = [skin_path + '\\' + skin + '\\' + ele]
    
        self.jason = open('test.json', mode='r')

      #dumping the dictionary we made into the jason file 
      jason = open(json_path, mode='w')
      json.dump(elements_place, jason)
      jason.close()

      #updating the UI's combobox
      self.jason = open('test.json', mode='r')
      self.elements: dict = json.load(self.jason)
      self.jason.close()




      self.element_combo.addItems(self.elements.keys())
  
app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()

