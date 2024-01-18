![Screen](/voice_screen.png)
1. [Описание программы](#opis)
2. [Требования к конфигурации](#treb)
3. [Подключение к YandexSpeechKit](#yand)
4. [Установка программы](#nastr)
5. [Запуск программы](#pusk) 

# 1. Описание программы <a name='opis'></a>
The program allows you to conduct a voice dialogue of 2 people in different languages with online translation and voiceover into the language of the interlocutor.\
   Программа позволяет вести голосовой диалог 2-х человек на разных языках с онлайн переводом и озвучкой на язык собеседника.\
Перед началом работы сделать настройки: установить языки и голоса собеседников, указать время в секундах на фразу собеседника, настроить схему цикла работы программы. Запуск цикла - кнопка **`СТАРТ`**.\
**`Схема 111:`** распознавание с микрофона **`язык1`** в текст, перевод на **`язык2`**,
синтез речи на **`языке2`** и озвучка **`голосом2`**.\
Если активен **`второй себеседник`**, то произойдет распознавание с микрофона **`язык2`** в текст, перевод на **`язык1`**,
синтез речи на **`языке1`** и озвучка **`голосом1`**.

Частные случаи:\
**`Схема 210:`**
распознавание из аудио файлов форматов WAV, OGG и
даже Mp3! в текстовую строку.\
Скачал песню Toto Cutungo - Litaliano в формате Mp3. Поставил распознавание с италянского и перевод на русский. Сохранил протокол, оттуда скопировал в текстовый файл, разбил на строки, скачал перевод песни. Результаты работы - файл files/toto.txt. Результат - отрицательный, на троечку с огромным минусом(не распознан целый куплет).\
Взял файл попроще(русский шансон) - нормально, ошибок немного, оценил бы результат на 4.\
**`Схема 100:`**
Поднес микрофон к телевизору, результат на 5, получил стенограмму передачи:).\
**`Схема 010:`** перевод строки на другой язык; \
**`Схема 001:`** синтез речи из текста на разных языках и сохранение в WAV файл (files/audio_step3.wav).

# 2. Требования к конфигурации  <a name="treb"></a>
   ОС: проверялось на Linux Mint 20.3(base: Ubuntu 20.04) и на Windows 11.

   Python 3.10  
          (на Python3.11 версии не установился yandex-speechkit)  

   В программе использованы модули [YandexSpeechkit](https://cloud.yandex.ru/ru/docs/speechkit/) и модули создания/проверки токенов из программы `Вируальный дворецкий` от [ladykot](  https://github.com/ladykot/Butler).

# 3. Подключение к YandexSpeechKit <a name="yand"></a>

Программа написана с применением технологии
[Yandex SpeechKit](https://cloud.yandex.ru/ru/docs/speechkit/overview). Голосовые технологии Yandex SpeechKit помогают решить любую задачу, связанную с речью человека. SpeechKit может распознавать речь в режиме реального времени и из предварительно записанных аудиофайлов, автоматически определяя язык говорящего, а также озвучивать шаблонные фразы и развернутые тексты при помощи стандартных голосов SpeechKit.SpeechKit работает через интерфейсы API.

* Необходимо зарегистрироваться на [Yandex](https://yandex.ru/support/id/authorization/lite.html#lite__login-yandex) После регистрации получите грант на 60 дней.
* Необходимо создать [сервисный аккаунт](https://cloud.yandex.ru/ru/docs/iam/quickstart-sa). Сервисный аккаунт — аккаунт, от имени которого программы могут управлять ресурсами в Yandex Cloud
* назначить сервисному аккаунту [роли](https://cloud.yandex.ru/ru/docs/iam/operations/sa/assign-role-for-sa#cli_1):
>  ai.speechkit-stt.user ai.speechkit-tts.user ai.translate.user ai.viewer
speech-sense.viewer ai.languageModels.user
* сохранить folderid, api-key, oauth-token в файле переменных окружения `config.py`:
    
```Python    
# coding: utf-8
import os
def env_set():
    ''' Функция задает переменные окружения,
    чтобы использовать их в запросах к API YSK:
    oauth_token (str)
    id_folder (str)
    api_key (str)
'''
    os.environ["oauth_token"] = "y0_----Ваш oauth-token ---"
    os.environ["id_folder"] = "---Ваш folderId----"
    os.environ["api_key"] = "-----Ваш api-key----------------------"
    return True
```  

# 4. Установка программы <a name='nastr'></a>

## 4.1.  Создать папки для размещения ПО
  
  `cd <путь до Вашей папки>`  
  `mkdir voice`  папка с программами  
  `cd voice` зайти в созданную папку
  
  Скопируйте файлы:\
  requirements.txt - файл со списком необходимых модулей\
  voice_main.py - главная программа\
  voice_speech.py - модули распознавания и синтеза речи\
  voice_mic_text.py - модуль распознавания речи с микрофона\
  config.py  - файл с ключами и токенами. **`З а п о л н и т ь!!!`** (см разд.3)\
  voice_scr.py - модуль экрана программы(создан в Qt Designer)\
  
  `mkdir files` папка с времеными файлами (логи, протоколы, аудиофайла синтеза речи)

  `mkdir cloudapi` папка с файлами yandex-speechkit
  
  Файлы, создаваемые программой:\
  iam.txt - файл с iam-token\
  voice.ini - файл с сохраненными настройками (по кнопке "Сохранить настройки")\
  files/voice.log - лог-файл работы программы\
  files/audio_step1.wav - аудио файл создается на каждам цикле распознавания с микрофона(почему-то очень низкий уровень записи)\
  files/audio_step3.wav - аудио файл создается на каждом цикле синтеза речи \
  files/protocol.html - протокол беседы, дозаписывается по кнопке "Сохранить Протокол" 
  
## 4.2. Создать  создание виртуального окружения (virtual environment) для работы программы
На Linux:\
  `sudo apt-get install Python3.10` - установка python 3.10  
  `python3 -m venv voice_env` - установка виртуального окружения\
  `source voice_env/bin/activate` - активация виртуального окружения\

На Windows:\
  `<путь к python3.10>\python -m venv voice_env` - установка виртуального окружения\
В терминале:\
  `cd <путь до Вашей папки>`\
  `source voice_env/scripts/activate` - активация виртуального окружения\


  `pip install -r requirements.txt ` (рекомендуется) установка необходимого ПО

  Или:  
```
 pip install yandex-speechkit  
 sudo apt-get install libasound2-dev  
 pip install simpleaudio  
 pip install PyQt5
 sudo apt install portaudio19-dev
 pip install PyAudio
 pip install grpcio-tools
```

## 4.3. cloudapi
   [Потоковое распознавание речи](https://cloud.yandex.ru/ru/docs/speechkit/stt/api/microphone-streaming)   

## 5. Запук программы:   <a name='pusk'></a>

   `python3 voice_main.py` 
    
    
  
