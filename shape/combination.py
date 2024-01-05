from PySide6.QtCore import QPoint
from PySide6.QtGui import QPen, QColor, QBrush, QPainter, Qt, QPolygon
from PySide6.QtWidgets import QGraphicsItem, QGraphicsEllipseItem
from shape.base import Base


class Combination(Base):
    def __init__(self, items):
        self.itemList = items
        topLeftX = 600
        topLeftY = 600
        bottomRightX = 0
        bottomRightY = 0
        for i in self.itemList:
            if topLeftX > i.x() + i.rect().x():
                topLeftX = i.x() + i.rect().x()
            if topLeftY > i.y() + i.rect().y():
                topLeftY = i.y() + i.rect().y()
            if i.x() + i.rect().x() + i.rect().width() > bottomRightX:
                bottomRightX = i.x() + i.rect().x() + i.rect().width()
            if i.y() + i.rect().y() + i.rect().height() > bottomRightY:
                bottomRightY = i.y() + i.rect().height() + i.rect().y()
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.bottomRightX = bottomRightX
        self.bottomRightY = bottomRightY
        super().__init__(self.topLeftX, self.topLeftY, self.bottomRightX - self.topLeftX,
                         self.bottomRightY - self.topLeftY)
        self.name = "Combination"
        self.itemSetting = []
        for i in self.itemList:
            newList = [(i.x() + i.rect().x() - self.topLeftX) / (self.bottomRightX - self.topLeftX),
                       (i.y() + i.rect().y() - self.topLeftY) / (self.bottomRightY - self.topLeftY),
                       i.rect().width() / (self.bottomRightX - self.topLeftX),
                       i.rect().height() / (self.bottomRightY - self.topLeftY)]
            self.itemSetting.append(newList)
        self.myPen(249,203,133)

    def paint_items(self, painter):
        l = self.rect().x()
        r = self.rect().y()
        w = self.rect().width()
        h = self.rect().height()
        for i in range(len(self.itemList)):
            if self.itemList[i].name == 'Circle':
                painter.drawEllipse(l + self.itemSetting[i][0] * w,
                                    r + self.itemSetting[i][1] * h,
                                    w * self.itemSetting[i][2],
                                    h * self.itemSetting[i][3])
            if self.itemList[i].name == 'Rectangle':
                painter.drawRect(l + self.itemSetting[i][0] * w,
                                 r + self.itemSetting[i][1] * h,
                                 w * self.itemSetting[i][2],
                                 h * self.itemSetting[i][3])
            if self.itemList[i].name == 'Line':
                painter.drawLine(l + self.itemSetting[i][0] * w,
                                 r + self.itemSetting[i][1] * h + h * self.itemSetting[i][3]/2,
                                 l + self.itemSetting[i][0] * w + w * self.itemSetting[i][2],
                                 r + self.itemSetting[i][1] * h + h * self.itemSetting[i][3]/2)
            if self.itemList[i].name == 'Triangle':
                painter.drawPolygon(QPolygon([QPoint(l + self.itemSetting[i][0] * w,
                                                     r + self.itemSetting[i][1] * h + h * self.itemSetting[i][3]),
                                              QPoint(l + self.itemSetting[i][0] * w + w * self.itemSetting[i][2],
                                                     r + self.itemSetting[i][1] * h + h * self.itemSetting[i][3]),
                                              QPoint(l + self.itemSetting[i][0] * w + w * self.itemSetting[i][2] / 2,
                                                     r + self.itemSetting[i][1] * h)]))

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(QColor(255, 255, 255, 0)))
        painter.setPen(self.pen)
        self.paint_items(painter)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        for handle, rect in self.handles.items():
            if self.handleSelected is None or handle == self.handleSelected:
                painter.drawRect(rect)
