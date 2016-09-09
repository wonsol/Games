#ASSIGNMENT 2
#Sol Won
#INFO-I399
#Due date: 2016.02.09

#Part 1
def npile():
    #There are two players, start with the first player
    player = 1
    
    #Get the number of piles
    piles = int(raw_input("How many piles: "))
    print "There are", piles, " piles!\n"

    #Initiailize the number of stones in each pile
    pileStones = []
    for pile in range(piles):
        piles = int(raw_input("How many stones in pile " + str(pile+1)+ ": "))
        pileStones.append(piles)

    #data structure for moves
    #move = [pile, stones to remove]
    move = [0,0]
    
    while True:
    #ask for a valid move and check if it's valid   
    #print initial information
        print "\nCurrent player is ", player, "\n"

        #HINT: See enumerate function
        for index, stones in enumerate(pileStones):
            print "Pile " + str(index+1) +": " + str(stones) + " stones"
        print "\n"

        #get pile
        while True:
            move[0] = int(raw_input("Which pile: "))
            if move[0] > 0 and move[0] <= len(pileStones):
                break
            print "This is not a valid pile!"           

        #get # of stones
        while True:
            move[1] = int(raw_input("# of stones to remove: "))
            if move[1] <= pileStones[move[0]-1]:
                if move[1] > 0:
                    break
                else:
                    print "Need to select at least 1 stone!"
            else:
                print "Too many stones! There are only ",pileStones[move[0]-1], " in that pile!"
            
        #update the number of stones in the pile
        pileStones[move[0]-1] = pileStones[move[0]-1] - move[1]
        print "\nThe number of stones in pile ", move[0]," is now ",pileStones[move[0]-1]

        #check if win, loss
        win = False
        for stones in str(len(pileStones)):
            if sum(pileStones) == 0:
                win = True
                break
        if(win):
            print "\nPlayer ", player, "wins!"
            break

        #switch players
        if player == 1:
            player = 2
        else:
            player = 1

    #end game
    print "Game over"


#Part 2
def whoWins(piles):
        #number of 1s in each stacked column
        columnCounts = []
        
        #convert # of stones in each pile to binary and add the ones for each order of magnitude
        for stones in piles:
            #see Hint 2
            counter = 0
            while (stones > 0):
                rem = stones % 2
                if counter == len(columnCounts):
                    columnCounts.append(rem)
                else:
                    columnCounts[counter] += rem
                stones = stones / 2
                counter = counter + 1
            
        #check to see who wins
        for items in columnCounts:
                if(items % 2 == 1):
                        print "Player 1 wins!"
                        return          
        print "Player 2 wins!"


#Bonus
def npoker():
    #There are two players, start with the first player
    player = 1
    player_one_stone = 0
    player_two_stone = 0
    #Get the number of piles
    piles = int(raw_input("How many piles: "))
    print "There are", piles, " piles!\n"

    #Initiailize the number of stones in each pile
    pileStones = []
    for pile in range(piles):
        piles = int(raw_input("How many stones in pile " + str(pile+1)+ ": "))
        pileStones.append(piles)

    #data structure for moves
    #move = [pile, stones to remove]
    move = [0,0]
    
    while True:
    #ask for a valid move and check if it's valid   
    #print initial information
        print "\nCurrent player is ", player, "who has", player_one_stone," stones.\n"
        while True:
           take_add = int(raw_input("Take(0) or Add(1): "))
           if take_add == "0":
              #HINT: See enumerate function
              for index, stones in enumerate(pileStones):
                  print "Pile " + str(index+1) +": " + str(stones) + " stones"
              print "\n"

              #get pile
              while True:
                  move[0] = int(raw_input("Which pile: "))
                  if move[0] > 0 and move[0] <= len(pileStones):
                      break
                  print "This is not a valid pile!"           

              #get # of stones
              while True:
                  move[1] = int(raw_input("# of stones to remove: "))
                  if move[1] <= pileStones[move[0]-1]:
                      if move[1] > 0:
                          break
                      else:
                          print "Need to select at least 1 stone!"
                  else:
                      print "Too many stones! There are only ",pileStones[move[0]-1], " in that pile!"
                  
              #update the number of stones in the pile
              pileStones[move[0]-1] = pileStones[move[0]-1] - move[1]
              print "\nThe number of stones in pile ", move[0]," is now ",pileStones[move[0]-1]

              #check if win, loss
              win = False
              for stones in str(len(pileStones)):
                  if sum(pileStones) == 0:
                      win = True
                      break
              if(win):
                  print "\nPlayer ", player, "wins!"
                  break

              #switch players
              if player == 1:
                  player = 2
              else:
                  player = 1

   
           elif take_add == "1" and player_one_stone == 0:
              print "Player has no stones to add!"
           elif take_add == "1" and player_two_stone == 0:
              print "Player has no stones to add!"
           else:
              #HINT: See enumerate function
              for index, stones in enumerate(pileStones):
                  print "Pile " + str(index+1) +": " + str(stones) + " stones"
              print "\n"

              #get pile
              while True:
                  move[0] = int(raw_input("Which pile: "))
                  if move[0] > 0 and move[0] <= len(pileStones):
                      break
                  print "This is not a valid pile!"           

              #get # of stones
              while True:
                  move[1] = int(raw_input("# of stones to add: "))
                  if move[1] <= pileStones[move[0]-1]:
                      if move[1] > 0:
                          break
                      else:
                          print "Need to select at least 1 stone!"
                  else:
                      print "Too many stones! There are only ",pileStones[move[0]-1], " in that pile!"
                  
              #update the number of stones in the pile
              pileStones[move[0]-1] = pileStones[move[0]-1] + move[1]
              print "\nThe number of stones in pile ", move[0]," is now ",pileStones[move[0]-1]

        #check if win, loss
        win = False
        for stones in str(len(pileStones)):
            if sum(pileStones) == 0:
                win = True
                break
        if(win):
            print "\nPlayer ", player, "wins!"
            break

        #switch players
        if player == 1:
            player = 2
        else:
            player = 1

    #end game
    print "Game over"

