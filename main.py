# defining player variables (if you're using emojis, make sure to have a space after them so it doesnt do the weird overlap thing)
team_1 = '🔴      '
team_2 = '🔵      '
space = '⚫      '

# defining the game board
game_board = [
    team_1, team_1, team_1, team_1, space, team_2, team_2, team_2, team_2
]

# while loop where the game actually happens
while True:
  # checks if the user won
  if game_board == [
      team_2, team_2, team_2, team_2, space, team_1, team_1, team_1, team_1
  ]:
    print('1️⃣      2️⃣      3️⃣      4️⃣      5️⃣      6️⃣      7️⃣      8️⃣      9️⃣')
    print(''.join(game_board))
    print('congrats, you won')
    break
  # optional, for spacing
  print('1️⃣      2️⃣      3️⃣      4️⃣      5️⃣      6️⃣      7️⃣      8️⃣      9️⃣')
  # print the board
  print(''.join(game_board))

  # take user input
  user_input = int(input('select a space or whatever\n'))

  # the -1 is because python starts counting at 0, while we start counting at 1. the first element in a list is list_name[0] not list_name[1].
  list_input = user_input - 1
  # gets the player on the board that corresponds to the user input
  user_input_player = game_board[list_input]

  # if the selected player is really a space:
  if user_input_player == space:
    print('you cant move there thats a space')
    print('\n')
    continue

  # if the selected player is equal to team 1:
  elif user_input_player == team_1:

    # if the selected team 1 player is one move away from an availible space:
    if user_input < 9 and game_board[list_input + 1] == space:
      # swaps the selected player and the space, then goes back to the start of this while loop
      game_board[list_input], game_board[list_input + 1] = game_board[
          list_input + 1], game_board[list_input]
      print('\n')
      continue

    # if the selected team 1 player is two moves away from an availible space (and there's a piece to jump over):
    elif user_input < 8 and game_board[list_input + 2] == space and game_board[list_input + 1] != space:
      # swaps the selected player and the space, then goes back to the start of this while loop
      game_board[list_input], game_board[list_input + 2] = game_board[
          list_input + 2], game_board[list_input]
      print('\n')
      continue

    # otherwise, you cant move the selected player
    else:
      print('\n')
      print('you cant move that player')
      print('\n')
      continue

  # if the selected player is equal to team 2:
  elif user_input_player == team_2:

    # if the selected team 2 player is one move away from an availible space:
    if user_input > 1 and game_board[list_input - 1] == space:
      # swaps the selected player and the space, then goes back to the start of this while loop
      game_board[list_input], game_board[list_input - 1] = game_board[
          list_input - 1], game_board[list_input]
      print('\n')
      continue

    # if the selected team 2 player is two moves away from an availible space (and there's a piece to jump over):
    elif user_input > 2 and game_board[list_input - 2] == space and game_board[list_input - 1] != space:
      # swaps the selected player and the space, then goes back to the start of this while loop
      game_board[list_input], game_board[list_input - 2] = game_board[
          list_input - 2], game_board[list_input]
      print('\n')
      continue

    # otherwise, you cant move the selected player
    else:
      print('\n')
      print('you cant move that player')
      print('\n')
      continue
