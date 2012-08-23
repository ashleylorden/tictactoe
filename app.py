from flask import Flask, request, url_for, \
     render_template, jsonify, session
from tictactoe import *
import json
import os

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def start():
	return render_template("start.html")

@app.route ("/game/<character>")
def game(character):
	return render_template("game.html")

@app.route ("/tictactoe", methods=["GET"])
def move(space=''):
	space = request.args['space']
	game = TicTacToe()
	ai = AI(game)
	end = False
	if space == '':
		player = first_player()
		if player == "p":
			ai.computer_play()
	else:
		space = int(space)
		current_board = session['board']		
		game.board = current_board
		game.move(space, "h")
		end = game.terminate()
		if not end:
			ai.computer_play()
			end = game.terminate()

	session['board'] = game.board
	my_board = {'board' : game.board}
	if not end:
		return json.dumps(my_board)
	print end
	my_board['message'] = end
	return json.dumps(my_board)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)