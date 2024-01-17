#!/usr/bin/env python
# coding: utf-8
'''
The program allows you to conduct a voice dialogue
of 2 people in different languages with online
translation and voiceover into the language of
the interlocutor.
Программа позволяет вести диалог 2-х человек на
разных языках с онлайн переводом на язык собеседника.
Также можно переводить аудио файлы форматов WAV, PCM, OGG и
даже Mp3! в текст.
Author: Krasavcev V.N.
'''

import os
import sys
import subprocess
import time
# import threading
# import json
import logging
# import requests
from PyQt5 import QtWidgets, QtCore, QtGui
import voice_scr

if os.name == 'nt':
    otvet = subprocess.run(
            ['ping', '-n', '1', 'ya.ru'],
            stdout=subprocess.DEVNULL, check=False)
else:
    otvet = subprocess.run(
            ['ping', '-c', '1', 'ya.ru'],
            stdout=subprocess.DEVNULL, check=False)
if otvet.returncode == 0:
    print('Есть Интерент')
else:
    print('!!!!!!! Отсутствует Internet !!!!!!!!!!')
    sys.exit()

import voice_speech as sp
import voice_mic_text
from importlib import reload

#  запишем в логи информацию о токенах:
log_format = '%(asctime)s - %(message)s'
logging.basicConfig(filename=r'files/voice.log',
                    format=log_format,
                    level=logging.INFO)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class MyWindow(QtWidgets.QWidget, voice_scr.Ui_Form):
    """Основной экран программы.
    Назначается цикл работы программы(распознавание-перевод-
    синтез речи) По кнопке СТАРТ запускается выполнение.
    Меняете активного собеседника и запускаете следующий цикл. и т.д
    """
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.lst_lng = [
             'ru-RU русский язык', 'de-DE немецкий',
             'en-US английский', 'es-ES испанский',
             'fi-FI финский', 'fr-FR французский',
             'he-HE иврит', 'it-IT итальянский',
             'kk-KZ казахский', 'nl-NL голландский', 'pl-PL польский',
             'pt-PT португальский', 'pt-BR бразильский португальский',
             'sv-SE шведский', 'tr-TR турецкий', 'uz-UZ узбекский (латиница)'
        ]
        self.lst_voice = {
             'de-DE': ['lea'],
             'en-US': ['john'],
             'he-IL': ['naomi modern', 'naoimi classic'],
             'kk-KK': ['amira', 'madi'],
             'ru-RU': [
                      'alena neutral', 'alena good', 'filipp',
                      'ermil neutral', 'ermil good', 'jane neutral',
                      'jane good', 'jane evil', 'madirus',
                      'omazh neutral', 'omazh evil',
                      'zahar neutral', 'zahar good',
                      'dasha neutral', 'dasha good', 'dasha friendly',
                      'julia neutral', 'julia strict',
                      'lera neutral', 'lera friendly',
                      'masha good', 'masha strict', 'masha friendly',
                      'marina neutral', 'marina whisper', 'marina friendly',
                      'alexander neutral', 'alexander good',
                      'kirill neutral', 'kirill strict', 'kirill good',
                      'anton neutral', 'anton good'],
             'uz-UZ': ['nigora']
        }
        self.sp_btn_akt = 'background-color: green;\nborder : 3px solid black;\
                          \nborder-radius : 10px;'
        self.sp_btn_pas = 'background-color: white;\nborder : 2px solid black;\
                          \nborder-radius : 10px;'
        self.cur_file_input, self.cur_lng1, self.cur_voice1, self.cur_lng2, \
            self.cur_voice2, self.step1, self.step2, \
            self.step3 = self.rest_parametrs()
        self.str1, self.lng1, self.str2, self.lng2 = '', '', '', ''
        self.thread1 = ''
        self.setWindowTitle('Voice Translator V 1.0.0')
        self.timer_id = 0
        self.cur_time = self.mic_time.value()
        self.lcdNumber.display(self.cur_time)
        self.lbl_prot = QtWidgets.QLabel('')
        self.lbl_prot.setTextFormat(1)
        self.lbl_file_input.setText(self.cur_file_input)
        self.cmb1.addItems(self.lst_lng)
        self.cmb1.setCurrentText(self.cur_lng1)
        self.cmb1.currentIndexChanged.connect(self.change_lng1)
        if self.cur_lng1[0:5] in self.lst_voice:
            self.cmb2.addItems(self.lst_voice[self.cur_lng1[0:5]])
        self.cmb2.setCurrentText(self.cur_voice1)
        self.cmb3.addItems(self.lst_lng)
        self.cmb3.setCurrentText(self.cur_lng2)
        self.cmb3.currentIndexChanged.connect(self.change_lng2)
        if self.cur_lng2[0:5] in self.lst_voice:
            self.cmb4.addItems(self.lst_voice[self.cur_lng2[0:5]])
        self.cmb4.setCurrentText(self.cur_voice2)
        self.btn_file_open.clicked.connect(self.open_file_to_speech)
        self.st1_0.toggled.connect(self.change_step1)
        self.st1_1.toggled.connect(self.change_step1)
        self.st1_2.toggled.connect(self.change_step1)
        self.st2_0.toggled.connect(self.change_step2)
        self.st2_1.toggled.connect(self.change_step2)
        self.st3_0.toggled.connect(self.change_step3)
        self.st3_1.toggled.connect(self.change_step3)
        self.st3_2.toggled.connect(self.change_step3)
        self.radio_btn1.toggled.connect(self.change_radio)
        self.radio_btn2.toggled.connect(self.change_radio)
        if self.step1 == '0':
            self.st1_0.setChecked(True)
        elif self.step1 == '1':
            self.st1_1.setChecked(True)
        else:
            self.st1_2.setChecked(True)
        if self.step2 == '0':
            self.st2_0.setChecked(True)
        else:
            self.st2_1.setChecked(True)
        if self.step3 == '0':
            self.st3_0.setChecked(True)
        elif self.step3 == '1':
            self.st3_1.setChecked(True)
        else:
            self.st3_2.setChecked(True)
        self.radio_btn1.setChecked(True)
        self.btn_start.clicked.connect(self.start)
        self.btn_save_prot.clicked.connect(self.save_protocol)
        self.btn_save.clicked.connect(self.save_parametrs)
        self.btn_esc.clicked.connect(self.run_esc)
        self.btn_exit.clicked.connect((QtWidgets.qApp.quit))

    def change_step1(self):
        """изменение радио кнопки на 1 шаге"""
        if self.st1_0.isChecked():
            self.st1_0.setStyleSheet(self.sp_btn_akt)
            self.st1_1.setStyleSheet(self.sp_btn_pas)
            self.st1_2.setStyleSheet(self.sp_btn_pas)
            self.step1 = '0'
        elif self.st1_1.isChecked():
            self.st1_0.setStyleSheet(self.sp_btn_pas)
            self.st1_1.setStyleSheet(self.sp_btn_akt)
            self.st1_2.setStyleSheet(self.sp_btn_pas)
            self.step1 = '1'
        else:
            self.st1_0.setStyleSheet(self.sp_btn_pas)
            self.st1_1.setStyleSheet(self.sp_btn_pas)
            self.st1_2.setStyleSheet(self.sp_btn_akt)
            self.step1 = '2'

    def change_step2(self):
        """изменение радио кнопки на 2 шаге"""
        if self.st2_0.isChecked():
            self.st2_0.setStyleSheet(self.sp_btn_akt)
            self.st2_1.setStyleSheet(self.sp_btn_pas)
            self.step2 = '0'
        else:
            self.st2_0.setStyleSheet(self.sp_btn_pas)
            self.st2_1.setStyleSheet(self.sp_btn_akt)
            self.step2 = '1'

    def change_step3(self):
        """изменение радио кнопки на 3 шаге"""
        if self.st3_0.isChecked():
            self.st3_0.setStyleSheet(self.sp_btn_akt)
            self.st3_1.setStyleSheet(self.sp_btn_pas)
            self.st3_2.setStyleSheet(self.sp_btn_pas)
            self.step3 = '0'
        elif self.st3_1.isChecked():
            self.st3_0.setStyleSheet(self.sp_btn_pas)
            self.st3_1.setStyleSheet(self.sp_btn_akt)
            self.st3_2.setStyleSheet(self.sp_btn_pas)
            self.step3 = '1'
        else:
            self.st3_0.setStyleSheet(self.sp_btn_pas)
            self.st3_1.setStyleSheet(self.sp_btn_pas)
            self.st3_2.setStyleSheet(self.sp_btn_akt)
            self.step3 = '2'

    def change_radio(self):
        """изменение радио кнопки активного собеседника"""
        if self.radio_btn1.isChecked():
            self.radio_btn1.setStyleSheet(self.sp_btn_akt)
            self.radio_btn2.setStyleSheet(self.sp_btn_pas)
        else:
            self.radio_btn1.setStyleSheet(self.sp_btn_pas)
            self.radio_btn2.setStyleSheet(self.sp_btn_akt)

    def change_lng1(self):
        """изменение списка доступных голосов при изменении языка"""
        self.cur_lng1 = self.cmb1.currentText()
        self.cmb2.clear()
        if self.cur_lng1[0:5] == 'he-HE':
            self.cmb2.addItems(self.lst_voice['he-IL'])
        if self.cur_lng1[0:5] in self.lst_voice:
            self.cmb2.addItems(self.lst_voice[self.cur_lng1[0:5]])

    def change_lng2(self):
        """изменение списка доступных голосов при изменении языка"""
        self.cur_lng2 = self.cmb3.currentText()
        self.cmb4.clear()
        if self.cur_lng2[0:5] == 'he-HE':
            self.cmb4.addItems(self.lst_voice['he-IL'])
        if self.cur_lng2[0:5] in self.lst_voice:
            self.cmb4.addItems(self.lst_voice[self.cur_lng2[0:5]])

    def open_file_to_speech(self):
        """выбор файла для распознавания"""
        file_txt = QtWidgets.QFileDialog.getOpenFileName(
                   parent=window,
                   caption='Выберите аудио файл для распознавания',
                   filter='All (*);;Audio (*.wav *.ogg *.mp3 *.pcm)',
                   initialFilter='Audio (*.wav *.ogg *.mp3 *.pcm)')
        file_txt = file_txt[0]
        self.lbl_file_input.setText(file_txt)
        self.lbl_file_input.show()

    def on_change(self, kod_signal, lbl_s):
        """обновление экрана по сигналам из потока"""
        if kod_signal == 0:    # печать изменеия в строке статуса
            self.lbl_stat.setText(lbl_s)
        if kod_signal in (1, 6):      # получена строки с микрофона/файла
            self.str1 = lbl_s
            if self.radio_btn1.isChecked():
                self.te_pers1.setText(self.str1)
                cursor = self.te_pers1.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                self.te_pers1.setTextCursor(cursor)
                if kod_signal == 1:
                    self.lbl_prot.setText(
                        f'{self.lbl_prot.text()} <p>P1: {self.str1}</p>')
            else:
                self.te_pers2.setText(self.str1)
                cursor = self.te_pers2.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                self.te_pers2.setTextCursor(cursor)
                if kod_signal == 1:
                    self.lbl_prot.setText(
                        f'{self.lbl_prot.text()} <p>P2: {self.str1}</p>')
            self.sc_prot.setWidget(self.lbl_prot)
            self.sc_prot.verticalScrollBar().setValue(10000)
        elif kod_signal == 2:     # получена переведенная строка
            self.str2 = lbl_s
            if self.radio_btn1.isChecked():
                self.te_pers2.setText(self.str2)
                self.lbl_prot.setText(
                    self.lbl_prot.text() + '<p><b>P1: ' + self.str1 +
                    '</b><br>' + ' <span style="color:red">' + self.str2 +
                    '</span>' + '</p>')
                self.sc_prot.setWidget(self.lbl_prot)
            else:
                self.te_pers1.setText(self.str2)
                self.lbl_prot.setText(
                    self.lbl_prot.text() + '<p><b>   P2: ' +
                    self.str1 + '</b><br>' +
                    ' <span style="color:green">' + self.str2 +
                    '</span>' + '</p>')
                self.sc_prot.setWidget(self.lbl_prot)
            logging.info('Перевод строки на %s', self.lng1)
        elif kod_signal == 3:
            self.progress_bar.setValue(int(lbl_s))
        elif kod_signal == 4:
            self.lbl_stat.setText(lbl_s)
            QtWidgets.QMessageBox.information(
                      window, 'Предупреждение', lbl_s,
                      buttons=QtWidgets.QMessageBox.Ok)
        elif kod_signal == 5:
            self.killTimer(self.timer_id)
            self.timer_id = 0

    def timerEvent(self, event):
        """таймер"""
        self.cur_time -= 1
        self.lcdNumber.display(self.cur_time)

    def run_esc(self):
        """Прерывание потоков"""
        self.thread1.terminate()
        self.killTimer(self.timer_id)
        self.timer_id = 0
        self.lbl_stat.setText('Выполнение прервано. Жду дальнейших указаний')

    def start(self):
        """формирование переменных и создание потока"""
        if self.radio_btn1.isChecked():
            self.str1 = self.te_pers1.toPlainText()
            self.lng1 = self.cmb1.currentText()[0:5]
            self.lng2 = self.cmb3.currentText()[0:5]
            self.str2 = self.te_pers2.toPlainText()
            if self.step2 == '1':
                per1 = self.cmb4.currentText().split()
            else:
                per1 = self.cmb2.currentText().split()
        else:
            self.str1 = self.te_pers2.toPlainText()
            self.lng1 = self.cmb3.currentText()[0:5]
            self.lng2 = self.cmb1.currentText()[0:5]
            self.str2 = self.te_pers1.toPlainText()
            if self.step2 == '1':
                per1 = self.cmb2.currentText().split()
            else:
                per1 = self.cmb4.currentText().split()
        path2 = r'files/audio_step3.wav'
        voice, role = '', ''
        if len(per1) > 0:
            voice = per1[0]
        if len(per1) > 1:
            role = per1[1]
        if self.step1 == '1':
            self.cur_time = self.mic_time.value()
            self.timer_id = self.startTimer(
                1000, timerType=QtCore.Qt.VeryCoarseTimer)
        self.thread1 = ThreadVoice(
                       self.step1, self.step2, self.step3,
                       self.lbl_file_input.text(), self.str1, self.lng1,
                       self.str2, path2, self.lng2, voice, role,
                       str(self.mic_time.value()))
        self.thread1.signal_lbl_stat.connect(
             self.on_change, QtCore.Qt.QueuedConnection)
        self.thread1.start()

    def save_protocol(self):
        """сохранение протокола беседы в файл"""
        with open(r'files/protocol.html', 'a', encoding="utf-8") as f_pr:
            f_pr.write(f'\n===== Дата: {time.asctime()} =====\n')
            f_pr.write(self.lbl_prot.text())
        f_pr.close()

    def save_parametrs(self):
        """сохранение параметров в INI файле"""
        self.save_p.setValue('cur_file_input', self.lbl_file_input.text())
        self.save_p.setValue('cur_lng1', self.cmb1.currentText())
        self.save_p.setValue('cur_voice1', self.cmb2.currentText())
        self.save_p.setValue('cur_lng2', self.cmb3.currentText())
        self.save_p.setValue('cur_voice2', self.cmb4.currentText())
        self.save_p.setValue('cur_step1', self.step1)
        self.save_p.setValue('cur_step2', self.step2)
        self.save_p.setValue('cur_step3', self.step3)
        self.save_p.setValue('cur_mic_time', self.mic_time.value())
        self.save_p.sync()

    def rest_parametrs(self):
        """восстановление параметров из INI файла"""
        self.save_p = QtCore.QSettings('voice.ini', 1)
        if self.save_p.contains('cur_file_input'):
            self.cur_file_input = self.save_p.value('cur_file_input')
        else:
            self.cur_file_input = 'Файл не выбран'
        if self.save_p.contains('cur_lng1'):
            self.cur_lng1 = self.save_p.value('cur_lng1')
        else:
            self.cur_lng1 = 'ru-RU русский язык'
        if self.save_p.contains('cur_voice1'):
            self.cur_voice1 = self.save_p.value('cur_voice1')
        else:
            self.cur_voice1 = 'alena neutral'
        if self.save_p.contains('cur_lng2'):
            self.cur_lng2 = self.save_p.value('cur_lng2')
        else:
            self.cur_lng2 = 'en-US английский'
        if self.save_p.contains('cur_voice2'):
            self.cur_voice2 = self.save_p.value('cur_voice2')
        else:
            self.cur_voice2 = 'john'
        if self.save_p.contains('cur_step1'):
            self.step1 = self.save_p.value('cur_step1')
        else:
            self.step1 = '1'
        if self.save_p.contains('cur_step2'):
            self.step2 = self.save_p.value('cur_step2')
        else:
            self.step2 = '1'
        if self.save_p.contains('cur_step3'):
            self.step3 = self.save_p.value('cur_step3')
        else:
            self.step3 = '1'
        if self.save_p.contains('cur_mic_time'):
            self.mic_time.setValue(int(self.save_p.value('cur_mic_time')))
        else:
            self.mic_time.setValue(10)
        return self.cur_file_input, self.cur_lng1, self.cur_voice1, \
            self.cur_lng2, self.cur_voice2, self.step1, \
            self.step2, self.step3


