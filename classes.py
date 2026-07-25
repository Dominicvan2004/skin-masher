from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QComboBox
)
from PyQt5.QtGui import QPixmap
import os
class Image(QWidget):
    def __init__(self, img_dir:str, scale: tuple, path:str):
        super().__init__()
        self.hlayout = QHBoxLayout()
        self.path = path
        self.img_dir = img_dir
        self.label = QLabel()
        self.label.setPixmap(QPixmap(img_dir).scaled(scale[0], scale[1]))
        self.button = QPushButton('Add to Skin')

        self.button.clicked.connect(self.add_element)

        self.hlayout.addWidget(self.label)
        self.hlayout.addWidget(self.button)

        self.setLayout(self.hlayout)
    def add_element(self):
        """
        Adds the element to the selected skin
        """
        combo = QComboBox()
        choice: str = combo.currentText()
        combo.addItems(os.listdir(self.path))
        self.hlayout.addWidget(combo)
        combo.currentIndexChanged.connect(combo.deleteLater)



        
    



        

        
     
       