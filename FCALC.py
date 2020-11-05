import wolframalpha
import sys
from PyQt5 import QtWidgets
import dialog

client = wolframalpha.Client('#API')


class ExampleApp(QtWidgets.QMainWindow, dialog.Ui_Dialog):

    def button_click(self):
        mes = self.lineEdit.text()
        print(mes)
        res = client.query(mes)

        rez = next(res.results).text
        print(rez)

        self.lineEdit.setText(rez)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_click)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
