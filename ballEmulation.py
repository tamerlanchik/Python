import time
import math
import sys
import random

from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPainter, QBrush, QPen, QPalette
from PyQt5.QtCore import Qt, QPoint, QTimer
Ww=1000
Hw=600
N=2
a=(0, 10)
bordH=10

bord1=(0, 0)
bord2=(0, 0)
T=0.1
balls=[0]*N
#balls[0]=[400, 100, 20, 0.1, 0, 0.1]
#balls[1]=[500, 100, 20, -0.1, 0, 0.2]

for i in range(N):
    R=random.randint(1, 10)
    x=random.randint(0, Ww)
    y=random.randint(0, Hw)
    vX=random.randint(-30, 30)/10
    vY=random.randint(-30, 30)/10
    weight=random.randint(0, 10000)/1000  
    balls[i]=[x, y, R, vX, vY, weight]
    print(balls[i])


class Phys():
    def __init__(self):
        print("Module Phys iitialisated")
    def recalc(self):
        global balls
        for i in range(N):
            x, y, R=balls[i][0:3]
            if bord1[1]+bordH//2+1>=y-R or bord2[1]+bordH//2-1<=y+R:
                balls[i][4]*=-1
            if bord1[0]+bordH//2+1>=x-R or bord2[0]+bordH//2-1<=x+R:
                balls[i][3]*=-1
            balls[i][4]+=T*a[1]*0.001
            balls[i][3]+=T*a[0]*0.001
                
            balls[i][0]+=balls[i][3]
            balls[i][1]+=balls[i][4]
            
            if bord1[1]+bordH//2+1>=balls[i][1]-R:
                balls[i][1]=bord1[1]+bordH//2+1
            elif bord2[1]+bordH//2-1<=balls[i][1]+R:
                balls[i][1]=bord2[1]+bordH//2-1
            if bord1[0]+bordH//2+1>=balls[i][0]-R:
                balls[i][0]=bord1[0]+bordH//2+1
            elif bord2[0]+bordH//2-1<=balls[i][0]+R:
                balls[i][0]=bord2[0]+bordH//2-1
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.display=Display()
        self.setCentralWidget(self.display)
        self.resize(Ww, Hw)
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())
        
        self.setWindowTitle('Phys')
        self.show()
        
        
        
class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.sqrSize=15
        self.setFixedHeight(600)
        self.setFixedWidth(1000)
        global bord1, bord2
        Pal=QPalette()
        Pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(Pal)
        self.painter=QPainter(self)

        bord1=(10,10)
        bord2=(self.width()-30, self.height()-30)        
        
        self.tmr=QTimer()
        self.tmr.setInterval(T)
        self.tmr.timeout.connect(self.moveB)
        self.tmr.start()
    
    def paintEvent(self, e):
        pen1=QPen(Qt.black, bordH)
        pen2=QPen(Qt.red, 1)
        self.painter.begin(self)        
        self.painter.setPen(Qt.gray)
        self.drawGrid()
        self.painter.setPen(pen1)
        
        self.painter.drawRect(10, 10, self.width()-30, self.height()-30)
        
        self.painter.setPen(pen2)
        self.painter.setBrush(Qt.red)
        for i in range(N):
            self.painter.drawEllipse(QPoint(balls[i][0], balls[i][1]), balls[i][2], balls[i][2]) 
        self.painter.end()
    def moveB(self):
        Phys.recalc(Phys)
        self.update()
    def drawGrid(self):
        for i in range(self.sqrSize, max(self.width(), self.height()), self.sqrSize):
            self.painter.drawLine(i, 0, i, self.height())
            self.painter.drawLine(0, i, self.width(), i)
            


if __name__=="__main__":
    app=QApplication(sys.argv)
    gui=Window()
    phys=Phys()
    sys.exit(app.exec_())
