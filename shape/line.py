from PySide6.QtCore import QLine
from PySide6.QtGui import QPen, QColor, QBrush, QPainter, Qt
from PySide6.QtWidgets import QGraphicsItem, QGraphicsEllipseItem
from shape.base import Base


class Line(Base):
    def __init__(self, *args):
        super().__init__(*args)
        self.name = "Line"
        self.angle = 0
        self.myPen(45,53,225)

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(QColor(255, 255, 255,0)))
        painter.setPen(self.pen)
        line = QLine(self.rect().x(),self.rect().y()+self.rect().height()/2,self.rect().right(),self.rect().y()+self.rect().height()/2)
        painter.drawLine(line)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        for handle, rect in self.handles.items():
            if self.handleSelected is None or handle == self.handleSelected:
                painter.drawRect(rect)



