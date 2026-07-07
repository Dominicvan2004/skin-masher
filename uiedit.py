from PyQt5.QtWidgets import (
  QMainWindow, 
  QApplication, 
  QLabel, 
  QPushButton,
  QLineEdit,
  QScrollArea,
  QWidget,
  QFormLayout,
  QGroupBox
  )
from PyQt5 import uic
from masher import find_skin_element as fse
from classes import Image
import sys
import os
import json

class UI(QMainWindow):
  def __init__(self):
    super(UI, self).__init__()

    uic.loadUi("untitled.ui", self)
    self.UIinit()

    self.dir_dict: dict= {
      'skin_path': ''
    }


    jason = open('test.json', mode='r')
    elements: dict = json.load(jason)

    self.line1.textChanged.connect(lambda: self.update_dir(self.dir_dict, 'skin_path',  self.line1))
   
    for path in elements['hitcircle.png']:
      self.form.addWidget(Image(path, (20,20)))
    
    self.group.setLayout(self.form) 

    self.pushButt.clicked.connect(lambda: fse(
      dstn=self.dir_dict['ele_path'],
      direct=self.dir_dict['skin_path'],
      element=self.dir_dict['skin_ele']))

    self.show()


  def UIinit(self) -> None:
    self.line1 = self.findChild(QLineEdit, "skinFolder")
    self.pushButt = self.findChild(QPushButton, "pushButton")

    self.form = self.findChild(QFormLayout, 'formLayout')
    self.group = self.findChild(QGroupBox, 'groupBox')
  


  def update_dir(self, var: dict, key: str, line: QLineEdit)->None:
    var[key] = line.text()
    print(var[key])

app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()

