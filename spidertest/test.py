from PyQt5 import QtWidgets
import sys
from spidertest.SpiderUI import Ui_Form  # 导入ui文件转换后的py文件
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class mywindow(QtWidgets.QWidget, Ui_Form):
    _signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget_Video.setHorizontalHeaderLabels(['名称', '链接', '下载量', '下载'])
        self.tableWidget_Video.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_Video.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget_Video.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget_Video.horizontalHeader().setSectionResizeMode(3, 30)
        self.tableWidget_Video.setObjectName("tableWidget_video")
        self.tableWidget_Video.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_Music.setHorizontalHeaderLabels(['名称', '链接', '下载量', '下载'])
        self.tableWidget_Music.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_Music.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget_Music.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget_Music.horizontalHeader().setSectionResizeMode(3, 30)
        self.tableWidget_Music.setObjectName("tableWidget_Music")
        self.tableWidget_Music.verticalHeader().setDefaultSectionSize(30)
        self.searchButton.clicked.connect(self.insert)
        # self.file = open('C:/Users\Administrator/OneDrive/Python/spidertest/video.txt', 'wr', encoding='utf-8')
    # def insert(self):
    #     txt = open(r'C:/Users\Administrator/OneDrive/Python/spidertest/video.txt', 'rb')
    #     data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
    #     txt.close()
    #     print(data)
    def insert(self):
        txt = open(r'C:/Users\Administrator/OneDrive/Python/spidertest/video.txt', 'rb')
        data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
        list=data
        for i in range(5):
            item = QTableWidgetItem(list[i])
            self.tableWidget_Video.setItem(i,2,item)
            QApplication.processEvents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
