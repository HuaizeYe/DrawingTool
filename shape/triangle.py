from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QPen, QColor, QBrush, QPainter, Qt, QPolygonF, QPolygon
from PySide6.QtWidgets import QGraphicsItem, QGraphicsEllipseItem
from shape.base import Base


class Triangle(Base):
    def __init__(self, *args):
        super().__init__(*args)
        self.name = "Triangle"
        self.myPen(145,203,125)
        self.points = QPolygon([QPoint(self.rect().left(),self.rect().bottom()),
                           QPoint(self.rect().right(),self.rect().bottom()),
                           QPoint(self.rect().left()+self.rect().width()/2,self.rect().top())])

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(QColor(255, 255, 255,0)))
        painter.setPen(self.pen)
        self.points = QPolygon([QPoint(self.rect().left(),self.rect().bottom()),
                           QPoint(self.rect().right(),self.rect().bottom()),
                           QPoint(self.rect().left()+self.rect().width()/2,self.rect().top())])
        painter.drawPolygon(self.points)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        for handle, rect in self.handles.items():
            if self.handleSelected is None or handle == self.handleSelected:
                painter.drawRect(rect)



