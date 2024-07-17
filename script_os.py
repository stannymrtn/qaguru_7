import os

# Определение путей
CURRENT_FILE = os.path.abspath(__file__)  # Получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)  # Получаем абсолютный путь к текущей директории
FILES_DIR = os.path.join(CURRENT_DIRECTORY, 'files')  # Склеиваем путь к текущей директории и папке files
FOLDER_DIR = os.path.join(CURRENT_DIRECTORY, 'resource')  # Склеиваем путь к текущей директории и папке resource
ZIP_DIR = os.path.join(FOLDER_DIR, 'archive.zip')  # Склеиваем путь к папке resource и зип файлу archive.zip