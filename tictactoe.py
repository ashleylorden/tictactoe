import random

# Tic Tac Toe logic

# computer character = p
# human player character = h

def first_player():
	chance = random.randint(0,1)
	if chance == 0:
		return "p"
	elif chance == 1:
		return "h"

class TicTacToe(object):
	"""The classic game of tic tac toe"""
	def __init__(self):
		self.board = list(" " * 9)

	def move(self, space, character):
		self.board[space] = character

	def is_available(self, space):
		return self.board[space] == " "
		
	def three_in_row(self, character, space1, space2, space3):
		if self.board[space1] == character \
		and self.board[space2] == character \
		and self.board[space3] == character:
			return True

	def winner(self, character):
		if self.three_in_row(character, 0, 1, 2) \
		or self.three_in_row(character, 3, 4, 5) \
		or self.three_in_row(character, 6, 7, 8) \
		or self.three_in_row(character, 0, 3, 6) \
		or self.three_in_row(character, 1, 4, 7) \
		or self.three_in_row(character, 2, 5, 8) \
		or self.three_in_row(character, 0, 4, 8) \
		or self.three_in_row(character, 6, 4, 2):
			return True
		else:
			return False

	def available_board(self):
		available_board = []
		for space in range(9):
			if self.is_available(space):
				available_board.append(space)
		return available_board

	def tie(self):
		if len(self.available_board()) == 0:
			return True
		else:
			return False

	def copy(self):
		copy = TicTacToe()
		copy.board = list(self.board)
		return copy

	def terminate(self):
		if self.winner("p"):
			return "win p"
		elif self.winner("h"):
			return "win h"
		elif self.tie():
			return "tie"
		else:
			return ""

class AI(object):
	turn = {"p" : "h", "h": "p"}

	def __init__(self, board):
		self.board = board
		self.player = "p"

	def generate(self, board, player):
		children = []
		for space in board.available_board():
			child = board.copy()
			child.move(space, player)
			children.append((child, space))
		return children

	def minimax(self, board, player):
		outcome = board.terminate()
		if outcome == "win p":
			return 1
		elif outcome == "win h":
			return -1
		elif outcome == "tie":
			return 0
		player = AI.turn[player]
		next_round = self.generate(board, player)
		if player == self.player:
			return max([self.minimax(board, player) for board, space in next_round])
		else:
			return min([self.minimax(board, player) for board, space in next_round])

	def computer_play(self):
		if len(self.board.available_board()) == 9:
			self.board.move(2, self.player)
			return
		possibilities = self.generate(self.board, self.player)
		scores = [(self.minimax(child, self.player), space) for child, space in possibilities]
		best_space = sorted(scores)[-1][1]
		self.board.move(best_space, self.player)

