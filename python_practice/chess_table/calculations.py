
def calculate_score(player_info: dict):
    scores = 0
    for elem in player_info["enemies"]:
        if elem["result"] == "0-1" or elem["result"] == "--+":
            scores += 1
        elif elem["result"] == "1-0" or elem["result"] == "+--":
            pass
        elif elem["result"] == "½-½":
            scores += 0.5
    print(scores)