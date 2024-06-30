import os
import pandas


def get_concat_file():
    # Путь к каталогу с CSV файлами
    files_directory = 'csv/let_pr/chess'

    # Создание пустого DataFrame для объединения данных
    all_data = pandas.DataFrame()

    # Загрузка всех CSV файлов из каталога
    for filename in os.listdir(files_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(files_directory, filename)
            df = pandas.read_csv(file_path)
            all_data = pandas.concat([all_data, df], ignore_index=True)
    return all_data


def delete_spaces(frame: pandas.DataFrame):
    frame['Имя'] = frame['Имя'].str.strip()
    frame['Имя.1'] = frame['Имя.1'].str.strip()
    frame['Результат'] = frame['Результат'].str.replace(' ', '')


def save_to_csv(data_frame: pandas.DataFrame, file_path='output_files/output.csv'):
    data_frame.to_csv(file_path, index=False)
    print(f'DataFrame сохранен в файл: {file_path}')

