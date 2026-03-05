from pathlib import Path
import shutil
import argparse

# Функція для парсингу аргументів командного рядка
def parse_arguments():
    parser = argparse.ArgumentParser(description='Copy files into directories based on extension.')
    parser.add_argument('source', help='Path to source directory')  # шлях до вихідної директорії
    parser.add_argument('destination', nargs='?', default='dist', help='Path to destination directory (default: dist)')  # шлях до директорії призначення, за замовчуванням dist
    return parser.parse_args()

# Рекурсивна функція для копіювання файлів у піддиректорії за розширенням
def copy_files_by_extension(src_dir: Path, dest_dir: Path):
    try:
        for item in src_dir.iterdir():  # перебираємо всі елементи директорії
            if item.is_dir():  # якщо елемент є директорією, викликаємо функцію рекурсивно
                copy_files_by_extension(item, dest_dir)
            elif item.is_file():  # якщо елемент є файлом
                ext = item.suffix[1:] if item.suffix else 'no_extension'  # отримуємо розширення файлу, якщо його немає — 'no_extension'
                dest_subdir = dest_dir / ext  # створюємо шлях до піддиректорії за розширенням
                dest_subdir.mkdir(parents=True, exist_ok=True)  # створюємо піддиректорію, якщо її немає
                shutil.copy2(item, dest_subdir / item.name)  # копіюємо файл у відповідну піддиректорію
    except PermissionError as e:
        print(f"PermissionError: {e}")  # обробка помилок доступу
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")  # обробка помилок відсутності файлу
    except Exception as e:
        print(f"Error: {e}")  # обробка інших помилок

# Головна функція
def main():
    args = parse_arguments()  # отримуємо аргументи
    source_dir = Path(args.source)  # шлях до вихідної директорії
    destination_dir = Path(args.destination)  # шлях до директорії призначення
    destination_dir.mkdir(parents=True, exist_ok=True)  # створюємо директорію призначення, якщо її немає
    copy_files_by_extension(source_dir, destination_dir)  # запускаємо копіювання файлів

# Точка входу в скрипт
if __name__ == '__main__':
    main()
