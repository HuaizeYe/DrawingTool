#单例 组合 装饰器 原型 外观 中介者 模板模式
import os
import sys

import PySide6
from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget, QFrame, QTextBrowser, QSpinBox
from PySide6.QtGui import QPainter, QColor

from draw_view import DrawView

pysideDir = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(pysideDir, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


# 定义主窗体
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.basic_setup()

        self.pushButtonCircle.clicked.connect(lambda: self.drawArea.addCircle())
        self.pushButtonRectangle.clicked.connect(lambda:self.drawArea.addRectangle())
        self.pushButtonTriangle.clicked.connect(lambda: self.drawArea.addTriangle())
        self.pushButtonLine.clicked.connect(lambda: self.drawArea.addLine())
        self.pushButtonCopy.clicked.connect(lambda: self.status.setText(self.drawArea.Copy()))
        self.pushButtonPaste.clicked.connect(lambda: self.status.setText(self.drawArea.Paste()))
        self.pushButtonCombine.clicked.connect(lambda: self.status.setText(self.drawArea.Combine()))
        self.pushButtonDelete.clicked.connect(lambda: self.status.setText(self.drawArea.Delete()))
        self.pushButtonUndo.clicked.connect(lambda: self.status.setText(self.drawArea.Undo()))
        self.pushButtonAngle.clicked.connect(lambda: self.status.setText(self.drawArea.Angle(self.spinboxAngle.value())))
        self.pushButtonFont.clicked.connect(lambda: self.status.setText(self.drawArea.Font(self.spinboxFont.value())))
        self.pushButtonColor.clicked.connect(lambda: self.status.setText(self.drawArea.Pen(self.spinboxR.value(),
                                                                                           self.spinboxG.value(),
                                                                                           self.spinboxB.value())))

    def basic_setup(self):
        if not self.objectName():
            self.setObjectName(u"Mainwindow")
        self.resize(800, 500)
        self.setFixedSize(QSize(800, 500))
        self.setStyleSheet("background:#FFEEEE")

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        # 按钮区初始设置
        self.buttonArea = QFrame(self.centralwidget)
        self.buttonArea.setObjectName(u"buttonArea")
        self.buttonArea.setGeometry(QRect(5, 5, 140, 200))
        self.buttonArea.setFixedSize(QSize(135, 140))
        self.buttonArea.setStyleSheet('border: 2px solid #F96217')
        self.pushButtonCircle = QPushButton(self.buttonArea)
        self.pushButtonCircle.setObjectName(u"pushButtonCircle")
        self.pushButtonCircle.setGeometry(QRect(5, 5, 60, 60))
        self.pushButtonCircle.setFlat(True)
        self.pushButtonCircle.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonRectangle = QPushButton(self.buttonArea)
        self.pushButtonRectangle.setObjectName(u"pushButtonRectangle")
        self.pushButtonRectangle.setGeometry(QRect(70, 5, 60, 60))
        self.pushButtonRectangle.setFlat(True)
        self.pushButtonRectangle.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonLine = QPushButton(self.buttonArea)
        self.pushButtonLine.setObjectName(u"pushButtonLine")
        self.pushButtonLine.setGeometry(QRect(5, 70, 60, 60))
        self.pushButtonLine.setFlat(True)
        self.pushButtonLine.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonTriangle = QPushButton(self.buttonArea)
        self.pushButtonTriangle.setObjectName(u"pushButtonTriangle")
        self.pushButtonTriangle.setGeometry(QRect(70, 70, 60, 60))
        self.pushButtonTriangle.setFlat(True)
        self.pushButtonTriangle.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')

        self.settingArea = QFrame(self.centralwidget)
        self.settingArea.setObjectName(u"settingArea")
        self.settingArea.setGeometry(QRect(5, 150, 140, 250))
        self.settingArea.setFixedSize(QSize(135, 345))
        self.settingArea.setStyleSheet('border: 2px solid #F96217')

        self.pushButtonCopy = QPushButton(self.settingArea)
        self.pushButtonCopy.setObjectName(u"pushButtonCopy")
        self.pushButtonCopy.setGeometry(QRect(5, 5, 60, 20))
        self.pushButtonCopy.setFlat(True)
        self.pushButtonCopy.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonCopy.setText("复制")
        self.pushButtonPaste = QPushButton(self.settingArea)
        self.pushButtonPaste.setObjectName(u"pushButtonPaste")
        self.pushButtonPaste.setGeometry(QRect(70, 5, 60, 20))
        self.pushButtonPaste.setFlat(True)
        self.pushButtonPaste.setText("粘贴")
        self.pushButtonPaste.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonCombine = QPushButton(self.settingArea)
        self.pushButtonCombine.setObjectName(u"pushButtonCombine")
        self.pushButtonCombine.setGeometry(QRect(5, 30, 60, 20))
        self.pushButtonCombine.setFlat(True)
        self.pushButtonCombine.setText("组合")
        self.pushButtonCombine.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonDelete = QPushButton(self.settingArea)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setGeometry(QRect(5, 55, 60, 20))
        self.pushButtonDelete.setFlat(True)
        self.pushButtonDelete.setText("删除")
        self.pushButtonDelete.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonUndo = QPushButton(self.settingArea)
        self.pushButtonUndo.setObjectName(u"pushButtonUndo")
        self.pushButtonUndo.setGeometry(QRect(70, 30, 60, 20))
        self.pushButtonUndo.setFlat(True)
        self.pushButtonUndo.setText("撤销")
        self.pushButtonUndo.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.pushButtonAngle = QPushButton(self.settingArea)
        self.pushButtonAngle.setObjectName(u"pushButtonAngle")
        self.pushButtonAngle.setGeometry(QRect(70, 80, 60, 20))
        self.pushButtonAngle.setFlat(True)
        self.pushButtonAngle.setText("角度")
        self.pushButtonAngle.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.spinboxAngle = QSpinBox(self.settingArea)
        self.spinboxAngle.setObjectName(u"spinboxAngle")
        self.spinboxAngle.setGeometry(QRect(5, 80, 60, 20))
        self.spinboxAngle.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.spinboxAngle.setMaximum(359)
        self.spinboxAngle.setMinimum(0)

        self.pushButtonFont = QPushButton(self.settingArea)
        self.pushButtonFont.setObjectName(u"pushButtonFont")
        self.pushButtonFont.setGeometry(QRect(70, 105, 60, 20))
        self.pushButtonFont.setFlat(True)
        self.pushButtonFont.setText('字体')
        self.pushButtonFont.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.spinboxFont = QSpinBox(self.settingArea)
        self.spinboxFont.setObjectName(u"spinboxFont")
        self.spinboxFont.setGeometry(QRect(5, 105, 60, 20))
        self.spinboxFont.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.spinboxFont.setMaximum(20)
        self.spinboxFont.setMinimum(6)

        self.spinboxR = QSpinBox(self.settingArea)
        self.spinboxR.setObjectName(u"spinboxR")
        self.spinboxR.setGeometry(QRect(5, 130, 45, 20))
        self.spinboxR.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.spinboxR.setMaximum(255)
        self.spinboxR.setMinimum(0)


        self.spinboxG = QSpinBox(self.settingArea)
        self.spinboxG.setObjectName(u"spinboxG")
        self.spinboxG.setGeometry(QRect(45, 130, 45, 20))
        self.spinboxG.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.spinboxG.setMaximum(255)
        self.spinboxG.setMinimum(0)

        self.spinboxB = QSpinBox(self.settingArea)
        self.spinboxB.setObjectName(u"spinboxB")
        self.spinboxB.setGeometry(QRect(85, 130, 45, 20))
        self.spinboxB.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')
        self.spinboxB.setMaximum(255)
        self.spinboxB.setMinimum(0)

        self.pushButtonColor = QPushButton(self.settingArea)
        self.pushButtonColor.setObjectName(u"pushButtonColor")
        self.pushButtonColor.setGeometry(QRect(5, 155, 60, 20))
        self.pushButtonColor.setFlat(True)
        self.pushButtonColor.setText('边框颜色')
        self.pushButtonColor.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')

        self.pushButtonBrush = QPushButton(self.settingArea)
        self.pushButtonBrush.setObjectName(u"pushButtonBrush")
        self.pushButtonBrush.setGeometry(QRect(70, 155, 60, 20))
        self.pushButtonBrush.setFlat(True)
        self.pushButtonBrush.setText('填充颜色')
        self.pushButtonBrush.setStyleSheet('border: 2px solid #FCA55E; border-radius: 20px;')

        self.pushButtonTip = QTextBrowser(self.settingArea)
        self.pushButtonTip.setObjectName(u"pushButtonTip")
        self.pushButtonTip.setGeometry(QRect(5, 205, 125, 80))
        self.pushButtonTip.setText("使用说明:\n1.复制粘贴功能不支持旋转、组合修改大小、字体\n2.撤销只会在关键功能记录状态，因此不支持大小修改，位置变换，字体大小调整和角度调整\n3.组合不支持旋转、文字标签")
        self.pushButtonTip.setStyleSheet('border: 2px solid #FCA55E')
        self.status = QTextBrowser(self.settingArea)
        self.status.setGeometry(QRect(5,290,125,48))
        self.status.setText("状态栏")
        self.drawArea = DrawView(self.centralwidget)

        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("画图工具")
        self.pushButtonCircle.setText("圆")
        self.pushButtonRectangle.setText("矩形")
        self.pushButtonLine.setText("线")
        self.pushButtonTriangle.setText("三角形")
        # QMetaObject.connectSlotsByName(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    # sys.exit(app.exec_())
