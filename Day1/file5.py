player1 = int(input("Enter points scored in 60 balls by player 1"))
player2 = int(input("Enter points scored in 60 balls by player 2"))
player3 = int(input("Enter points scored in 60 balls by player 3"))
sr1 = player1 * 100 / 60
sr2 = player2 * 100 / 60
sr3 = player3 * 100 / 60
print('Strike rates are')
print('Player 1', sr1)
print('Player 2', sr2)
print('Player 3', sr3)
print('Strike rates for 60 more balls are')
print('Player 1', player1*2)
print('Player 2', player2*2)
print('Player 3', player3*2)
print('Maximum 6 by player 1 are', player1 // 6)
print('Maximum 6 by player 2 are', player2 // 6)
print('Maximum 6 by player 3 are', player3 // 6)
