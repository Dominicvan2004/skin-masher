from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QComboBox
)
from PyQt5.QtGui import QPixmap
import os
from shutil import copy
class Image(QWidget):
    def __init__(self, img_dir:str, scale: tuple, path:str):
        super().__init__()
        #initialzing widgets 
        self.hlayout = QHBoxLayout()
        self.path = path
        self.img_dir = img_dir
        self.label = QLabel()
        self.label.setPixmap(QPixmap(img_dir).scaled(scale[0], scale[1]))
        self.button = QPushButton('Add to Skin')

        #adding event on button click
        self.button.clicked.connect(self.Add_element)

        #adding widgets to layout
        self.hlayout.addWidget(self.label)
        self.hlayout.addWidget(self.button)

        self.setLayout(self.hlayout)
    def Add_element(self):
        """
        Controls combo box menu and adds element to the selected skin.
        """

        combo = QComboBox()
        
        combo.addItems(os.listdir(self.path))
        self.hlayout.addWidget(combo)
        combo.currentIndexChanged.connect(lambda: copy(self.img_dir, (self.path + "\\" + combo.currentText())))
        combo.currentIndexChanged.connect(combo.deleteLater)






        
    



        

        
     
       