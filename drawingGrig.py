size=self.size()
        qp.setPen(Qt.gray)
        for i in range(26, size.width()-20, size.width()//30):
            qp.drawLine(i, size.height()//30, i, size.height()-30)
            
        for i in range(26, size.height()-20, size.height()//30):
                qp.drawLine(size.width()//30, i, size.width()-30, i)
