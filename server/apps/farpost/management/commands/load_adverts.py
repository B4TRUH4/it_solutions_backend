import json

from django.core.management.base import BaseCommand, CommandError
from ...models import Advert


class Command(BaseCommand):
    """Команда для загрузки данных из файла"""
    help = 'Loads adverts from JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            type=str,
            help='file with json data of adverts'
        )

    def handle(self, *args, **options):
        adverts = []
        try:
            with open(options['file']) as file:
                json_data = json.load(file)
                for advert in json_data:
                    adverts.append(Advert(**advert))
            Advert.objects.bulk_create(adverts)
        except FileNotFoundError:
            raise CommandError('Файл не найден')
        except Exception as e:
            raise CommandError(f'Ошибка создания объектов: {e}')

