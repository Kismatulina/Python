# Погружение в Python #
# Урок 30. Семинар 15: Обзор стандартной библиотеки Python
# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log

import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

debug_info_handler = logging.FileHandler(os.path.join(current_dir, 'debug_info.log'), encoding='utf-8')
debug_info_handler.setLevel(logging.DEBUG)
formatter_debug = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_info_handler.setFormatter(formatter_debug)

warnings_errors_handler = logging.FileHandler(os.path.join(current_dir, 'warnings_errors.log'), encoding='utf-8')
warnings_errors_handler.setLevel(logging.WARNING)
formatter_warning = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
warnings_errors_handler.setFormatter(formatter_warning)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")