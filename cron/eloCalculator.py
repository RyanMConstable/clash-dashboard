
def playerElo(currentClanWarJSON, playerTag):
    #Work in progress
    for player in currentClanWarJSON["clan"]["members"]:
        if player["tag"] == playerTag:
            playerInfo = player
            break
    return
