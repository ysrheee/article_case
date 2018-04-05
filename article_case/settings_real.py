from article_case.settings import *


DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'articlecase',
        'USER': 'articlecase',
        'PASSWORD': 'dkdlxlruddud!1',
        'HOST': 'articlecase.c6vsglxpugme.ap-northeast-2.rds.amazonaws.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}