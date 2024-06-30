import calculations
import file_manager
import player_storage

if __name__ == "__main__":
    # Объединение файлов, удаление пробелов в имени, сохранение файла
    file_frame = file_manager.get_concat_file()
    file_manager.delete_spaces(file_frame)
    file_manager.save_to_csv(file_frame)

    # создание файла с уникальными именами на основе столбца Имя, сохранение этого файла
    unique_data = file_frame.drop_duplicates(subset='Имя')
    file_manager.save_to_csv(unique_data, 'output_files/Unique.csv')

    # Перебирается уникальный фрейм, добавляется каждый игрок в список
    for index, row in unique_data.iterrows():
        player_storage.add_player(row["Ном."], row["Имя"], row["Рейт"])

    # на основе имени игрока из уникального фрейма ищутся противники и добавляются в список к каждому игроку
    for elem in player_storage.players_list:
        name = elem["player"]["name"]
        for index, row in file_frame.iterrows():
            if row["Имя"] == name:
                player_storage.add_enemy_to_player(elem["player"]["id"], row["Ном..1"], row["Имя.1"],
                                                   row["Рейт.1"], row["Результат"])
            elif row["Имя.1"] == name:
                player_storage.add_enemy_to_player(elem["player"]["id"], row["Ном."], row["Имя"],
                                                   row["Рейт"], row["Результат"][::-1])
                print("------------------")
                print(row["Результат"])
                print(row["Результат"][::-1])
                print("------------------")

    # for elem in player_storage.players_list:
    #     calculations.calculate_score(elem)
    #     print("----------------------")
    calculations.calculate_score(player_storage.players_list[0])
