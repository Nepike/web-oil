# Масло сайт

пока разработка сюда можно писать туду + полезные ссылки или код

https://app.weeek.net/ws/1024673/project/1/board/1


## 1. Как поднять сайт в dev?

### 1.1 Зависимости
- Python 3.12+

### Windows PowerShell
```bash

git clone https://github.com/Nepike/web-oil
cd web-oil

python3 -m venv .venv
. .\.venv\Scripts\activate
pip install -r requirements.txt

cp .env.example ./.env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```