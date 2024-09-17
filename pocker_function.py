def findPokerHand(hand):

    # we will track the rank and suit of each card 
    # rank is the first character of the card 
    # suit is the second character of the card

    ranks = []
    suits = []

    # we will tack the maximum
    possibleRanks = []

    # we will loop through the hand and get the rank and suit of each card
    for card in hand:
        if len(card) == 2:
            rank= card[0]
            suit = card[1]

        else:
            rank = card[0:2]
            suit = card[2]

        # we will convert the rank to integer
        if rank == "J":
            rank = 11
        elif rank == "Q":
            rank = 12
        elif rank == "K":
            rank = 13
        elif rank == "A":
            rank = 14
    
        ranks.append(int(rank))
        suits.append(suit)

    sorted_ranks = sorted(ranks)

    # Royal Flush  &&  Strianht Flush  && Flush
    if suits.count(suits[0]) == 5:

        if 14 in sorted_ranks and 13 in sorted_ranks and 12 in sorted_ranks and 11 in sorted_ranks and 10 in sorted_ranks:
            # Royal Flush
            possibleRanks.append(10)
        elif all (sorted_ranks[i] == sorted_ranks[i-1]+1 for i in range (1,len(sorted_ranks))):
            # Straight Flush
            possibleRanks.append(9)

        else:
            # Flush
            possibleRanks.append(6)

    # four Straight
    if all (sorted_ranks[i] == sorted_ranks[i-1]+1 for i in range (1,len(sorted_ranks))):
        possibleRanks.append(5)

    # the set function will remove the duplicates
    Unique_values = list(set(sorted_ranks))

   # Four of a kind and Full House
    # 3 3 3 3 5   -- set --- 3 5 --- unique values = 2 --- Four of a kind
    # 3 3 3 5 5   -- set -- 3 5 ---- unique values = 2 --- Full house
    if len(Unique_values) == 2:
        for val in Unique_values:
            if sorted_ranks.count(val) == 4:  # --- Four of a kind
                possibleRanks.append(8)
            if sorted_ranks.count(val) == 3:  # --- Full house
                possibleRanks.append(7)

    # three of a kind && two paire

    # 5 5 5 7 8 ---set--- 5 7 8  ----> unique values a --> three of a kind
    # 5 5 7 7 8 ---set--- 5 7 8  ----> unique values a --> two pair

    if len(Unique_values) == 3:
        for val in Unique_values:
            if sorted_ranks.count(val) == 3:
                possibleRanks.append(4) # ---> four of a kind
            if sorted_ranks.count(val) == 2:
                possibleRanks.append(3) # ---> two pair


    # Pair
    if len(Unique_values) == 4:
        possibleRanks.append(2)

    # High Card
    if not possibleRanks:
        possibleRanks.append(1)

    pokerHandRanks = {10: "Royal Flush",
                      9: "Straight Flush",
                      8: "Four of a Kind",
                      7: "Full House",
                      6: "Flush",
                      5: "Straight",
                      4: "Three of a Kind",
                      3: "Two Pair",
                      2: "Pair",
                      1: "High Card"}
                
    output = pokerHandRanks[max(possibleRanks)]
    print(hand,output)
    return output


if __name__ == '__main__':
    findPokerHand(["KH", "AH", "QH", "JH", "10H"])  # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card