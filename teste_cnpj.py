from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 125)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_cnpj = QLabel(self.centralwidget)
        self.lb_cnpj.setObjectName("lb_cnpj")
        self.lb_cnpj.setMinimumSize(QSize(0, 24))
        self.lb_cnpj.setMaximumSize(QSize(16777215, 24))
        font = QFont()
        font.setFamilies(["Segoe UI Semibold"])
        font.setPointSize(10)
        font.setBold(True)
        self.lb_cnpj.setFont(font)

        self.gridLayout.addWidget(self.lb_cnpj, 0, 0, 1, 1)

        self.bt_verificar = QPushButton(self.centralwidget)
        self.bt_verificar.setObjectName("bt_verificar")
        self.bt_verificar.setMinimumSize(QSize(0, 24))
        self.bt_verificar.setMaximumSize(QSize(16777215, 24))
        self.bt_verificar.setFont(font)

        self.gridLayout.addWidget(self.bt_verificar, 0, 2, 1, 1)

        self.txt_cnpj = QLineEdit(self.centralwidget)
        self.txt_cnpj.setObjectName("txt_cnpj")
        self.txt_cnpj.setMinimumSize(QSize(0, 24))
        self.txt_cnpj.setMaximumSize(QSize(16777215, 24))
        self.txt_cnpj.setFont(font)

        self.gridLayout.addWidget(self.txt_cnpj, 0, 1, 1, 1)

        self.lb_texto = QLabel(self.centralwidget)
        self.lb_texto.setObjectName("lb_texto")
        self.lb_texto.setFont(font)

        self.gridLayout.addWidget(self.lb_texto, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.lb_cnpj.setText(QCoreApplication.translate("MainWindow", "CNPJ:", None))
        self.bt_verificar.setText(
            QCoreApplication.translate("MainWindow", "Verificar", None)
        )
        self.txt_cnpj.setText("")
        self.lb_texto.setText(
            QCoreApplication.translate("MainWindow", "TextLabel", None)
        )


def validar_cnpj(cnpj):
    """Valida um CNPJ brasileiro.

    Args:
        cnpj (str): O CNPJ a ser validado.

    Returns:
        bool: True se o CNPJ é válido, False caso contrário.
    """

    cnpj = "".join([c for c in cnpj if c.isdigit()])

    if len(cnpj) != 14:
        return False

    if cnpj == cnpj[0] * 14:
        return False

    multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj_para_verificar = cnpj[:-2]

    for i in range(2):
        soma = 0
        for j, digito in enumerate(cnpj_para_verificar):
            soma += int(digito) * multiplicadores[j]
        resto = 11 - (soma % 11)
        if resto >= 10:
            resto = 0
        cnpj_para_verificar += str(resto)
        multiplicadores.insert(0, 6)

    return cnpj == cnpj_para_verificar


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.bt_verificar.clicked.connect(self.verificar_cnpj)
        self.txt_cnpj.editingFinished.connect(self.verificar_cnpj)

    def verificar_cnpj(self):
        """Valida o CNPJ inserido pelo usuário e exibe a mensagem correspondente."""
        cnpj = self.txt_cnpj.text()
        cnpj = "".join([c for c in cnpj if c.isdigit()])
        if validar_cnpj(cnpj):
            cnpj_formatado = (
                f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
            )
            self.lb_texto.setText(f"O CNPJ {cnpj_formatado} é válido.")
        else:
            self.lb_texto.setText(f"O CNPJ {cnpj} é inválido.")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
