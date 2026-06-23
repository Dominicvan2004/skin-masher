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
class UI(QMainWindow):
  def __init__(self):
    super(UI, self).__init__()

    uic.loadUi("untitled.ui", self)
    self.UIinit()

    self.dir_dict = {
      'skin_ele': '',
      'skin_path': '',
      'ele_path': ''
    }

    self.line1.textChanged.connect(lambda: self.update_dir(self.dir_dict, 'skin_ele',  self.line1))
    self.line2.textChanged.connect(lambda: self.update_dir(self.dir_dict, 'ele_path',  self.line2))
    self.line3.textChanged.connect(lambda: self.update_dir(self.dir_dict, 'skin_path', self.line3))

   
    for i in os.listdir('cursors'):
      self.form.addRow(Image(f'cursors\\{i}'))

    self.group.setLayout(self.form)



  
    self.pushButt.clicked.connect(lambda: fse(
      dstn=self.dir_dict['ele_path'],
      direct=self.dir_dict['skin_path'],
      element=self.dir_dict['skin_ele']))

    self.show()


  def UIinit(self) -> None:
    self.line1 = self.findChild(QLineEdit, "line1")
    self.line2 = self.findChild(QLineEdit, "line2")
    self.line3 = self.findChild(QLineEdit, "line3")
    self.pushButt = self.findChild(QPushButton, "pushButton")

    self.form = self.findChild(QFormLayout, 'form')
    self.group = self.findChild(QGroupBox, 'groupBox')
    self.area = self.findChild(QScrollArea, 'scrollArea')
  


  def update_dir(self, var: dict, key: str, line: QLineEdit)->None:
    var[key] = line.text()
    print(var[key])

app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()

