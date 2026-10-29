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
# from schemas import(
#   Element,
#   FolderPath
# )





class UI(QMainWindow):

  def __init__(self):
    super(UI, self).__init__()
    uic.loadUi("app.ui", self)
    self.UIinit()
    engine = create_engine("sqlite:///database.db")
    self.con = db_connection(engine=engine,
                             skin_folder_path=self.line1.text())


    

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
      
    # for ele in element_dict[element]:
    #    layout.addWidget(Image(ele, (100,100), self.elements['folder_path']))
    

       
  def scrape(self, skin_path: str, json_path: str):
    
      
    
        
  
app = QApplication(sys.argv)

UIWindow = UI()
app.exec_()

