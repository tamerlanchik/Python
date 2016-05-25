import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt
import random as r

class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        #self.setFixedSize(500, 500)
        #self.move(self.size().width()//2, self.size().height()//2)
        self.resize(500, 500)
        '''qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())'''
        self.move(300, 300)
        
        self.setWindowTitle('ds')
        self.show()
        
        
    def paintEvent(self, e):
        qp=QPainter()
        qp.begin(self)
        self.draws(qp)
        qp.end()
        
    def draws(self, qp):
        size=self.size()
        qp.setPen(Qt.gray)
        for i in range(26, size.width()-20, size.width()//30):
            qp.drawLine(i, size.height()//30, i, size.height()-30)
            
        for i in range(26, size.height()-20, size.height()//30):
                qp.drawLine(size.width()//30, i, size.width()-30, i)
        
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(size.width()//2, size.height()//30, size.width()//2, size.height()-20)
        qp.drawLine(size.width()//30, size.height()//2, size.width()-20, size.height()//2)
        
        a=[Qt.black, Qt.red, Qt.darkRed, Qt.green, Qt.blue, Qt.darkBlue, Qt.cyan, Qt.darkCyan, Qt.magenta, Qt.yellow]
        #qp.setPen(a[r.randint(0, 8)])
        for _ in range(5000):
            qp.setPen(a[r.randint(0, 9)])
            qp.drawLine(r.randint(0, size.width()), r.randint(0, size.height()), r.randint(0, size.width()), r.randint(0, size.height()) )
            qp.setPen(a[r.randint(0, 9)])
            qp.drawEllipse(r.randint(0, size.width()), r.randint(0, size.height()), r.randint(0, 120), r.randint(0, 120) )
        
        '''brush=QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 30, 400, 400)'''   
        
app=QApplication(sys.argv)
ex=Display()
sys.exit(app.exec_())
