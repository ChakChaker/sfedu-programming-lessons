players_list = []


def add_player(id, name, rate):
    players_list.append({"player": {"id": id, "name": name, "rate": rate}, "enemies": []})


def add_enemy_to_player(player_id, id, name, rate, result):
    for elem in players_list:
        if elem["player"]["id"] == player_id:
            elem["enemies"].append({"name": name, "rate": rate, "id": id, "result": result})