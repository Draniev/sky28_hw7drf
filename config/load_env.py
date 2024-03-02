import os

from dotenv import load_dotenv

is_dotenv_load = load_dotenv()

if not is_dotenv_load:
    raise FileNotFoundError('Не удалось загрузить переменные окружения!')

EMAIL_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

SECRET = os.getenv('SECRET_KEY')
STRIPE_API = os.getenv('STRIPE_API_KEY')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

if not (EMAIL_USER and EMAIL_PASSWORD and
        SECRET and STRIPE_API and DB_USER and
        DB_NAME and DB_PASSWORD):
    raise FileNotFoundError('Не удалось загрузить какую-то переменную')
