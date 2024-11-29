from django.core.management.base import BaseCommand
from django.conf import settings
from gallery.models import Image
import os

class Command(BaseCommand):
    help = 'Синхронизация метаданных изображений из директории static/tiles с базой данных'

    def has_dzi_file(self, directory):
        """Проверяет наличие любого .dzi файла в директории"""
        try:
            dzi_files = [f for f in os.listdir(directory) if f.endswith('.dzi')]
            if dzi_files:
                return dzi_files[0]
            return None
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при проверке DZI файла: {str(e)}'))
            return None

    def handle(self, *args, **options):
        tiles_dir = os.path.join(settings.STATIC_ROOT, 'tiles')
        
        if not os.path.exists(tiles_dir):
            self.stdout.write(self.style.ERROR(f'Директория {tiles_dir} не существует'))
            return

        self.stdout.write(f'Начало сканирования директории: {tiles_dir}')
        self.stdout.write(f'Содержимое директории: {os.listdir(tiles_dir)}')

        existing_images = {str(image.id): image for image in Image.objects.all()}
        valid_directories = []

        for dir_name in sorted(os.listdir(tiles_dir)):
            dir_path = os.path.join(tiles_dir, dir_name)
            self.stdout.write(f'Обработка директории: {dir_path}')
            
            if not os.path.isdir(dir_path):
                self.stdout.write(f'Пропуск {dir_path} - не является директорией')
                continue

            dzi_file = self.has_dzi_file(dir_path)
            if not dzi_file:
                self.stdout.write(f'Пропуск {dir_path} - DZI файл не найден')
                continue

            valid_directories.append(dir_name)
            
            try:
                unique_prefix = f'model_{dir_name}_{os.path.splitext(dzi_file)[0]}'
                self.stdout.write(f'Создание записи с префиксом: {unique_prefix}')
                
                if dir_name in existing_images:
                    image = existing_images[dir_name]
                    old_prefix = image.url_prefix
                    image.url_prefix = unique_prefix
                    image.save()
                    self.stdout.write(self.style.SUCCESS(
                        f'Обновлена запись для изображения {dir_name} (старый префикс: {old_prefix}, новый: {unique_prefix})'
                    ))
                else:
                    Image.objects.create(
                        id=dir_name,
                        title=f'Image {dir_name}',
                        url_prefix=unique_prefix
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Создана новая запись для изображения {dir_name} с префиксом {unique_prefix}'
                    ))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Ошибка обработки директории {dir_name}: {str(e)}'))
                # Не прерываем выполнение, продолжаем со следующей директорией
                continue

        self.stdout.write(f'Обработано директорий: {len(valid_directories)}')
        self.stdout.write(f'Список обработанных директорий: {valid_directories}')