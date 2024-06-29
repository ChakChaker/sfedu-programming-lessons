import pandas as pd


def save_to_csv(data_frame: pd.DataFrame, file_path='output_files/output.csv'):
    data_frame.to_csv(file_path, index=False)
    print(f'DataFrame сохранен в файл: {file_path}')