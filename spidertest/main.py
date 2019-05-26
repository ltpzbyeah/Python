
from PyQt5 import QtWidgets
import sys
from spidertest.SpiderUI import Ui_Form  # 导入ui文件转换后的py文件
from PyQt5.QtWidgets import *
from scrapy.cmdline import execute  # 调用此函数可以执行scrapy的脚本
from spidertest.keyText import KeyText
import threading

from PyQt5.QtCore import QObject, pyqtSignal, QThread, QBasicTimer



class ThreadObject(QObject):
    _thread = pyqtSignal()

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        mywindow.progressBar.setValue(self.step)




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
        self.searchButton.clicked.connect(self.checkComboBox)
        self.mythread = ThreadObject()
        # 连接信号
        self.mythread._thread.connect(self.video)
        self.thread = QThread()
        self.mythread.moveToThread(self.thread)
        # 开始线程
        self.thread.started.connect(self.mythread.timerEvent)
        self.thread.start()
        self.timer = QBasicTimer()
        self.step = 0

    def checkComboBox(self):
        self.searchButton.setEnabled(False)
        if self.comboBox.currentText() == '视频':
            self.stackedWidget.setCurrentIndex(0)
            self.video()

        if self.comboBox.currentText() == '音乐':
            self.music()

        if self.comboBox.currentText() == '百科':
            self.search()
    def video(self):
        KeyText.GlobalText(self)
        execute(['scrapy', 'crawl', 'videospider'])
        self.move_thread.start()

    def music(self):
        self.stackedWidget.setCurrentIndex(1)

        # execute(['scrapy', 'crawl', 'musicspider'])
        # self.pyThread = threading.Thread(target=self.music)
        # self.pyThread.start()

    def search(self):
        self.stackedWidget.setCurrentIndex(2)

        # execute(['scrapy', 'crawl', 'searchspider'])
        # self.pyThread = threading.Thread(target=self.search)
        # self.pyThread.start()

    # def spidersignal(self):
    def closeEvent(self, event):
        self.move_thread.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
