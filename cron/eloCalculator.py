
def playerElo(currentClanWarJSON, playerTag, attack):
    returnInfo = {}

    playerInfo = None
    enemyInfo = None

    #Work in progress
    for player in currentClanWarJSON["clan"]["members"]:
        if player["tag"] == playerTag:
            playerInfo = player
            break

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

    #Here is the elo calculation
    eloChange = 0

    if enemyPosition < preferredAttackLow:
        #For attacking low targets
        if TH == enemyTH:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:
        elif TH > enemyTH:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:
        else:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:
    elif enemyPosition == preferredAttackLow or enemyPosition == preferredAttackHigh:
        #For attacking preferred targets
        if TH == enemyTH:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:
        
        elif TH > enemyTH:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:

        else:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:
    else:
        #For attacking higher targets
        if TH == enemyTH:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:
        
        elif TH > enemyTH:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:

        else:
            if stars == 3:

            elif stars == 2:

            elif stars == 1:

            else:

    returnInfo["enemyPosition"] = enemyPosition
    returnInfo["enemyTH"] = enemyTH
    returnInfo["preferredAttackLow"] = preferredAttackLow
    reutnrInfo["preferredAttackHigh"] = preferredAttackHigh
            
    return returnInfo
