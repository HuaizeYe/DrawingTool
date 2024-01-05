import os, PySide6

from PySide6.QtCore import QRect
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, Qt, QFont
from PySide6.QtWidgets import QStyleOption, QFrame, QGraphicsView, \
    QGraphicsScene, QGraphicsItem, QGraphicsEllipseItem, QGraphicsItemGroup, QMenu
from shape.circle import Circle
from shape.rectangle import Rectangle
from shape.combination import Combination
from shape.triangle import Triangle
from shape.line import Line

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PySide6 import QtCore, QtGui, QtWidgets
import sys
from random import random


class DrawView(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setGeometry(QRect(145, 5, 650, 490))
        self.setStyleSheet('border: 2px solid #F96BDE')
        self.setRenderHints(QPainter.Antialiasing |  # 抗锯齿
                            QPainter.TextAntialiasing |  # 文字抗锯齿
                            QPainter.SmoothPixmapTransform |  # 使图元变换更加平滑
                            QPainter.LosslessImageRendering)  # 不失真的图片渲染
        # 视窗更新模式
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        # 设置拖拽模式
        self.setDragMode(self.RubberBandDrag)
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QColor(255, 255, 255))
        self.setScene(self.scene)
        self.setSceneRect(QRect(0, 0, 640, 480))
        self.selectedItem = []
        self.sceneStack = []
        # self.scene.St
        # self.currentItem = QGraphicsItemGroup()
        # self.currentItem.addToGroup(Circle(QRect(10 ,10, 200, 200)))
        # self.currentItem.addToGroup(Circle(QRect(20, 20, 200, 200)))
        # self.scene.addItem(self.currentItem)
        self.currentItemNum = 0

    def addCircle(self):
        newCircle = Circle(QRect(10 * self.currentItemNum, 10 * self.currentItemNum, 200, 200))
        self.scene.addItem(newCircle)
        self.currentItemNum += 1
        self.sceneStack.append({'remove': [newCircle]})
        return newCircle

    def addRectangle(self):
        newRectangle = Rectangle(QRect(10 * self.currentItemNum, 10 * self.currentItemNum, 200,
                                       200))  # Rectangle(QRect(10 * self.currentItemNum, 10 * self.currentItemNum, 200, 200))
        self.scene.addItem(newRectangle)
        self.currentItemNum += 1
        self.sceneStack.append({'remove': [newRectangle]})
        return newRectangle

    def addTriangle(self):
        newTriangle = Triangle(QRect(10 * self.currentItemNum, 10 * self.currentItemNum, 200,
                                     200))  # Rectangle(QRect(10 * self.currentItemNum, 10 * self.currentItemNum, 200, 200))
        self.scene.addItem(newTriangle)
        self.currentItemNum += 1
        self.sceneStack.append({'remove': [newTriangle]})
        return newTriangle

    def addLine(self):
        newLine = Line(QRect(10 * self.currentItemNum, 10 * self.currentItemNum, 200,
                             20))  # Rectangle(QRect(10 * self.currentItemNum, 10 * self.currentItemNum, 200, 200))
        self.scene.addItem(newLine)
        self.currentItemNum += 1
        self.sceneStack.append({'remove': [newLine]})
        return newLine

    def Copy(self):
        self.selectedItem = []
        sign = ''
        for i in self.scene.selectedItems():
            self.selectedItem.append(i)
            sign += i.name + ' '

        return '复制' + sign

    # 无法复制修改大小的物体
    def Paste(self):
        sign = ''
        status = []
        for i in self.selectedItem:
            if i.name == "Circle":
                newCircle = Circle(i.x() + 30, i.y() + 30, i.rect().width(), i.rect().height())
                newCircle.text.setPlainText(i.text.toPlainText())
                self.scene.addItem(newCircle)
                status.append(newCircle)
            if i.name == "Rectangle":
                newRectangle = Rectangle(i.x() + 30, i.y() + 30, i.rect().width(), i.rect().height())
                newRectangle.text.setPlainText(i.text.toPlainText())
                self.scene.addItem(newRectangle)
                status.append(newRectangle)
            if i.name == "Triangle":
                newTriangle = Triangle(i.x() + 30, i.y() + 30, i.rect().width(), i.rect().height())
                newTriangle.text.setPlainText(i.text.toPlainText())
                self.scene.addItem(newTriangle)
                status.append(Triangle)

            if i.name == "Line":
                newLine = Line(i.x() + 30, i.y() + 30, i.rect().width(), i.rect().height())
                newLine.text.setPlainText(i.text.toPlainText())
                self.scene.addItem(newLine)
                status.append(newLine)

            if i.name == "Combination":
                newCombinataion = Combination(i.itemList)
                newCombinataion.text.setPlainText(i.text.toPlainText())
                self.scene.addItem(newCombinataion)
                status.append(newCombinataion)
            sign += i.name + ' '
        self.sceneStack.append({'remove': status})
        return '粘贴' + sign

    def Combine(self):
        s = self.scene.selectedItems()
        newCombination = Combination(s)
        add = []
        for i in s:
            self.scene.removeItem(i)
            add.append(i)
        self.scene.addItem(newCombination)
        self.sceneStack.append({'remove': [newCombination], 'add': add})
        return '组合完成'

    def Delete(self):
        sign = ''
        s = self.scene.selectedItems()
        add = []
        for i in s:
            self.scene.removeItem(i)
            sign += i.name
            add.append(i)
        self.sceneStack.append({'add': add})
        return '删除' + sign

    def Angle(self, angle):
        sign = ''
        s = self.scene.selectedItems()
        for i in s:
            sign += i.name + ' '
            i.setRotation(angle)
        return '旋转' + sign + str(angle) + '°'

    def Font(self, fontsize):
        sign = ''
        s = self.scene.selectedItems()
        for i in s:
            sign += i.name + ' '
            font = QFont()
            font.setPixelSize(fontsize)
            i.text.setFont(font)
        return '调整' + sign + '字体为'+str(fontsize)

    def Undo(self):
        if len(self.sceneStack) >= 1:
            if 'remove' in self.sceneStack[-1]:
                for i in self.sceneStack[-1]['remove']:
                    self.scene.removeItem(i)
            if 'add' in self.sceneStack[-1]:
                for i in self.sceneStack[-1]['add']:
                    self.scene.addItem(i)
            self.sceneStack.pop(-1)
            return '撤销成功'
        return '撤销失败'

    def Pen(self,r,g,b):
        sign = ''
        s = self.scene.selectedItems()
        for i in s:
            sign += i.name + ' '
            i.myPen(r,g,b)
        return '设置' + sign + '边框颜色'

    def Brush(self,r,g,b):
        sign = ''
        s = self.scene.selectedItems()
        for i in s:
            sign += i.name + ' '
            i.myBrush(r,g,b)
        return '设置' + sign + '填充颜色'

    # def contextMenuEvent(self, event):
    #     menu = QMenu()
    #     removeAction = menu.addAction("Remove")
    #     markAction = menu.addAction("Mark")
    #     selectedAction = menu.exec(self.mapToGlobal(event.pos()))
