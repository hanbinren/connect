# coding: utf-8
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from login import session
import ftrack_api.entity.location
import ftrack_api.structure.origin
import ftrack_api.accessor.disk
import ftrack_api


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Connect")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(325, 275, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(225, 275, 75, 23))
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(310, 15, 75, 23))
        self.pushButton2.setObjectName("pushButton2")

        self.textEteil1 = QtWidgets.QTableWidget(Dialog)
        self.textEteil1.setGeometry(QtCore.QRect(15, 40, 370, 220))
        self.textEteil1.setObjectName('textEteil1')
        self.textEteil1.setShowGrid(True)

        projects = session.query('Project')
        for project in projects:
            i = len(project['name'])
        self.textEteil1.setRowCount(i)
        self.textEteil1.setColumnCount(2)
        self.textEteil1.setHorizontalHeaderLabels(['Name', 'Type'])
        self.textEteil1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.textEteil1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.textEteil1.setSelectionBehavior(QAbstractItemView.SelectRows)


        self.textEteil = QtWidgets.QLineEdit(Dialog)
        self.textEteil.setGeometry(QtCore.QRect(15, 15, 260, 23))
        self.textEteil.setObjectName('textEteil')
        self.textEteil.setPlaceholderText('Ftrack')
        self.textEteil.setReadOnly(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connect"))
        self.pushButton.setText(_translate("Dialog", "退出"))

        # Dialog.setWindowTitle(_translate('Dialog','Connect'))
        self.pushButton1.setText(_translate('Dialog','确定'))

        # Dialog.setWindowTitle(_translate('Dialog', 'Connect'))
        self.pushButton2.setText(_translate('Dialog', '返回上一级'))


