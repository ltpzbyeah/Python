from PyQt5 import QtWidgets

from spidertest.SpiderUI import Ui_Form  # 导入ui文件转换后的py文件

text = None
signal=None


class KeyText(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def GlobalText(self):
        global text
        text = self.lineEdit.text()
    def Signal(self):
        global signal

