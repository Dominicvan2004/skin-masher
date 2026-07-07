from PyQt5.QtWidgets import (
  QMainWindow, 
  QApplication, 
  QPushButton,
  QLineEdit,
  QFormLayout,
  QGroupBox,
  QComboBox
  )
from PyQt5 import uic
from masher import find_skin_element as fse
from classes import Image
from data import scrape
import sys
import os
import json


#handle input for folder and make the json thing a function

class UI(QMainWindow):
  def __init__(self):
    super(UI, self).__init__()

    uic.loadUi("untitled.ui", self)
    self.UIinit()

    jason = open('test.json', mode='r')
    elements: dict = json.load(jason)

    self.element_combo.addItems(elements.keys())

    self.skin_button.clicked.connect(lambda: scrape(
      skin_path=self.line1.text(),
      json_path='test.json'
    ))

    self.element_button.clicked.connect(lambda: self.populate_layout(
      layout=self.form,
      element=self.element_combo.currentText(),
      element_dict=elements
    ))

    self.group.setLayout(self.form)

    self.show()

  def populate_layout(self, layout: QFormLayout, element: str, element_dict: dict):
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
       layout.addWidget(Image(ele, (100,100)))
       

  def UIinit(self) -> None:
    self.line1 = self.findChild(QLineEdit, "skinFolder")
    self.element_combo = self.findChild(QComboBox, "elements")
    self.skin_button = self.findChild(QPushButton, "pushButton")
    self.element_button = self.findChild(QPushButton, "elementButton")

    self.form = self.findChild(QFormLayout, 'formLayout')
    self.group = self.findChild(QGroupBox, 'groupBox')
  
app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()

