# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(600, 459)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(60, 70, 271, 361))
        self.frame_1.setStyleSheet("#frame_1{\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"background-image:url(:/img/icon/background.jpg);\n"
"background-repeat: no-repeat;\n"
"background-size: cover; \n"
"background-position: center; \n"
"}")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.label = QtWidgets.QLabel(self.frame_1)
        self.label.setGeometry(QtCore.QRect(10, 90, 251, 31))
        self.label.setStyleSheet("color:rgb(217, 217, 217);\n"
"font: 24pt \"Adobe 黑体 Std R\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_1)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 251, 91))
        self.label_2.setStyleSheet("color:rgb(217, 217, 217);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 70, 221, 361))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 221, 351))
        self.frame_3.setStyleSheet("#frame_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"    border-top:3px solid blue;\n"
"    border-right:3px solid qlineargradient(spread:pad, x1:1, y1:1, x2:0.994, y2:0, stop:0.0454545 rgba(255, 0, 0, 255), stop:0.931818 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"    border-bottom:3px solid red;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.fram_3 = QtWidgets.QFrame(self.frame_3)
        self.fram_3.setGeometry(QtCore.QRect(0, 40, 221, 261))
        self.fram_3.setMinimumSize(QtCore.QSize(221, 261))
        self.fram_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fram_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fram_3.setObjectName("fram_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fram_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.fram_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255,0);\n"
"border:none;\n"
"border-bottom:1px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"padding-right:5px;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_login = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_login.setStyleSheet("")
        self.stackedWidget_login.setObjectName("stackedWidget_login")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_r_account = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_r_account.setObjectName("lineEdit_r_account")
        self.verticalLayout_6.addWidget(self.lineEdit_r_account)
        self.lineEdit_r_pwd = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_r_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_r_pwd.setObjectName("lineEdit_r_pwd")
        self.verticalLayout_6.addWidget(self.lineEdit_r_pwd)
        self.lineEdit_r_pwd2 = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_r_pwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_r_pwd2.setObjectName("lineEdit_r_pwd2")
        self.verticalLayout_6.addWidget(self.lineEdit_r_pwd2)
        self.pushButton_r_register = QtWidgets.QPushButton(self.page_login)
        self.pushButton_r_register.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_r_register.setObjectName("pushButton_r_register")
        self.verticalLayout_6.addWidget(self.pushButton_r_register)
        self.stackedWidget_login.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_register)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_account = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_account.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.verticalLayout_5.addWidget(self.lineEdit_account)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_pwd.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.verticalLayout_5.addWidget(self.lineEdit_pwd)
        self.pushButton_sure = QtWidgets.QPushButton(self.page_register)
        self.pushButton_sure.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.verticalLayout_5.addWidget(self.pushButton_sure)
        self.stackedWidget_login.addWidget(self.page_register)
        self.page_getback = QtWidgets.QWidget()
        self.page_getback.setObjectName("page_getback")
        self.page_getback_2 = QtWidgets.QVBoxLayout(self.page_getback)
        self.page_getback_2.setObjectName("page_getback_2")
        self.lineEdit_g_account = QtWidgets.QLineEdit(self.page_getback)
        self.lineEdit_g_account.setObjectName("lineEdit_g_account")
        self.page_getback_2.addWidget(self.lineEdit_g_account)
        self.lineEdit_g_pwd = QtWidgets.QLineEdit(self.page_getback)
        self.lineEdit_g_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_g_pwd.setObjectName("lineEdit_g_pwd")
        self.page_getback_2.addWidget(self.lineEdit_g_pwd)
        self.lineEdit_g_pwd2 = QtWidgets.QLineEdit(self.page_getback)
        self.lineEdit_g_pwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_g_pwd2.setObjectName("lineEdit_g_pwd2")
        self.page_getback_2.addWidget(self.lineEdit_g_pwd2)
        self.pushButton_g_getback = QtWidgets.QPushButton(self.page_getback)
        self.pushButton_g_getback.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_g_getback.setObjectName("pushButton_g_getback")
        self.page_getback_2.addWidget(self.pushButton_g_getback)
        self.stackedWidget_login.addWidget(self.page_getback)
        self.verticalLayout_4.addWidget(self.stackedWidget_login)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_login.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_login.setIcon(icon)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.pushButton_register = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_register.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/icon/register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_register.setIcon(icon1)
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout.addWidget(self.pushButton_register)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_g = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_g.setStyleSheet("#pushButton_getback{background-color:rgb(0, 0, 0)\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_g.setObjectName("pushButton_g")
        self.verticalLayout_7.addWidget(self.pushButton_g)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_5)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(170, 10, 41, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px;\n"
"\n"
"}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 310, 219, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget_message = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget_message.setObjectName("stackedWidget_message")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_message.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_message = QtWidgets.QLabel(self.page_2)
        self.label_message.setText("")
        self.label_message.setObjectName("label_message")
        self.horizontalLayout_2.addWidget(self.label_message)
        self.stackedWidget_message.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget_message)
        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)
        self.stackedWidget_login.setCurrentIndex(2)
        self.stackedWidget_message.setCurrentIndex(1)
        self.pushButton.clicked.connect(loginWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(loginWindow)
        loginWindow.setTabOrder(self.pushButton_register, self.pushButton)
        loginWindow.setTabOrder(self.pushButton, self.lineEdit_account)
        loginWindow.setTabOrder(self.lineEdit_account, self.lineEdit_pwd)
        loginWindow.setTabOrder(self.lineEdit_pwd, self.pushButton_sure)
        loginWindow.setTabOrder(self.pushButton_sure, self.lineEdit_r_account)
        loginWindow.setTabOrder(self.lineEdit_r_account, self.lineEdit_r_pwd)
        loginWindow.setTabOrder(self.lineEdit_r_pwd, self.lineEdit_r_pwd2)
        loginWindow.setTabOrder(self.lineEdit_r_pwd2, self.pushButton_r_register)
        loginWindow.setTabOrder(self.pushButton_r_register, self.pushButton_login)
        loginWindow.setTabOrder(self.pushButton_login, self.lineEdit_g_account)
        loginWindow.setTabOrder(self.lineEdit_g_account, self.lineEdit_g_pwd)
        loginWindow.setTabOrder(self.lineEdit_g_pwd, self.lineEdit_g_pwd2)
        loginWindow.setTabOrder(self.lineEdit_g_pwd2, self.pushButton_g_getback)
        loginWindow.setTabOrder(self.pushButton_g_getback, self.pushButton_g)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "登录窗口"))
        self.label.setText(_translate("loginWindow", "  防溺水预警系统"))
        self.label_2.setText(_translate("loginWindow", "            畅游未来，安全先行"))
        self.lineEdit_r_account.setPlaceholderText(_translate("loginWindow", "请输入账号:"))
        self.lineEdit_r_pwd.setPlaceholderText(_translate("loginWindow", "请输入密码:"))
        self.lineEdit_r_pwd2.setPlaceholderText(_translate("loginWindow", "确认密码:"))
        self.pushButton_r_register.setText(_translate("loginWindow", "注册"))
        self.lineEdit_account.setPlaceholderText(_translate("loginWindow", "请输入账号:"))
        self.lineEdit_pwd.setPlaceholderText(_translate("loginWindow", "请输入密码:"))
        self.pushButton_sure.setText(_translate("loginWindow", "确认登录"))
        self.lineEdit_g_account.setPlaceholderText(_translate("loginWindow", "请输入账号:"))
        self.lineEdit_g_pwd.setPlaceholderText(_translate("loginWindow", "请输入密码:"))
        self.lineEdit_g_pwd2.setPlaceholderText(_translate("loginWindow", "确认密码:"))
        self.pushButton_g_getback.setText(_translate("loginWindow", "重置"))
        self.pushButton_g.setText(_translate("loginWindow", "重置密码"))
import apprcc_rc
