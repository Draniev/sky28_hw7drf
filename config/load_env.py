import os

from dotenv import load_dotenv

if not os.getenv('INTO_DOCKER'):
    is_dotenv_load = load_dotenv()
    if not is_dotenv_load:
        raise FileNotFoundError('Не удалось загрузить переменные окружения!')
    else:
        print('Переменные окружения УСТАНОВЛЕНЫ')

EMAIL_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

SECRET = os.getenv('SECRET_KEY')
STRIPE_API = os.getenv('STRIPE_API_KEY')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_HOST = os.getenv('DB_HOST') if os.getenv('DB_HOST') else '127.0.0.1'
REDIS_HOST = os.getenv('REDIS_HOST') if os.getenv('REDIS_HOST') else '127.0.0.1'

if not (EMAIL_USER and EMAIL_PASSWORD and
        SECRET and STRIPE_API and DB_USER and
        DB_NAME and DB_PASSWORD):
    print(f'{EMAIL_USER=}, {EMAIL_PASSWORD=}, {SECRET=}, {STRIPE_API=}, {DB_USER=}, {DB_NAME=}, {DB_PASSWORD=}')
    raise FileNotFoundError('Не удалось загрузить какую-то переменную')
