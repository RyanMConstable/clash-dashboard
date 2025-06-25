
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
    enemyTH = int(enemyInfo["townhallLevel"])
    TH = int(playerInfo["townhallLevel"])

    #Here is the elo calculation
    eloChange = 0

    if enemyPosition < preferredAttackLow:
        #For attacking low targets
        if TH == enemyTH:
            if stars == 3:
                eloChange = 0
            elif stars == 2:
                eloChange = -3
            elif stars == 1:
                eloChange = -4 
            else:
                eloChange = -5
        elif TH > enemyTH:
            if stars == 3:
                eloChange = 0
            elif stars == 2:
                eloChange = -4
            elif stars == 1:
                eloChange = -5
            else:
                eloChange = -6
        else:
            if stars == 3:
                eloChange = 0
            elif stars == 2:
                eloChange = -1
            elif stars == 1:
                eloChange = -2
            else:
                eloChange = -3
    elif enemyPosition == preferredAttackLow or enemyPosition == preferredAttackHigh:
        #For attacking preferred targets
        if TH == enemyTH:
            if stars == 3:
                eloChange += 2
            elif stars == 2:
                eloChange = 0
            elif stars == 1:
                eloChange -= 1
            else:
                eloChange -= 2
        elif TH > enemyTH:
            if stars == 3:
                eloChange += 1
            elif stars == 2:
                eloChange = 0
            elif stars == 1:
                eloChange -= 2
            else:
                eloChange -= 3
        else:
            if stars == 3:
                eloChange += 3
            elif stars == 2:
                eloChange += 1
            elif stars == 1:
                eloChange = 0
            else:
                eloChange -= 1
    else:
        #For attacking higher targets
        if TH == enemyTH:
            if stars == 3:
                eloChange += 3 
            elif stars == 2:
                eloChange -= 2
            elif stars == 1:
                eloChange -= 3
            else:
                eloChange -= 4
        elif TH > enemyTH:
            if stars == 3:
                eloChange += 1
            elif stars == 2:
                eloChange -= 1
            elif stars == 1:
                eloChange -= 2
            else:
                eloChange -= 3
        else:
            if stars == 3:
                eloChange += 5
            elif stars == 2:
                eloChange -= 1
            elif stars == 1:
                eloChange -= 2
            else:
                eloChange -= 3

    returnInfo["enemyPosition"] = enemyPosition
    returnInfo["enemyTH"] = enemyTH
    returnInfo["preferredAttackLow"] = preferredAttackLow
    returnInfo["preferredAttackHigh"] = preferredAttackHigh
    returnInfo["eloChange"] = eloChange
            
    return returnInfo
