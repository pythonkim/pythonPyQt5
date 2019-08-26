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
        self.backButton.clicked.connect(self.reload)
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

        self.sButton01 = QPushButton('네이버',self)
        #self.forwardButton.('네이버')
        self.sButton01.clicked.connect(self.button_clicked)
        self.toolBar.addWidget(self.sButton01)

        self.sButton02 = QPushButton('구글',self)
        #self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.sButton02.clicked.connect(self.button_clicked)
        self.toolBar.addWidget(self.sButton02)

        self.sButton03 = QPushButton('유튜브',self)
        #self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.sButton03.clicked.connect(self.button_clicked)
        self.toolBar.addWidget(self.sButton03)

        self.sButton04 = QPushButton('인스타그램',self)
        #self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.sButton04.clicked.connect(self.button_clicked)
        self.toolBar.addWidget(self.sButton04)

        self.sButton05 = QPushButton('다음', self)
        # self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.sButton05.clicked.connect(self.button_clicked)
        self.toolBar.addWidget(self.sButton05)

        self.sButton06 = QPushButton('줌', self)
        # self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.sButton06.clicked.connect(self.button_clicked)
        self.toolBar.addWidget(self.sButton06)

        self.sButton07 = QPushButton('도움말', self)
        # self.forwardButton.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.sButton07.clicked.connect(self.button_clicked)
        self.toolBar.addWidget(self.sButton07)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)

        initialUrl = "https://www.naver.com/"

        self.addressLineEdit.setText('')
        self.webEngineView.load(QUrl(initialUrl))
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)


    def load(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        print(url)
        url1 = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + self.addressLineEdit.text()
        if url.isValid():
            self.webEngineView.load(url1)
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload) #이렇게 하면 새로고침이 되네

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back) #뒤로가기

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward) #앞으로



    def button_clicked(self):
        url = ""
        search_keyword = self.addressLineEdit.text()
        search_engine = self.sender().text()
        if search_engine == '네이버':
            url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + search_keyword
            self.webEngineView.load(url) #보여줘라
            if url.isValid():
                self.webEngineView.load('https://www.naver.com')
        elif search_engine == '구글':
            url = "https://www.google.com/search?newwindow=1&hl=ko&source=hp&ei=pcpjXe78KpG7wAPP8biACA&q=" + search_keyword
            self.webEngineView.load(url)
            if not search_keyword:
                self.webEngineView.load('https://www.google.com')
        elif search_engine == '유튜브':
            url = "https://www.youtube.com/results?search_query=" + search_keyword
            self.webEngineView.load(url)
            if not search_keyword:
                self.webEngineView.load('https://www.youtube.com/')

        elif search_engine == '인스타그램':
            url = "https://www.instagram.com/explore/tags/" + search_keyword
            self.webEngineView.load(url)
            if not search_keyword:
                self.webEngineView.load('https://www.instagram.com/')

        elif search_engine == '다음':
            url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=" + search_keyword
            self.webEngineView.load(url)
            if not search_keyword:
                self.webEngineView.load('https://www.daum.net/')

        elif search_engine == '줌':
            url = "http://search.zum.com/search.zum?method=uni&option=accu&rd=1&qm=f_typing.top&query=" + search_keyword
            self.webEngineView.load(url)
            if not search_keyword:
                self.webEngineView.load('http://zum.com')
        elif search_engine == '도움말':
            url = "https://styleranker.co.kr"
            self.webEngineView.load(url)




        print(search_engine)
        self.curCat = self.sender().text()
        print(self.curCat)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    availableGeometry = app.desktop().availableGeometry(mainWin)
    mainWin.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3)
    mainWin.show()
    sys.exit(app.exec_())