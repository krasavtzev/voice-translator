# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voice_scr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1039, 824)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.person1 = QtWidgets.QLabel(Form)
        self.person1.setGeometry(QtCore.QRect(210, 140, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.person1.setFont(font)
        self.person1.setObjectName("person1")
        self.person1_2 = QtWidgets.QLabel(Form)
        self.person1_2.setGeometry(QtCore.QRect(600, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.person1_2.setFont(font)
        self.person1_2.setObjectName("person1_2")
        self.cmb1 = QtWidgets.QComboBox(Form)
        self.cmb1.setGeometry(QtCore.QRect(135, 180, 181, 24))
        self.cmb1.setCurrentText("")
        self.cmb1.setMaxVisibleItems(3)
        self.cmb1.setObjectName("cmb1")
        self.cmb2 = QtWidgets.QComboBox(Form)
        self.cmb2.setGeometry(QtCore.QRect(320, 180, 121, 24))
        self.cmb2.setObjectName("cmb2")
        self.cmb3 = QtWidgets.QComboBox(Form)
        self.cmb3.setGeometry(QtCore.QRect(495, 180, 171, 24))
        self.cmb3.setObjectName("cmb3")
        self.cmb4 = QtWidgets.QComboBox(Form)
        self.cmb4.setGeometry(QtCore.QRect(680, 180, 171, 24))
        self.cmb4.setObjectName("cmb4")
        self.btn_save_prot = QtWidgets.QPushButton(Form)
        self.btn_save_prot.setGeometry(QtCore.QRect(170, 770, 151, 51))
        self.btn_save_prot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save_prot.setObjectName("btn_save_prot")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(350, 770, 151, 51))
        self.btn_save.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save.setObjectName("btn_save")
        self.btn_esc = QtWidgets.QPushButton(Form)
        self.btn_esc.setGeometry(QtCore.QRect(530, 770, 151, 51))
        self.btn_esc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_esc.setObjectName("btn_esc")
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(710, 770, 151, 51))
        self.btn_exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_exit.setObjectName("btn_exit")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(310, 560, 421, 61))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.radio_btn1 = QtWidgets.QRadioButton(self.groupBox)
        self.radio_btn1.setGeometry(QtCore.QRect(20, 20, 161, 31))
        self.radio_btn1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radio_btn1.setFont(font)
        self.radio_btn1.setStyleSheet("border : 3px solid black;\n"
"border-radius : 10px;")
        self.radio_btn1.setObjectName("radio_btn1")
        self.radio_btn2 = QtWidgets.QRadioButton(self.groupBox)
        self.radio_btn2.setGeometry(QtCore.QRect(250, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radio_btn2.setFont(font)
        self.radio_btn2.setStyleSheet("border : 3px solid black;\n"
"border-radius : 10px;")
        self.radio_btn2.setObjectName("radio_btn2")
        self.sc_prot = QtWidgets.QScrollArea(Form)
        self.sc_prot.setGeometry(QtCore.QRect(30, 210, 971, 231))
        self.sc_prot.setWidgetResizable(True)
        self.sc_prot.setObjectName("sc_prot")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 969, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sc_prot.setWidget(self.scrollAreaWidgetContents)
        self.lbl_scheme = QtWidgets.QLabel(Form)
        self.lbl_scheme.setGeometry(QtCore.QRect(160, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_scheme.setFont(font)
        self.lbl_scheme.setObjectName("lbl_scheme")
        self.te_pers1 = QtWidgets.QTextEdit(Form)
        self.te_pers1.setGeometry(QtCore.QRect(40, 480, 471, 75))
        self.te_pers1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.te_pers1.setObjectName("te_pers1")
        self.te_pers2 = QtWidgets.QTextEdit(Form)
        self.te_pers2.setGeometry(QtCore.QRect(520, 480, 471, 75))
        self.te_pers2.setObjectName("te_pers2")
        self.btn_file_open = QtWidgets.QPushButton(Form)
        self.btn_file_open.setGeometry(QtCore.QRect(30, 670, 121, 41))
        self.btn_file_open.setObjectName("btn_file_open")
        self.lbl_file_input = QtWidgets.QLabel(Form)
        self.lbl_file_input.setGeometry(QtCore.QRect(20, 720, 441, 20))
        self.lbl_file_input.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lbl_file_input.setObjectName("lbl_file_input")
        self.lbl_stat0 = QtWidgets.QLabel(Form)
        self.lbl_stat0.setGeometry(QtCore.QRect(320, 745, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_stat0.setFont(font)
        self.lbl_stat0.setScaledContents(True)
        self.lbl_stat0.setObjectName("lbl_stat0")
        self.lbl_stat = QtWidgets.QLabel(Form)
        self.lbl_stat.setGeometry(QtCore.QRect(410, 750, 571, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_stat.setFont(font)
        self.lbl_stat.setStyleSheet("border-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 245, 201);")
        self.lbl_stat.setObjectName("lbl_stat")
        self.btn_start = QtWidgets.QPushButton(Form)
        self.btn_start.setGeometry(QtCore.QRect(460, 620, 100, 100))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"color: rgb(0,0,0);  \n"
"border-radius: 50px;  border: 2px groove gray;\n"
"font: 14pt \"AcadEref\";\n"
"border-style: outset;")
        self.btn_start.setObjectName("btn_start")
        self.vgp_1 = QtWidgets.QGroupBox(Form)
        self.vgp_1.setGeometry(QtCore.QRect(20, 30, 312, 121))
        self.vgp_1.setStyleSheet("border-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 245, 201);")
        self.vgp_1.setObjectName("vgp_1")
        self.vbox_st1 = QtWidgets.QVBoxLayout(self.vgp_1)
        self.vbox_st1.setObjectName("vbox_st1")
        self.st1_0 = QtWidgets.QRadioButton(self.vgp_1)
        self.st1_0.setObjectName("st1_0")
        self.vbox_st1.addWidget(self.st1_0)
        self.st1_1 = QtWidgets.QRadioButton(self.vgp_1)
        self.st1_1.setObjectName("st1_1")
        self.vbox_st1.addWidget(self.st1_1)
        self.st1_2 = QtWidgets.QRadioButton(self.vgp_1)
        self.st1_2.setObjectName("st1_2")
        self.vbox_st1.addWidget(self.st1_2)
        self.vgp_2 = QtWidgets.QGroupBox(Form)
        self.vgp_2.setGeometry(QtCore.QRect(350, 30, 312, 121))
        self.vgp_2.setStyleSheet("border-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 245, 201);")
        self.vgp_2.setObjectName("vgp_2")
        self.vbox_st2 = QtWidgets.QVBoxLayout(self.vgp_2)
        self.vbox_st2.setObjectName("vbox_st2")
        self.st2_0 = QtWidgets.QRadioButton(self.vgp_2)
        self.st2_0.setObjectName("st2_0")
        self.vbox_st2.addWidget(self.st2_0)
        self.st2_1 = QtWidgets.QRadioButton(self.vgp_2)
        self.st2_1.setObjectName("st2_1")
        self.vbox_st2.addWidget(self.st2_1)
        self.vgp_3 = QtWidgets.QGroupBox(Form)
        self.vgp_3.setGeometry(QtCore.QRect(680, 30, 312, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.vgp_3.setFont(font)
        self.vgp_3.setAutoFillBackground(False)
        self.vgp_3.setStyleSheet("border-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 245, 201);")
        self.vgp_3.setObjectName("vgp_3")
        self.vbox_st3 = QtWidgets.QVBoxLayout(self.vgp_3)
        self.vbox_st3.setContentsMargins(1, 1, -1, -1)
        self.vbox_st3.setObjectName("vbox_st3")
        self.st3_0 = QtWidgets.QRadioButton(self.vgp_3)
        self.st3_0.setObjectName("st3_0")
        self.vbox_st3.addWidget(self.st3_0)
        self.st3_1 = QtWidgets.QRadioButton(self.vgp_3)
        self.st3_1.setObjectName("st3_1")
        self.vbox_st3.addWidget(self.st3_1)
        self.st3_2 = QtWidgets.QRadioButton(self.vgp_3)
        self.st3_2.setObjectName("st3_2")
        self.vbox_st3.addWidget(self.st3_2)
        self.mic = QtWidgets.QLabel(Form)
        self.mic.setGeometry(QtCore.QRect(530, 10, 181, 20))
        self.mic.setObjectName("mic")
        self.mic_time = QtWidgets.QSpinBox(Form)
        self.mic_time.setGeometry(QtCore.QRect(730, 10, 61, 26))
        self.mic_time.setMinimum(3)
        self.mic_time.setMaximum(300)
        self.mic_time.setObjectName("mic_time")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(470, 450, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setWhatsThis("")
        self.lcdNumber.setStyleSheet("background-color: rgb(199, 255, 208);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setMidLineWidth(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_timer = QtWidgets.QLabel(Form)
        self.label_timer.setGeometry(QtCore.QRect(130, 450, 351, 20))
        self.label_timer.setObjectName("label_timer")
        self.cmb1.raise_()
        self.person1.raise_()
        self.person1_2.raise_()
        self.cmb2.raise_()
        self.cmb3.raise_()
        self.cmb4.raise_()
        self.btn_save_prot.raise_()
        self.btn_save.raise_()
        self.btn_esc.raise_()
        self.btn_exit.raise_()
        self.groupBox.raise_()
        self.sc_prot.raise_()
        self.lbl_scheme.raise_()
        self.te_pers1.raise_()
        self.te_pers2.raise_()
        self.btn_file_open.raise_()
        self.lbl_file_input.raise_()
        self.lbl_stat0.raise_()
        self.lbl_stat.raise_()
        self.btn_start.raise_()
        self.vgp_1.raise_()
        self.vgp_2.raise_()
        self.vgp_3.raise_()
        self.mic.raise_()
        self.mic_time.raise_()
        self.lcdNumber.raise_()
        self.label_timer.raise_()

        self.retranslateUi(Form)
        self.cmb1.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Voice translator V 1.0"))
        self.person1.setText(_translate("Form", "Собеседник 1"))
        self.person1_2.setText(_translate("Form", "Собеседник 2"))
        self.cmb1.setToolTip(_translate("Form", "Выбор языка 1-го собеседника"))
        self.cmb2.setToolTip(_translate("Form", "<html><head/><body><p>Выбор голоса и роли (при воспроизведении текста) 1-го собеседника</p></body></html>"))
        self.cmb3.setToolTip(_translate("Form", "Выбор языка 2-го собеседника"))
        self.cmb4.setToolTip(_translate("Form", "Выбор голоса и роли (при воспроизведении текста) 2-го собеседника"))
        self.btn_save_prot.setToolTip(_translate("Form", "Сохранить протокол беседы в текстовый файл"))
        self.btn_save_prot.setText(_translate("Form", "Сохранить Протокол"))
        self.btn_save.setToolTip(_translate("Form", "Сохрагить выбранную схему, языки, роли"))
        self.btn_save.setText(_translate("Form", "Сохранить настройки"))
        self.btn_esc.setToolTip(_translate("Form", "Прервать цикл работы по схеме"))
        self.btn_esc.setText(_translate("Form", "Прервать"))
        self.btn_exit.setToolTip(_translate("Form", "Выход из программы"))
        self.btn_exit.setText(_translate("Form", "Выход"))
        self.groupBox.setTitle(_translate("Form", "Активный пользователь"))
        self.radio_btn1.setText(_translate("Form", "Собеседник 1"))
        self.radio_btn2.setText(_translate("Form", "Собеседник 2"))
        self.lbl_scheme.setText(_translate("Form", "Схема работы:"))
        self.btn_file_open.setToolTip(_translate("Form", "Окно выбора аудио файла(используется если значенеие  первого этапа > 1)"))
        self.btn_file_open.setText(_translate("Form", "Открыть файл\n"
" для распознавания"))
        self.lbl_file_input.setText(_translate("Form", "TextLabel"))
        self.lbl_stat0.setText(_translate("Form", "СТАТУС:"))
        self.lbl_stat.setText(_translate("Form", "Установка параметров. Ожидание Старта"))
        self.btn_start.setToolTip(_translate("Form", "<html><head/><body><p>Запуск цикла работы Speechkit по указанной схеме</p></body></html>"))
        self.btn_start.setText(_translate("Form", "СТАРТ!"))
        self.vgp_1.setTitle(_translate("Form", "Шаг 1"))
        self.st1_0.setText(_translate("Form", "0. Распознавание аудио не производить"))
        self.st1_1.setToolTip(_translate("Form", "<html><head/><body><p>Производится распознавание звука с микрофона и запись в текстовую строку. Таймер показывает оставшееся время на фразу. </p></body></html>"))
        self.st1_1.setText(_translate("Form", "1. Произвести распознавание с микрофона"))
        self.st1_2.setToolTip(_translate("Form", "Берется файл из \"Открыть файл для распознавания\". Файл д.б. формата wav,ogg,pcm или mp3"))
        self.st1_2.setText(_translate("Form", "2. Произвести распознавание из аудиофайла"))
        self.vgp_2.setTitle(_translate("Form", "Шаг 2"))
        self.st2_0.setText(_translate("Form", "0. Перевод выполнять не надо"))
        self.st2_1.setToolTip(_translate("Form", "Осуществляется перевод строки с языка активного пользователя на язык второг собеседника."))
        self.st2_1.setText(_translate("Form", "1. Сделать перевод строки"))
        self.vgp_3.setTitle(_translate("Form", "Шаг 3"))
        self.st3_0.setText(_translate("Form", "0. Распознавание аудио не производить"))
        self.st3_1.setToolTip(_translate("Form", "Результат сохраняется в files/audio_step3.wav. На каждом цикле файл создается по новой. Если он Вам нужен - успейте скопировать в другое место."))
        self.st3_1.setText(_translate("Form", "1. Произвести синтез речи и воспроизвести"))
        self.st3_2.setToolTip(_translate("Form", "Результат сохраняется в files/audio_step3.wav. На каждом цикле файл создается по новой. Если он Вам нужен - успейте скопировать в другое место."))
        self.st3_2.setText(_translate("Form", "2. Провести синтез речи в файл"))
        self.mic.setToolTip(_translate("Form", "От 3 до 300 сек."))
        self.mic.setText(_translate("Form", "Время работы микрофона:"))
        self.mic_time.setToolTip(_translate("Form", "От 3 до 300 сек."))
        self.lcdNumber.setToolTip(_translate("Form", "Таймер оставшегося времени активности микрофона"))
        self.label_timer.setText(_translate("Form", "Таймер оставшегося времени активности микрофона-"))
