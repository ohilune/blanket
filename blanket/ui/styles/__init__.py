from fileinput import close

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from pathlib import Path
import logging


class BlanketQSS(object):
    BLENDER = 'blender'

    def __init__(self):
        pass

    @classmethod
    def apply(cls, app: QApplication, style: str):
        stylesheet_path = Path(__file__).parent / style / 'style.qss'
        icon_path = Path(__file__).parent / style / 'icon.png'
        image_directory = str(Path(__file__).parent / style / 'images')
        QDir.addSearchPath('images', image_directory)

        if icon_path.exists():
            app.setWindowIcon(QIcon(str(icon_path)))
        else:
            logging.warning(f'Icon not found: {icon_path}')

        if stylesheet_path.exists():
            app.setStyleSheet(stylesheet_path.read_text())
        else:
            logging.warning(f'Theme not found: {stylesheet_path}')
