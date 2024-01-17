# coding: utf-8
import os
def env_set():
    ''' Функция задает переменные окружения,
    чтобы использовать их в запросах к API YSK:
    oauth_token (str)
    id_folder (str)

    :return: True
'''
    os.environ["oauth_token"] = "y0_----Ваш oauth-token -----------------------------------"
    os.environ["id_folder"] = "---Ваш folderId-----"
    os.environ["api_key"] = "AQ-----Ваш api-key----------------------"
    return True
    