import sys
import random
#from PySide6 import QtCore, QtWidgets, QtGui
#from __future__ import annotations

#hello world appliation
'''
class SirWidgetTheFirst(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hello", "Hi", "Sup", "Hello cruel world", "Wotcha", "Howdy", "Greetings mortal"]

        self.button = QtWidgets.QPushButton("I like to be clicked")
        self.text = QtWidgets.QLabel("Hello cruel world", alignment=QtCore.Qt.AlignCenter)
        self.text2 = QtWidgets.QLabel("this button also exists for some reason")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = SirWidgetTheFirst()
    widget.resize(800,400)
    widget.show()

    sys.exit(app.exec())

'''

#button layout


from PySide6.QtCore import QSizeF, Qt
from PySide6.QtWidgets import (QApplication, QGraphicsAnchorLayout, QGraphicsProxyWidget,
                               QGraphicsScene, QGraphicsView, QGraphicsWidget,
                               QPushButton, QSizePolicy)

def create_item(minimum, prefered, maximum, name):
    #           size format[horizontal],[vertical] name is just a string
    w = QGraphicsProxyWidget()

    w.setWidget(QPushButton(name))
    w.setMinimumSize(minimum)
    w.setMaximumSize(maximum)
    w.setPreferredSize(prefered)
    w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    #                   horizontal policy              vertical policy

    return w

if __name__ == '__main__':
    app = QApplication(sys.argv)

    scene = QGraphicsScene()
    scene.setSceneRect(0, 0, 800, 480)
    #                          W   H

    min_size = QSizeF(30, 100)
    pref_size = QSizeF(210, 100)
    max_size = QSizeF(300, 100)

    #formatting for buttons:
    #button_name = create_item(QSizeF(float,float),QSizeF(float,float),QSizeF(float,float),"name")
    #                            min size           pref size            max size           name

    button_exp_red = create_item(min_size, pref_size, max_size, "export Red channel")
    button_exp_green = create_item(min_size, pref_size, max_size, "export Green channel")
    button_exp_blue = create_item(min_size, pref_size, max_size, "export Blue channel")
    button_exp_alpha = create_item(min_size, pref_size, max_size, "export Alpha channel")

    button_exp_ORMA = create_item(min_size, pref_size, max_size, "export channel packed texture")

    button_imp_red = create_item(min_size, pref_size, max_size, "import Red channel")
    button_imp_green = create_item(min_size, pref_size, max_size, "import Green channel")
    button_imp_blue = create_item(min_size, pref_size, max_size, "import Blue channel")
    button_imp_alpha = create_item(min_size, pref_size, max_size, "import Alpha channel")

    button_imp_ORMA = create_item(min_size, pref_size, max_size, "import channel packed texture")

    #l for layout
    l = QGraphicsAnchorLayout()
    l.setSpacing(1)
    
    #w for window
    w = QGraphicsWidget(None, Qt.WindowType.Window)
    w.setPos(20,20)
    w.setLayout(l)

    #vertical
    #format:
    #l.addAncor(first item/button, first edge, second item(usually l), second edge)
    l.addAnchor(button_exp_red, Qt.AnchorPoint.AnchorTop, l, Qt.AnchorPoint.AnchorTop)
    l.addAnchor(button_imp_red, Qt.AnchorPoint.AnchorTop, l, Qt.AnchorPoint.AnchorTop)



    scene.addItem(w)
    scene.setBackgroundBrush(Qt.GlobalColor.darkCyan)

    view = QGraphicsView(scene)
    view.show()

    sys.exit(app.exec())


