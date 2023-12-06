import django
from django.conf import settings
from pathlib import Path
from django.core.management import execute_from_command_line

# TO USE DJANGO ORM
def init_django():
    if settings.configured:
        return
    
    BASE_DIR = Path(__file__).resolve().parent.parent

    settings.configure(
        INSTALLED_APPS=[
            'django_model.db',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
                'USER': 'test',
                'PASSWORD': 'myapp',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
        }
    )

    django.setup()


if __name__ == "__main__":
    init_django()
    execute_from_command_line()