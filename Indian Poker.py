import random

##def game():
def Heuristic():
    bet = 0
    lowerbound_count = 0
    upperbound_count = 0
    for i in card_list:
        if i >= player_card:
            upperbound_count += 1
        else:
            lowerbound_count += 1

    point = (float(upperbound_count-lowerbound_count)/len(card_list))*100
    card_list.remove(computer_card)
    if point >= 0 and point<=5:
        bet = round(float(computer_chip) * 5/100)
        return bet
    elif point > 5 and point<=15:
        bet = round(float(computer_chip) * 10/100)
        return bet    
    elif point > 15 and point<=25:
        bet = round(float(computer_chip) * 15/100)
        return bet    
    elif point > 25 and point<=35:
        bet = round(float(computer_chip) * 20/100)
        return bet    
    elif point > 35 and point<=45:
        bet = round(float(computer_chip) * 25/100)
        return bet    
    elif point > 45 and point<=55:
        bet = round(float(computer_chip) * 30/100)
        return bet    
    elif point > 55 and point<=65:
        bet = round(float(computer_chip) * 35/100)
        return bet    
    elif point > 65 and point<=75:
        bet = round(float(computer_chip) * 40/100)
        return bet    
    elif point > 75 and point<=85:
        bet = round(float(computer_chip) * 45/100)
        return bet    
    elif point > 85 and point<=95:
        bet = round(float(computer_chip) * 50/100)
        return bet    
    elif point > 95:
        bet = round(float(computer_chip) * 55/100)
        return bet
    else:
        bet = 0
        return bet

def visual_computer():
    print "     ______                                                       __________     "
    print "    /      \       Player            VS             Computer     |          |    "
    print "   / Player \       Card                              Card       | Computer |    "
    print "   \        /      _____       ______________        _____       |          |    "
    print "    \______/      |     |     |              |      |     |      |__________|    "
    print "    /      \      |  ?  |     | Pot Size:"+str(pot)+"   |      |  "+str(computer_card)+"  |          |  |        "
    print "   /        \     |_____|     |______________|      |_____|       ___|__|____    "
    print "Player Chip: "+str(player_chip)+"                                                Computer Chip: "+str(computer_chip)
    print
    
def visual_players():
    print "     ______                                                       __________     "
    print "    /      \       Player            VS             Computer     |          |    "
    print "   / Player \       Card                              Card       | Computer |    "
    print "   \        /      _____       ______________        _____       |          |    "
    print "    \______/      |     |     |              |      |     |      |__________|    "
    print "    /      \      |  "+str(player_card)+"  |     |              |      |  "+str(computer_card)+"  |          |  |        "
    print "   /        \     |_____|     |______________|      |_____|       ___|__|____    "
    print "Player Chip: "+str(player_chip)+"                                                Computer Chip: "+str(computer_chip)
    print

def pf_heuri():
    lowerbound_count = 0
    upperbound_count = 0
    for i in card_list:
        if i >= player_card:
            upperbound_count += 1
        else:
            lowerbound_count += 1
    point = (float(upperbound_count-lowerbound_count)/len(card_list))*100
    card_list.remove(computer_card)
    if point < 60:
        return 0
    else:
        return 1

#main
print "WELCOME TO YOUNG AND SOL'S INDIAN POKER"
print
print """GAME INSTRUCTION IS AS FOLLOWS:
Each player has 50 chips on their hand.
There are total of 10 rounds.
In each round, the player will bet their money by watching opponent's card.
Game ends either you lose all the money or 10 rounds are completed.
"""

global player_card
global card_list
global player_chip
global computer_card
global computer_chip

card_list = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
who_first = [0,1,2,3,4,5,6,7,8,9]
player_chip = 50
computer_chip = 50
game_count = 1
table_chip = 0

who_player = random.choice(who_first)
who_first.remove(who_player)
who_computer = random.choice(who_first)

if who_player < who_computer:
    turn = 1
    print
    print "     ______                                                       __________     "
    print "    /      \       Player            VS             Computer     |          |    "
    print "   / Player \       Card                              Card       | Computer |    "
    print "   \        /      _____       ______________        _____       |          |    "
    print "    \______/      |     |     |              |      |     |      |__________|    "
    print "    /      \      |  "+str(who_player)+"  |     |              |      |  "+str(who_computer)+"  |          |  |        "
    print "   /        \     |_____|     |______________|      |_____|       ___|__|____    "
    print
    print "                           So Computer Bets First!\n"
elif who_player > who_computer:
    turn = 0
    print "     ______                                                       __________     "
    print "    /      \       Player            VS             Computer     |          |    "
    print "   / Player \       Card                              Card       | Computer |    "
    print "   \        /      _____       ______________        _____       |          |    "
    print "    \______/      |     |     |              |      |     |      |__________|    "
    print "    /      \      |  "+str(who_player)+"  |     |              |      |  "+str(who_computer)+"  |          |  |        "
    print "   /        \     |_____|     |______________|      |_____|       ___|__|____    "
    print
    print "                           So Player Bets First!\n"



