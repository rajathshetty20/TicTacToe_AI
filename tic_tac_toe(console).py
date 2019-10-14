#TIC TAC TOE Game
import os
from algo import Algo

my_algo = Algo()
player_name = ['X','O']
player_sign = ['X','O']
current_player = 0
#the (i)th matrix index in ([0,1,2,3,4,5,6,7,8]) is represented by the (k)th key on numpad ([7,8,9,4,5,6,1,2,3]) by numbers[k-1]
numbers = [6,7,8,3,4,5,0,1,2]

#clear screen and take username as input
os.system('clear')
print("\t\t\tTIC TAC TOE")
player_name[0] = input("Enter the name of player X: ")
player_name[1] = input("Enter the name of player O: ")

def print_board():
	print("\t\t\t  TIC TAC TOE",end = ' ')
	for x in range(0,9):
		if((x)%3==0):
			print("\n\n\t\t\t | ",end = ' ')
		print(my_algo.board[x],end = '  ')
		if((x+1)%3==0):
			print(" | ",end = '  ')
	print("\n")

while True:
	#whenever a new game begins, reset the board content to '-'
	for x in range(0,9):
		my_algo.board[x] = '-'

	while True:
		#take a valid choice as input
		while True:
			try:
				os.system('clear')
				print_board()
				print("USE THE NUM-PAD TO MAKE YOUR CHOICE")
				choice = int(input("{} : ".format(player_name[current_player])))
				if my_algo.board[numbers[choice-1]] == '-':
					my_algo.board[numbers[choice-1]] = player_sign[current_player]
					break
			except(ValueError, IndexError):
				pass

		#check if there is any win or draw
		if my_algo.check_win():
			os.system('clear')
			print_board()
			print("{} wins".format(player_name[current_player]))
			if current_player == 0:
				current_player = 1
			else:
				current_player = 0
			break
		elif my_algo.check_draw():
			os.system('clear')
			print_board()
			print("Draw")
			if current_player == 0:
				current_player = 1
			else:
				current_player = 0
			break

		#switch players
		if current_player == 0:
			current_player = 1
		else:
			current_player = 0

	print("\nDo you want to play again? [y/n] : ",end = ' ')
	if input() == 'n':
		break
