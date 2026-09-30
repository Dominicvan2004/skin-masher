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
from classes import Image
import sys
import os
from data import add_to_db as add





class UI(QMainWindow):

  def __init__(self):
    super(UI, self).__init__()

    uic.loadUi("untitled.ui", self)
    self.UIinit()



    self.jason = open('test.json', mode='r')
    self.jason.close()
    
    self.element_combo.addItems(self.elements.keys())

    self.skin_button.clicked.connect(lambda: self.scrape(
      skin_path=self.line1.text(),
    ))

    self.element_button.clicked.connect(lambda: self.populate_layout(
      layout=self.form,
      element=self.element_combo.currentText(),
      element_dict=self.elements
    ))

    self.group.setLayout(self.form)

    self.show()
  def UIinit(self) -> None:
    self.line1 = self.findChild(QLineEdit, "skinFolder")
    self.element_combo = self.findChild(QComboBox, "elements")
    self.skin_button = self.findChild(QPushButton, "pushButton")
    self.element_button = self.findChild(QPushButton, "elementButton")

    self.form = self.findChild(QVBoxLayout, 'vLayout')
    self.group = self.findChild(QGroupBox, 'groupBox')

  def populate_layout(self, layout: QVBoxLayout, element: str, element_dict: dict):
    """
    Populate the UI with the desired elements

    layout (QVBoxLayout): The layout your populating\n
    element (str):  The element you want to populate the UI with\n
    element_dict (dict): The dict holding all of the elements
    """
    #clearing the layout if has more than 0 elements
    if layout.count() > 0:
      for i in reversed(range(layout.count())): 
        layout.itemAt(i).widget().deleteLater()
      
    for ele in element_dict[element]:
       layout.addWidget(Image(ele, (100,100), self.elements['folder_path']))
       
  def scrape(self, skin_path: str, json_path: str):
    """Used to scrape the elements from skins in your skin folder

      Parameters: 
          skin_path: str - Path to your osu skin folder
          json_path: str - Path to the apps json file
        
    """

    #I am aware theres probably one to many variables but it works so lets move on ok?
    elements_place: dict = {}
    
    #saving the folder path in a key
    elements_place['folder_path'] = self.line1.text()

    #for each skin path scraping the name of skin and then each element and putting them into their own key 
    for skin in os.listdir(skin_path):
      
    
        
  
app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()