while True:
    if game_count < 11:
        while card_list != [] and turn == 1:
            player_card = random.choice(card_list)
            computer_card = random.choice(card_list)
            if player_card == computer_card:
                player_card = random.choice(card_list)
                computer_card = random.choice(card_list)
            else:
                #end of game?
                if computer_chip <= 0:
                    print "Game Over Player Won!"
                    game_count = 11
                    break
                elif player_chip <= 0:
                    print "Game Over Computer Won!"
                    game_count = 11
                    break
                #start game
                else:
                    print "------------------------------------------------------------------------------"
                    print "|                                    ROUND",game_count,"                                |"
                    print "------------------------------------------------------------------------------"
                    print
                    print "Player card:",player_card
                    pot = 4
                    player_chip -= 2
                    computer_chip -= 2
                    visual_computer()
                    computer_bet = int(Heuristic())
##                    print "Player: ",player_chip,"chips"
##                    print "Computer: ",computer_chip,"chips \n"
                    #computer die
                    psy = [0,1,1,1,1]
                    if player_card == 9:
                        choose = random.choice(psy)
                        if choose == 1:
                            computer_bet = int(round(computer_chip / 2))
                        else:
                            computer_bet = int(Heuristic())

                    if computer_bet == 0:
                        print "Computer died! Player won!"
                        player_chip += pot
                        pot = 0
                        card_list.remove(player_card)
                    #computer bet
                    else:
                        print "Computer bet "+str(computer_bet)+" chips \n"
                        computer_chip -= computer_bet
                        pot += computer_bet
                        visual_computer()
                        betting = raw_input("Do you want to call the bet?(Y/N)").lower()
                        if betting != "y" and betting != "n":
                            print "wrong input! type it again!"
                            betting = raw_input("Do you want to call the bet?(Y/N)").lower()
                        if betting == "y":
                            player_chip -= computer_bet
                            pot += computer_bet
                            if int(player_card) > int(computer_card):
                                player_chip += pot
                                pot = 0
                                card_list.remove(player_card)
                                print "Player won!"
                            elif int(player_card) < int(computer_card):
                                computer_chip += pot
                                pot = 0
                                card_list.remove(player_card)
                                print "Computer won!"
                            else:
                                computer_chip += float(pot) / 2
                                player_chip += float(pot) / 2
                                card_list.remove(player_card)
                                print "Draw!"
                        elif betting == "n":
                            if player_card == 9:
                                player_chip -= 10
                                computer_chip += 10
                                computer_chip += pot
                                pot = 0
                                print "You fold with highest card 9!"
                                print "10 chips go to computer for penalty"
                            else:
                                computer_chip += pot
                                pot = 0
                            card_list.remove(player_card)
                            print "Player died!"
                    print
                    print "Player's card was"
                    visual_players()
                    game_count += 1
                    turn = 0
                    raw_input("Press ENTER to continue...")

        while card_list != [] and turn == 0:
            player_card = random.choice(card_list)
            computer_card = random.choice(card_list)
            if player_card == computer_card:
                player_card = random.choice(card_list)
                computer_card = random.choice(card_list)
            else:
                if computer_chip <= 0:
                    print "Game Over Player Won!"
                    game_count = 11
                    break
                elif player_chip <= 0:
                    print "Game Over Computer Won!"
                    game_count = 11
                    break
                else:
                    print "------------------------------------------------------------------------------"
                    print "|                                    ROUND",game_count,"                                |"
                    print "------------------------------------------------------------------------------"
                    print
                    print "Player card:",player_card
                    pot = 4
                    player_chip -= 2
                    computer_chip -= 2
                    visual_computer()
                    try:
                        betting = int(raw_input("How many chips do you want to bet (0 to "+str(player_chip)+"): "))
                    except ValueError:
                        print "Wrong input!"
                        betting = int(raw_input("How many chips do you want to bet (0 to "+str(player_chip)+"): "))
                    while betting > player_chip:
                        print "You bet too much"
                        betting = int(raw_input("How many chips do you want to bet (0 or "+str(player_chip)+"): "))
                    if betting == 0:
                        print "Die!"
                        computer_chip += pot
                        pot = 0
                        card_list.remove(player_card)
                        card_list.remove(computer_card)
                    else:
                        pot += betting
                        player_chip -= betting
                        #Die or call
                        if pf_heuri() == 0: #0 = die
                            if computer_card == 9:
                                computer_chip -= 10
                                player_chip += 10
                                player_chip += pot
                                card_list.remove(player_card)
                                print "Computer's Penalty!"
                            else:
                                player_chip += pot
                                card_list.remove(player_card)                                
                                print "Computer Died! Player won!"
                        else:
                            computer_chip -= betting
                            pot += betting
                            #Comparing cards
                            if int(player_card) > int(computer_card):
                                player_chip += pot
                                pot = 0
                                card_list.remove(player_card)
                                print "Player won!"
                            elif int(player_card) < int(computer_card):
                                computer_chip += pot
                                pot = 0
                                card_list.remove(player_card)
                                print "Computer won!"
                            else:
                                computer_chip += float(pot) / 2
                                player_chip += float(pot) / 2
                                card_list.remove(player_card)
                                print "Draw!"
                    print
                    print "Player's card was"
                    visual_players()
##                    print "Player ends the round with",player_chip,"chips."
##                    print "Computer ends the round with",computer_chip,"chips."    
                    game_count += 1
                    turn = 1
                    raw_input("Press ENTER to continue...")
                    
    elif game_count == 11:
        print
        print "Total player chip:",player_chip
        print "Total computer chip:",computer_chip
        if player_chip > computer_chip:
            print "Player won! Congratulation!"
        elif computer_chip > player_chip:
            print "Computer won!"
        else:
            print "Draw! Rematch!!!"
        break










    
