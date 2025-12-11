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

#button layout test

'''
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

'''

#box layout test

from PySide6.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QCheckBox)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spider's Channel Packing Tool")

        '''#---testing layout

        #hbox layout
        layout = QHBoxLayout()
        imps = QVBoxLayout()
        exps = QVBoxLayout()

        #adds widgets
        imps.addWidget(QPushButton("import Red Channel"))
        imps.addWidget(QPushButton("import green Channel"))
        imps.addWidget(QPushButton("import blue Channel"))
        imps.addWidget(QPushButton("import alpha Channel"))

        exps.addWidget(QPushButton("export Red Channel"))
        exps.addWidget(QPushButton("export green Channel"))
        exps.addWidget(QPushButton("export blue Channel"))
        exps.addWidget(QPushButton("export alpha Channel"))

        #containers
        container1 = QWidget()
        container1.setLayout(imps)
        container2 = QWidget()
        container2.setLayout(exps)

        layout.addWidget(container1)
        layout.addWidget(container2)

        #sets layout on the application
        #self.setLayout(layout)
        '''

        #-----------------Final Layout-----------------

        seperateChans = QVBoxLayout()
        packedChans = QVBoxLayout()

        #makes the RGBA channels as boxes
        def MakeChannel(name):
            channel = QVBoxLayout()
            channel.addWidget(QPushButton("REPLACE ME WITH THE IMAGE"))#need to figure out adding images above these
            channel.addWidget(QPushButton("import "+name+" texture"))
            channel.addWidget(QPushButton("export "+name+" texture"))

            container = QWidget()
            container.setLayout(channel)

            return container#returns the created layout as a container
        
        #---------------------v-Seperate Channels-v------------------------

        #RGBA as containers
        red = MakeChannel(name="red")
        green = MakeChannel(name="green")
        blue = MakeChannel(name="blue")
        alpha = MakeChannel(name="alpha")

        #Add containers to Vertical layout
        seperateChans.addWidget(red)
        seperateChans.addWidget(green)
        seperateChans.addWidget(blue)
        seperateChans.addWidget(alpha)

        #---------------------^-Seperate Channels-^------------------------

        #----------------------v-PACKED Channels-v-------------------------

        #RGBA as containers
        RGBA = MakeChannel(name="packed")

        #Add containers to Vertical layout
        packedChans.addWidget(RGBA)

        #----------------------^-PACKED Channels-^-------------------------

        #-------------------------v-Settings-v----------------------------

        settings = QVBoxLayout()
        settings.addWidget(QPushButton("Pack Textures\n --> "))
        settings.addWidget(QPushButton("Unpack Textures\n <-- "))
        settings.addWidget(QCheckBox("Use Alpha"))


        #-------------------------^-Settings-^----------------------------

        #collums
        col1 = QWidget()
        col1.setLayout(seperateChans)#seperate channels

        col2 = QWidget()
        col2.setLayout(settings)#settings collum

        col3 = QWidget()
        col3.setLayout(packedChans)#packed texture

        #master layout
        Mlayout = QHBoxLayout()
        Mlayout.addWidget(col1,1)#numbers represent importance for scaling
        Mlayout.addWidget(col2,0)
        Mlayout.addWidget(col3,2)

        self.setLayout(Mlayout)
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
