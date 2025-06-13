
def playerElo(currentClanWarJSON, playerTag, attack):
    returnInfo = {}

    playerInfo = None
    enemyInfo = None

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
            print(f"Player: {playerInfo}")
            print(f"Enemy: {enemyInfo}")

            preferredAttackLow = playerInfo["mapPosition"] - 1
            preferredAttackHigh = playerInfo["mapPosition"]
            stars = attack["stars"]
            destruction = attack["destructionPercentage"]
            finishTime = attack["duration"]
            enemyPosition = enemyInfo["mapPosition"]
            enemyTH = enemyInfo["townhallLevel"]
            TH = playerInfo["townhallLevel"]

            print(preferredAttackLow, preferredAttackHigh, stars, destruction, finishTime, enemyPosition, enemyTH, TH)

            
    return
