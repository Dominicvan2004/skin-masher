from PyQt5.QtWidgets import (
    QLabel,
)
from PyQt5.QtGui import QPixmap


class Image(QLabel):
    def __init__(self, img_dir:str):
        super().__init__()
        self.setPixmap(QPixmap(img_dir))