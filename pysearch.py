import sys
from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('PySide2 WebEngineWidgets Example')

        self.toolBar = QToolBar()
        self.addToolBar(self.toolBar)

        self.backButton = QPushButton('<-')
        self.backButton.clicked.connect(self.back)
        self.toolBar.addWidget(self.backButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)

        self.backButton = QPushButton('새로고침')
        self.backButton.clicked.connect(self.back)
        self.toolBar.addWidget(self.backButton)

        self.qcomboBox = QComboBox() #
        #self.qcomboBox.addItem("Banana")  # 단일 아이템 추가시
        self.qcomboBox.addItems(["통합검색", "이미지검색", "쇼핑검색",'맞춤검색'])  # 다수 아이템 추가시
        self.qcomboBox.insertSeparator(2)  # 구분 선
        self.toolBar.addWidget(self.qcomboBox)


        self.addressLineEdit = QLineEdit()
        #self.addressLineEdit.setGeometry(10,10,200,200)
        self.addressLineEdit.returnPressed.connect(self.load)
        self.toolBar.addWidget(self.addressLineEdit)

        self.forwardButton = QPushButton('네이버',self)
        #self.forwardButton.('네이버')
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.forwardButton = QPushButton('구글',self)
        #self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.forwardButton = QPushButton('유튜브',self)
        #self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.forwardButton = QPushButton('인스타그램',self)
        #self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.forwardButton = QPushButton('다음', self)
        # self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.forwardButton = QPushButton('줌', self)
        # self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.forwardButton = QPushButton('도움말', self)
        # self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)

        #initialUrl = 'http://qt.io'
        initialUrl = "https://www.celebreview.kr/"

        self.addressLineEdit.setText('')
        self.webEngineView.load(QUrl(initialUrl))
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)



    def load(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        print(url)
        url1 = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + self.addressLineEdit.text()
        if url.isValid():
            self.webEngineView.load(url1)

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def urlChanged(self, url):
        self.addressLineEdit.setText(url.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    availableGeometry = app.desktop().availableGeometry(mainWin)
    mainWin.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3)
    mainWin.show()
    sys.exit(app.exec_())