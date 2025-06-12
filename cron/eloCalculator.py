
def playerElo(currentClanWarJSON, playerTag):
    player = None
    enemy = None

    #Work in progress
    for player in currentClanWarJSON["clan"]["members"]:
        if player["tag"] == playerTag:
            playerInfo = player
            break

    if "attacks" in playerInfo:
        for attack in playerInfo["attacks"]:
            #attack["defenderTag"]
            for enemy in currentClanWarJSON["opponent"]["members"]:
                if enemy["tag"] == attack["defenderTag"]:
                    enemyInfo = enemy
                    break

            #HERE WE NEED TO CALCULATE ELO
    return
