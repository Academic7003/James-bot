import os

from dotenv import load_dotenv

load_dotenv()

# Заберем токен нашего бота (прописать в файле ".env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# Заберем данные для подключения к базе данных (юзер, пароль, название бд) - тоже прописать в файле ".env"
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

admins = [
    os.getenv("ADMIN_ID"),
    os.getenv("ADMIN_ID2"),

]

ip = os.getenv("ip")

# Ссылка подключения к базе данных
POSTGRES_URI = postgres://nhvrxploartdws:23a8b4c5efa46d801e7568cbd5d8ee7b1e79196d3c83b7506ea72fa2b36c1d9b@ec2-44-208-88-195.compute-1.amazonaws.com:5432/d50o3psk3m1tgv
aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
