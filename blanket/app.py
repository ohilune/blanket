import ctypes
import sys
from pathlib import Path
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from blanket.core import config
from blanket.ui.main import BlanketMainWindow
from blanket.ui.styles import BlanketQSS


class BlanketApplication(QApplication):
    def __init__(self):
        super(BlanketApplication, self).__init__()
        self.setApplicationName('Blanket')
        self.setEffectEnabled(Qt.UIEffect.UI_AnimateCombo, False)

        self.config = config.load_config()

        # フォントファイルを追加
        font_path = Path(__file__).parent / 'ui' / 'resources' / 'fonts' / 'Inter' / 'Inter-Regular.ttf'
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        print(font_id)
        if font_id == -1:
            print(f'Font loading failed from path: {font_path}')
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(f'Loaded font family: {font_family}')

        BlanketQSS.apply(self, BlanketQSS.BLENDER)

        self.main_window = BlanketMainWindow(self.config)
        self.main_window.show()

        print(f'MainWindow font family: {self.main_window.font().family()}')


if __name__ == '__main__':
    app_id = 'ohilune.blanket.0.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    app = BlanketApplication()
    sys.exit(app.exec())
