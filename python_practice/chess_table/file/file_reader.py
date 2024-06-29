import os
import pandas as pd


def get_concat_file():
    # Путь к каталогу с CSV файлами
    files_directory = 'csv/let_pr/chess'

    # Создание пустого DataFrame для объединения данных
    all_data = pd.DataFrame()

    # Загрузка всех CSV файлов из каталога
    for filename in os.listdir(files_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(files_directory, filename)
            df = pd.read_csv(file_path)
            all_data = pd.concat([all_data, df], ignore_index=True)
    return all_data
