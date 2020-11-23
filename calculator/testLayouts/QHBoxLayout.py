import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
layout = QHBoxLayout() # set the layout variable
layout.addWidget(QPushButton('Left')) # create buttons
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout) # set the layout to the layout variable
window.show()
sys.exit(app.exec_())
