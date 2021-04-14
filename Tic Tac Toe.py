from IPython.display import clear_output

# = fields = #
inputs = [' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ']

# = game won check method = #
def gamewon(inputs, counter):
    if (inputs[0] == inputs[1] == inputs[2] == 'X') or (inputs[0] == inputs[4] == inputs[8] == 'X') or (inputs[0] == inputs[3] == inputs[6] == 'X') or(inputs[1] == inputs[4] == inputs[7] == 'X') or (inputs[2] == inputs[5] == inputs[8] == 'X') or (inputs[3] == inputs[4] == inputs[5] == 'X') or (inputs[6] == inputs[7] == inputs[8] == 'X'):
        print('X won! game is over')
        return True
    if (inputs[0] == inputs[1] == inputs[2] == 'O') or (inputs[0] == inputs[4] == inputs[8] == 'O') or (inputs[0] == inputs[3] == inputs[6] == 'O') or (inputs[1] == inputs[4] == inputs[7] == 'O') or (inputs[2] == inputs[5] == inputs[8] == 'O') or (inputs[3] == inputs[4] == inputs[5] == 'O') or (inputs[6] == inputs[7] == inputs[8] == 'O'):
        print('O won! game is over')
        return True
    if counter == 9:
        print('Draw!')
        return True
    return False

# = display game grid method = #
def display(inputs):
    clear_output()
    gamewon(inputs, 1)
    print(inputs[0] + ' | ' + inputs[1] + ' | ' + inputs[2])
    print('---' + '' + '---' + '' + '---')
    print(inputs[3] + ' | ' + inputs[4] + ' | ' + inputs[5])
    print('---' + '' + '---' + '' + '---')
    print(inputs[6] + ' | ' + inputs[7] + ' | ' + inputs[8])
display(inputs)

# = game play again logic = #
def game():
    val = ''
  
    while val not in ['y', 'n']:
        val = input("Play again? ")
    if val == 'y':
        gameplay()
        
# = gameplay method call to start the game = #       
def gameplay():
        counter = 0
        marker = 'X'
        inputs = [' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ']
        while gamewon(inputs, counter) == False:
            
            val = ''
            while val not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                val = input("Please enter a valid number from 1 to 9: ")
            if marker == 'X':
                marker = 'O'
                inputs[int(val)-1] = 'O'

            else:
                marker = 'X'
                inputs[int(val)-1] = 'X'
            
            display(inputs)
            counter += 1
           
#         display(inputs)
        game()
        print("Thank you for playing")