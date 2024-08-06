import logging


dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base': {
            'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        }
    },

    'handlers': {
        'console': {
            'class': logging.StreamHandler,
            'level': "DEBUG",
            'formatter': 'base'
        }
    },
    'loggers': {
        'voice.message': {
            'level': 'DEBUG',
            'handlers': ['console', ]
        },
        'aiogram.event': {
            'level': 'DEBUG',
            'handlers': ['console', ]
        },
        'aiogram.dispatcher':  {
            'level': 'DEBUG',
            'handlers': ['console', ]
        },
    }
}
