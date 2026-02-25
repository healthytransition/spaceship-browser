from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class Browser(QMainWindow):
def __init__(self):
super().__init__()
self.browser = QWebEngineView()
self.browser.setUrl(QUrl("https://google.com"))
self.setCentralWidget(self.browser)

navbar = QToolBar()
self.addToolBar(navbar)

back = QAction("←", self)
back.triggered.connect(self.browser.back)
navbar.addAction(back)

forward = QAction("→", self)
forward.triggered.connect(self.browser.forward)
navbar.addAction(forward)

self.url_bar = QLineEdit()
self.url_bar.returnPressed.connect(self.navigate)
navbar.addWidget(self.url_bar)

self.browser.urlChanged.connect(lambda q: self.url_bar.setText(q.toString()))

def navigate(self):
url = self.url_bar.text()
if not url.startswith("http"):
url = "https://" + url
self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())