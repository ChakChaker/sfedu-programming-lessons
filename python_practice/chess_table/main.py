from chess_table.file import file_reader, file_saver
from chess_table import player_storage

if __name__ == "__main__":
    file_data_frame = file_reader.get_concat_file()
    file_data_frame['Имя'] = file_data_frame['Имя'].str.strip()
    file_data_frame['Имя.1'] = file_data_frame['Имя.1'].str.strip()
    file_data_frame['Результат'] = file_data_frame['Результат'].str.replace(' ', '')
    file_saver.save_to_csv(file_data_frame)

    unique_data = file_data_frame.drop_duplicates(subset='Имя')
    file_saver.save_to_csv(unique_data, 'output_files/Unique.csv')

    two_columns_values = list(zip(unique_data['Ном.'], unique_data['Имя'], unique_data['Рейт']))
    two_columns_values[0] = 4
    print(two_columns_values[1])

    player_storage.add_player(1, "lox", 1240)
    player_storage.add_enemy_to_player(1, 3, "fdssf", 34, "1-0")
