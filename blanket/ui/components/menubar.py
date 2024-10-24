from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ファイルメニューの作成
        file_menu = self.addMenu('Project')

        # '新規プロジェクト' アクションを作成
        new_project_action = QAction('New Project', self)
        new_project_action.triggered.connect(self.on_new_project)
        file_menu.addAction(new_project_action)

        # '新規プロジェクト' アクションを作成
        open_project_action = QAction('Open Project', self)
        open_project_action.triggered.connect(self.on_new_project)
        file_menu.addAction(open_project_action)

        # '終了' アクションを作成
        exit_action = QAction('Close', self)
        exit_action.triggered.connect(self.on_exit)
        file_menu.addAction(exit_action)

        # 編集メニューの作成
        edit_menu = self.addMenu('Assets')
        undo_action = QAction('元に戻す', self)
        edit_menu.addAction(undo_action)

        # ヘルプメニューの作成
        help_menu = self.addMenu('Help')
        about_action = QAction('このソフトについて', self)
        help_menu.addAction(about_action)

    def on_new_project(self):
        print('新規プロジェクト作成')

    def on_exit(self):
        print('アプリケーション終了')
        self.parent().close()
