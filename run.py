from simple_term_menu import TerminalMenu


def show_the_rules():
    """
    Shows the rules of the game
    """
    print(f'''
    1.Follow the instructions!
    2.Type the words carefully!
    ''')


show_the_rules()

def main():
    """ Main program function"""
    # Welcome message
     # Shows welcoming message
    print(f'''Welcome to Madlib Mania!''')
    user_name = ""
    # Ask for user's name
    while len(user_name) < 2:
        user_name = input('Please enter your name: ')
    print(f'''Hello, {user_name}, please pick an option from the menu''')
    options = ['1.Instructions', '2.Start Game', '3.Quit']
    main_menu = TerminalMenu(options)
    sub_options = ['1.Story 1', '2.Story 2' , '3.Go back']
    sub_menu = TerminalMenu(sub_options)
    quitting = False 
    while quitting is not True:
        menu_index = main_menu.show()
        options_choice = options[menu_index]
        if options_choice == '3.Quit':
            print(f'Hope you enjoyed the game {user_name}!')
            quitting = True
        elif options_choice == '1.Instructions':
            show_the_rules()



    
