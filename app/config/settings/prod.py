import logging

from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com',
    '.amazonaws.com',
    'trello-api.smallbee.me',
]

WSGI_APPLICATION = 'config.wsgi.prod.application'

import_secrets()


# [171121 | Logging]
# "여기서 사용하는 Log 설정에 대한 버전이라고 생각하셔야 될 것 같아요.
# 기본값은 1이라고 되있어요
# 그리고 handler는 어떤 Log에 대해서 그 Log를 어떻게 처리해야할지에 대한 내용이에요
# 그런데 어떻게 처리해주는 그 handler 개수가 console 이름의 hanlder 한개만 있음.
# 애는 어떻게 동작하냐면 logging이라는 모듈에 있는 StreamHandler라는 class 형태로 동작을 해요
# 이거는 'logging streamhandler'라고 검색을 해보면 파이썬에 내장된 모듈이에요.
# StreamHandler 같은 경우에는 콘솔창에 내용을 표시해줘요.
# 그리고 loggers에서 django라고 되있잖아요.
# 이건 logger 모듈 이름이 'django'로 시작할경우를 말해요.
# 그리고 handler는 지금 console하나 갖고 있죠.
# level은 DEBUG고 propagate는 전파한다인데, 이 에러를 잡을 수 있는
# 다른 핸들러가 있으면 거기까지 전달을 계속해서 내리는 거예요.
# 만약에 이게 없으면 여기서 끊기겠죠.
# 핸들러가 여러개 있을 때 다 처리하고 싶다하면 propagate를 넣어줘야합니다.
# 그럼 이렇게 설정을 해놓고 나서 runserver한 곳으로 다시 와볼게요.
#
# 이 log를 우리가 서버를 켜놨을 때는 우리가 서버에 있는 runserver를 항상 보고 있는게 아니잖아요.
# 그러니까 그 내용이 어디 파일에 기록되면 보기가 더 좋겠죠.

logger = logging.getLogger('__name__')

LOG_DIR = os.path.join(ROOT_DIR, '.log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] %(name)s (%(asctime)s)\n\t%(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            # It is called 'StreamHandler' because it doesn't make any fiels.
        },
        # 'file': {
        #     'class': 'logging.FileHandler',
        #     'level': 'DEBUG',
        #     'filename': os.path.join(ROOT_DIR, '.log', 'django.log')
        # },
        'file_info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'formatter': 'default',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
    },
    'loggers': {
        # logger 이름에 장고가 들어가 있는지. 정확히는 logger 모듈의
        # 이름을 의미해요.
        # ...
        # 그런데 저게 포함하는 것까지는 모르겠어요. .으로 구분되어있으면
        # 애가 알아서 해주는 것 같기는 한데
        # 일단 한번 해볼게요.
        # 장고로 인해서 생기는 로그같은 경우에는
        # console에서 출력이 될거예요.
        'django': {
            'handlers': [
                'console',
                'file_info',
                'file_error',
            ],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
