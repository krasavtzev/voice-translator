# coding: utf-8

import os
import json
import logging
import requests
import simpleaudio as sa
from config import env_set
from pydub import AudioSegment
from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType
import pyaudio
import wave
import grpc
import yandex.cloud.ai.stt.v3.stt_pb2 as stt_pb2
import yandex.cloud.ai.stt.v3.stt_service_pb2_grpc as stt_service_pb2_grpc

log_format = '%(asctime)s - %(message)s'
logging.basicConfig(filename=r'files/voice.log',
                    format=log_format,
                    level=logging.INFO)
# Настройки потокового распознавания.
FORMAT = pyaudio.paInt16

CHANNELS = 1
RATE = 8000
CHUNK = 4096
WAVE_OUTPUT_FILENAME = r'files/audio_step1.wav'

audio = pyaudio.PyAudio()

URL = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
URL_REC = 'https://stt.api.cloud.yandex.net/speech/v1/stt:recognize'
URL_SYN = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
URL_TRANSL = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
URL_TOKENS = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
file_token = 'iam.txt'

if env_set():  # задаем переменные окружения
    oauth_token = os.environ['oauth_token']  # и кладем их в рабочие переменные
    id_folder = os.environ['id_folder']
    api_key = os.environ['api_key']

configure_credentials(
    yandex_credentials=creds.YandexCredentials(api_key=api_key))


def sound(trek):
    """ функция проигрывания аудио
    :param: trek (wav)
    """
    wave_obj = sa.WaveObject.from_wave_file(trek)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def write_token(iam_new):
    """ Функция записывает новый iam токен в файл
    :param iam_new: (str)
    """
    with open(file_token, 'w') as f:
        f.write(iam_new)


def create_new_token():
    """ Функция генерирует новый токен обменом oauth_token на iam-токен
    и записывет в iam.txt
    :return: iam_new (str)
    """
    logging.info('Время iam_token истекло. Отправка запроса ...')
    params = {'yandexPassportOauthToken': oauth_token}
    # указали oauth_token в параметрах запроса
    response = requests.post(URL_TOKENS,
                             params=params)
    decode_response = response.content.decode('UTF-8')  # декодируем бинарник
    text = json.loads(decode_response)  # загружаем в json
    iam_new = text.get('iamToken')  # iam_token << json по ключу iamToken
    expires_iam_token = text.get('expiresAt')

    write_token(iam_new)
    logging.info("Новый iam-токен успешно сгенерирован. "
                 f"Срок жизни: до {expires_iam_token}")
    return iam_new


def get_token():
    """ Функция проверяет работоспособность iam-токен.
    Если при попытке аторизации c iam-токен приходит ошибка,
    то генерируется и записывается в файл новый iam-токен
    вызовом функции create_token().
    """
    if os.path.exists(file_token):  # если уже получали токен и файл существует
        with open(file_token, 'r') as f:
            iam = f.read()
            headers = {'Authorization': f'Bearer {iam}'}
            data = {'text': "проверка",
                    'lang': 'ru-RU',
                    'folderId': id_folder}
            resp = requests.post(URL_SYN, headers=headers, data=data)

            if resp.status_code == 200:
                logging.info('iam-токен еще действует')
                return iam
            else:
                return create_new_token()
    else:  # если файла c iam-токеном еще не существует
        iam_new = create_new_token()
        write_token(iam_new)
        return iam_new


def audio_f_to_str(audio, lng):
    """ синхронное распознавания речи из аудиофайла
        с помощью Python SDK SpeechKit"""
    # https://cloud.yandex.ru/docs/speechkit/sdk/python/request
    # Аутентификация через API-ключ.

    model = model_repository.recognition_model()

    # Задайте настройки распознавания.
    model.model = 'general'
    model.language = lng
    model.audio_processing_type = AudioProcessingType.Full
    # AudioProcessingType.Stream — для потокового распознавания;
    # AudioProcessingType.Full — для асинхронного распознавания.

    # Распознавание речи в указанном аудиофайле и вывод результатов в консоль.
    result = model.transcribe_file(audio)
    print('result', result)
    for c, res in enumerate(result):
        # print(f'channel: {c}\n\nraw_text:\n{res.raw_text}\n
        # \nnorm_text:\n{res.normalized_text}\n')
        # print(norm_text:{res.normalized_text}\n')
        if res.has_utterances():
            print('utterances:')
            for utterance in res.utterances:
                print(utterance)
    return res.normalized_text


def trans_text(texts, target_language):
    """ перевод строки на другой язык"""
    # Яндекс переводчик
    # https://cloud.yandex.com/en-ru/docs/translate/
    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": id_folder,}

    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer {0}".format(iam_token)}
    response = requests.post(
        URL_TRANSL, json=body, headers=headers)
    print(response)
    decode_resp = response.content.decode('UTF-8')  # декодируем
    text = json.loads(decode_resp)  # загружаем в json
    answ4 = text['translations'][0]['text']
    return answ4


def str_to_audio_sdk(text, export_path, lng, voice, role):
    """ Синтез речи с помощью Python SDK"""
    # https://cloud.yandex.ru/docs/speechkit/sdk/python/synthesis
    model = model_repository.synthesis_model()

    # Задайте настройки синтеза.
    model.language = lng
    model.voice = voice
    model.role = role

    # Синтез речи и создание аудио с результатом.
    result = model.synthesize(text, raw_format=False)
    result.export(export_path, 'wav')


iam_token = get_token()
# задаем iam-токен (берем текущий или генерируем новый)


if __name__ == '__main__':
    str_ru = 'создание аудио файла из строки'
    str_eng = 'Permission is hereby granted, free of charge, to any person)'
    lng = 'ru-Ru'
    lng = 'en-En'
#    otv = str_to_audio_f(str_ru,lng)
#    print('Аудио файл создан',otv)
#    sound('str_to_f.wav')

    print(trans_text(str_ru, 'en'))
#    print(trans_text(str_eng,'ru'))

#    str1 = audio_f_to_str("audio_guest.ogg")
#    print('Расш: ',str1)
