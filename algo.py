class Algo:
	def __init__(self):
		self.board = ['-','-','-',
					'-','-','-',
					'-','-','-',
					'-','-','-',]

	def check_win(self):
		win = False
		#horizontal win
		if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[2] != '-':
			win = True
		elif self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[5] != '-':
			win = True
		elif self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[8] != '-':
			win = True
	    #vertical win
		elif self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[6] != '-':
			win = True
		elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[7] != '-':
			win = True
		elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[8] != '-':
			win = True
	    #diagonal win
		elif self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[8] != '-':
			win = True
		elif self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[6] != '-':
			win = True
		return win

	def check_draw(self):
		draw = True
		for x in range(0,9):
			if self.board[x] == '-':
				draw = False
				break
		return draw


