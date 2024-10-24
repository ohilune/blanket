from logging import basicConfig, getLogger, DEBUG
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from blanket.ui.components.menubar import MenuBar

logger = getLogger(__name__)
basicConfig(level=DEBUG)


class BlanketMainWindow(QMainWindow):
    def __init__(self, config, parent=None):
        super().__init__(parent)

        self.config = config

        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)
