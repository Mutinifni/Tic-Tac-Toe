def gameboard():
	print("\n %s| %s| %s" % (board[6],board[7],board[8]))
	print("__|__|__")
	print(" %s| %s| %s" % (board[3],board[4],board[5]))
	print("__|__|__")
	print(" %s| %s| %s\n" % (board[0],board[1],board[2]))
	
def checkwin(w):
	if board[0] == w and board[1] == w and board[2] == w:
			return True
	if board[3] == w and board[4] == w and board[5] == w:
			return True
	if board[6] == w and board[7] == w and board[8] == w:
			return True
	if board[0] == w and board[3] == w and board[6] == w:
			return True
	if board[1] == w and board[4] == w and board[7] == w:
			return True
	if board[2] == w and board[5] == w and board[8] == w:
			return True
	if board[6] == w and board[4] == w and board[2] == w:
			return True
	if board[0] == w and board[4] == w and board[8] == w:
		return True
	return False

board = ["1","2","3","4","5","6","7","8","9"]
turn = 1
moves = 0
result = False

while (moves < 9):
	gameboard()
	if turn == 1: #X's turn
		move = input("Choose your move, X: ")
		if board[(int(move)-1)] == move:
			board[(int(move)-1)] = "X"
		if checkwin("X"):
			result = True
			winner = "X."
			break
		moves += 1
		turn = 0
				
	else: #O's turn
		move = input("Choose your move, O: ")
		if board[(int(move) - 1)] == move:
			board[(int(move) - 1)] = "O"
		if checkwin("O"):
			result = True
			winner = "O."
			break
		moves += 1
		turn = 1
			
if result == True:
	print("Congratulations", winner,"You win!\n")
else:
	print("It's a draw!\n")
