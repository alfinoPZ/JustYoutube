import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class YoutubeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(900, 300, 600, 500)
        self.setWindowTitle('YouTube Viewer')
        self.resize(False, False)
        self.centralWidget()

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.search_input = QLineEdit(self)
        search_button = QPushButton('Pesquisar', self)
        search_button.clicked.connect(self.search_youtube)
        search_button.setStyleSheet("background-color: #3498db; color: white;")

        layout.addWidget(self.search_input)
        layout.addWidget(search_button)
        main_widget.setStyleSheet("background-color: #f0f0f0;")

        self.web_view = QWebEngineView(self)
        layout.addWidget(self.web_view)

    def search_youtube(self):
        search_query = self.search_input.text()

        search_url = QUrl(f"https://www.youtube.com/results?search_query={search_query}")
        self.web_view.setUrl(search_url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YoutubeViewer()
    ex.show()
    sys.exit(app.exec_())