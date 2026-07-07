from PyQt5.QtWidgets import (
    QLabel
)
from PyQt5.QtGui import QPixmap
import PyQt5.QtCore as Q


class Image(QLabel):
    def __init__(self, img_dir:str, scale: tuple):
        super().__init__()
        self.setPixmap(QPixmap(img_dir).scaled(scale[0], scale[1]))
        self.img_dir = img_dir
        


        

        
     
       