class ThreadVoice(QtCore.QThread):
    """ класс работы в потоке.
    Выполняется цикл Распознавание - перевод - синтез речи.
    Связь с главной программой осуществляется через сигналы.
    """
    signal_lbl_stat = QtCore.pyqtSignal(int, str)

    def __init__(self, step1, step2, step3, path1, str1, lng1, str2, path2,
                 lng2, voice, role, mic_time, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.step1 = step1
        self.step2 = step2
        self.step3 = step3
        self.str1 = str1
        self.lng1 = lng1
        self.path1 = path1
        self.str2 = str2
        self.lng2 = lng2
        self.path2 = path2
        self.voice = voice
        self.role = role
        self.mic_time = mic_time

    def run(self):
        """ Пошагово (распознавание-перевод-синтез речи)
        вызываются программы распознаваниия(с микрофона или файла),
        перевода, синтеза и аудио воспроизведения текста"""
        if self.step1 == '1':
            reload(voice_mic_text)
            self.signal_lbl_stat.emit(
                0, 'Распознавание с микрофона. ГОВОРИТЕ!! Speak up!!')
            self.str1 = voice_mic_text.run(
                sp.api_key, self.lng1,
                int(self.mic_time), self.signal_lbl_stat)
#            subprocess.run([
#                'python3', 'voice_mic_text.py', '--secret',
#                sp.api_key, '--lng', self.lng1, '--mic',
#                self.mic_time], check=False)
#            with open(r'files/voice_str.txt', 'r', encoding="utf-8") as f_str:
#                self.str1 = f_str.read()
            self.signal_lbl_stat.emit(1, self.str1)
            self.signal_lbl_stat.emit(5, 'Прерывание таймера')
        if self.step1 == '2':
            self.signal_lbl_stat.emit(0, 'Распознавание из файла')
            self.str1 = sp.audio_f_to_str(self.path1, self.lng1)
            self.signal_lbl_stat.emit(1, self.str1)
        if self.step2 == '1':
            self.signal_lbl_stat.emit(0, 'Перевод текста')
            print('str1-trans', self.str1, len(self.str1))
            if len(self.str1) == 0:
                self.signal_lbl_stat.emit(
                    4, 'Перевод.Строка для перевода пустая')
                self.str2 = ''
            else:
                self.str2 = sp.trans_text(self.str1, self.lng2[0:2])
            self.signal_lbl_stat.emit(2, self.str2)
            logging.info('Строка переведена ')
        if self.step3 in ('1', '2'):
            self.signal_lbl_stat.emit(0, 'Создание аудио файла')
#            sp.str_to_audio_f(self.str2, self.lng2)
            if self.step2 == '1':
                if len(self.str2) == 0:
                    self.signal_lbl_stat.emit(
                        4, 'Синтез речи.Строка для озвучки пустая')
                else:
                    sp.str_to_audio_sdk(self.str2, self.path2, self.lng2[0:2],
                                        self.voice, self.role)
            else:
                if len(self.str1) == 0:
                    self.signal_lbl_stat.emit(
                        4, 'Синтез речи.Строка для озвучки пустая')
                else:
                    sp.str_to_audio_sdk(self.str1, self.path2, self.lng1[0:2],
                                        self.voice, self.role)
            logging.info('Создан аудио файл ')
            if self.step3 == '1':
                time.sleep(1)
                self.signal_lbl_stat.emit(0, 'Озвучка текста')
                sp.sound(self.path2)
                logging.info('Озвучен аудио файл ')
        self.signal_lbl_stat.emit(
                0, 'Процесс завершен. Жду дальнейших указаний')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
