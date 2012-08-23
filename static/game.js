
var h;
var p;
var game_over = false;

function draw_board(board) {
	for (space in board) {
		if (board[space] == " ") {
		}
		else if (board[space] == "h") {
			element_id = "space" + space
			$('#' + element_id).addClass(h)
		}
		else if (board[space] == "p") {
			element_id = "space" + space
			$('#' + element_id).addClass(p)
		}
	}
}

function show_message(message){
	if (message == "win h") {
		$('div.message').html("<p>Awesome, you won!</p>");
	}
	else if (message == "win p") {
		$('div.message').html("<p>You lost. Don't feel bad, the computer practices a lot.</p>");
	}
	else if (message == "tie") {
		$('div.message').html("<p>Lame, we both lost.</p>");
	}
	$('#again').show();
	game_over = true;
}

var refresh = function(response){
	draw_board(response.board);
	if (response.message) {
		show_message(response.message);
	}
	else {
		$('div.message').html("<p>Your move.</p>");
	}
};

$(document).ready(function(){
	character = window.location.pathname.substr(6);
	if (character == "x") {
		h = "evil";
		p = "good";
		$('div.message').html("<p>Welcome, Evil!</p>");
	}
	else if (character == "o") {
		h = "good";
		p = "evil";
		$('div.message').html("<p>Welcome, Good!</p>");
	}
	else {
		$('div.message').html("<p>Hello there, hacker!</p>");
	}
	// initial call
	space = ""
	$.getJSON('/tictactoe', {"space": space}, refresh);

	$('.space').click(function(){
		if (game_over == true) {
			return;
		}
		if (! $(this).hasClass("evil") && ! $(this).hasClass("good")) {
			$('div.message').html("<p>Okay, it might take me a few seconds to come up with a response to that.</p>");
			// move
			space = $(this).attr('id').substr(5);
			$.getJSON('/tictactoe', {"space": space}, refresh);
		}
	});
});
