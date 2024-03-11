from django.core.management.base import BaseCommand
# Импортируйте необходимые функции из вашего скрипта
from rbuilder.xlsx_converter import xl_to_db


class Command(BaseCommand):
    help = 'Импорт данных для моделей из xl в бд'

    def handle(self, *args, **kwargs):
        # Здесь вызовите функцию из вашего скрипта
        xl_to_db()
