#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : LoL_lang_modificaton
# @File    : main.py
# @Author  : lee sure
# @Descriptions : main programming entry
# @Date    : 2023/7/4 22:48 
# @Software : PyCharm
import os
import sys
import base64
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QComboBox

from image import league_of_legends_alt_macos_bigsur_icon_190029_ico, china_icon_127906_ico, taiwan_icon_127914_ico, \
    krsouthkoreaflag_111691_ico, australia_icon_127744_ico
from read_config_file import modify_file, start_lol


with open(r'D:\python-workspaces\LoL_lang_modificaton\img\china.ico', 'wb') as w:
    w.write(base64.b64decode(china_icon_127906_ico))
with open(r'D:\python-workspaces\LoL_lang_modificaton\img\taiwan.ico', 'wb') as w:
    w.write(base64.b64decode(taiwan_icon_127914_ico))
with open(r'D:\python-workspaces\LoL_lang_modificaton\img\australia.ico', 'wb') as w:
    w.write(base64.b64decode(australia_icon_127744_ico))
with open(r'D:\python-workspaces\LoL_lang_modificaton\img\korea.ico', 'wb') as w:
    w.write(base64.b64decode(krsouthkoreaflag_111691_ico))
with open(r'D:\python-workspaces\LoL_lang_modificaton\img\lol.ico', 'wb') as w:
    w.write(base64.b64decode(league_of_legends_alt_macos_bigsur_icon_190029_ico))


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modfiy LOL Client Language")
        self.setWindowIcon(QIcon(r"./img/lol.ico"))
        self.button = QtWidgets.QPushButton("start game")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.cb = QComboBox()
        china_icon = QIcon(r"./img/china.ico")
        taiwan_icon = QIcon(r"./img/taiwan.ico")
        korea_icon = QIcon(r"./img/korea.ico")
        aus_icon = QIcon(r"./img/australia.ico")
        self.cb.addItem(aus_icon, "en_AU")
        self.cb.addItem(china_icon, "zh_CN")
        self.cb.addItem(taiwan_icon, "zh_TW")
        self.cb.addItem(korea_icon, "ko_KR")
        self.layout.addWidget(self.cb)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.confirmation)

    @Slot()
    def confirmation(self):
        modify_file(lang=self.cb.currentText())
        start_lol()
        print(self.cb.currentText())
        sys.exit(-1)
        # QtWidgets.QMessageBox.about(self, "warning", "write successfully, please restart your client")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(500, 300)
    widget.show()
    # remove pic after using
    os.remove(r'D:\python-workspaces\LoL_lang_modificaton\img\china.ico')
    os.remove(r'D:\python-workspaces\LoL_lang_modificaton\img\taiwan.ico')
    os.remove(r'D:\python-workspaces\LoL_lang_modificaton\img\australia.ico')
    os.remove(r'D:\python-workspaces\LoL_lang_modificaton\img\korea.ico')
    os.remove(r'D:\python-workspaces\LoL_lang_modificaton\img\lol.ico')

    sys.exit(app.exec())

