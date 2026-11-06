from PyQt5.QtWidgets import (
  QMainWindow, 
  QApplication, 
  QPushButton,
  QLineEdit,
  QVBoxLayout,
  QGroupBox,
  QComboBox
  )
from sqlalchemy import create_engine
from PyQt5 import uic
from classes import Image
import sys
import os
from data import (
  db_connection
)
from schemas import Cursor





class UI(QMainWindow):

  def __init__(self):
    super(UI, self).__init__()
    uic.loadUi("app.ui", self)
    self.UIinit()
    engine = create_engine("sqlite:///database.db")
    self.con = db_connection(engine=engine, skin_folder_path=self.line1.text())

    self.folder_button.clicked.connect(self.scrape)
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
    self.folder_button = self.findChild(QPushButton, "folder_button")
    self.element_button = self.findChild(QPushButton, "elementButton")

    self.form = self.findChild(QVBoxLayout, 'vLayout')
    self.group = self.findChild(QGroupBox, 'groupBox')

  def populate_layout(self, list_of_elements: list):
    """
    Populate the UI with the desired elements

    layout (QVBoxLayout): The layout your populating\n
    element (str):  The element you want to populate the UI with\n
    element_dict (dict): The dict holding all of the elements
    """
    #clearing the layout if has more than 0 elements
    if self.form.count() > 0:
      for i in reversed(range(self.form.count())): 
        self.form.itemAt(i).widget().deleteLater()
      
    for image in list_of_elements:
       self.form.addWidget(image)
       
  def scrape(self):
      self.con.skin_folder_path=self.line1.text()
      print()
      self.con.scrape_add_element(
        table=Cursor,
        element="cursor.png"
      )
    
        
  
app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()

