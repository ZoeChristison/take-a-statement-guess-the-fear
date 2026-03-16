import csv
import random

FILENAME = 'mag_game_data_storage.csv'

# Index numbers of following items in CSV
EP_NUMBER_KEY = 0
EP_TITLE_KEY = 1
EP_INFO_KEY = 2
CONTENT_WARNINGS_KEY = 3
EP_BLURB_KEY = 4
FEARS_KEY = 5

# Index numbers of following items in dictionary
# ep_number = dict key
EP_TITLE = 0
EP_INFO = 1
CONTENT_WARNINGS = 2
EP_BLURB = 3
FEARS = 4

# Function
# PLay game
def main():
    '''
    Play MAG game by calling make_csv_into_dict() to make
    CSV file with game data into a dict, take_guess() to
    take guesses from user, give_hints() to give user hints
    (episode info blurb, content warnings and blurb from episode),
    and give_answer() if they give up.
    return: None
    '''
    game_dict = make_csv_into_dict(FILENAME)
    play_again = 'y'

    while play_again == 'y':
        # Get episode number to determine which episode will be used
        episode_number = random.randint(1, 200)
        episode_number = 1

        episode_number = f'{episode_number}'

        begin_game(game_dict, episode_number)

        # Start number of hints at 1 so it can be used to determine which hint user will be given
        number_of_hints = 1

        while True: #### Could also do a turn-based game where user looses after x amount of turns-- would be while turns <= x:
            # Determine user action
            print('What action would you like to take? \n' \
            '1. Make Guess \n' \
            '2. Get hint \n' \
            '3. Show answer')

            action = input('>>> ')
            print()

            if action == '1': # Make guess
                # Get guess from user
                guess = input(f'What is your guess? ').title()

                # Give guess as an argument in function to determine if user won game
                game_won = take_guess(game_dict, episode_number, guess)

                # If user won game, print success and break out of loop
                if game_won == True:
                    print(f'{guess} is correct!')
                    break
                
                # If user was incorrect, print defeat
                #### Would also add to number_of_guesses if we decide to make that a thing
                else:
                    print(f'{guess} is incorrect. Please try again or ask for hint.')
                    #### number_of_guesses += 1
                    
            # End if action == '1' -- Make guess

            elif action == '2': # Get hint
                # Give hint to user based on how many they've already had
                hint = give_hints(game_dict, episode_number, number_of_hints)
                print(hint)

                # Add one to number of hints user has used
                number_of_hints += 1

            # End if action == '2' -- Get hint

            elif action == '3': # Get answer
                # Give answer and break out of loop
                give_answer(game_dict, episode_number)
                break

            # End if action == '3' -- Give up

            else: # Invalid input entered
                print('Invalid input given. Please enter a number from 1-3.')

        # Ask to play again
        play_again = input('Play again (y/n): ').lower()

    print('Thank you for playing Take a Statement, Guess the Fear! Have a good day!')

# Function
# Make CSV into dict
#### Will need two of these functions if fears are moved to seperate CSV-- will have make_game_csv_dict() return game_dict 
#### and make_answer_csv_dict() return answer_dict
def make_csv_into_dict(filename):
    '''
    Makes a dictionary from the rows in the CSV file.
     Param: filename: Name of file to check item in
    return: game dictionary
    '''
    # Open empty dictionary
    game_dict = {}

    # Open file andassign values to dict
    with open(filename) as file:

        reader = csv.reader(file)
        next(reader) 
        # Needed since we have a description line at beginning of CSV 
        # (Episode number,Title,Statement info,Content warning,Episode blurb,['Fears'])

        # Assign index values in CSV to dict (ep_number: [title, info, warnings, blurb, [fears]])
        for row in reader:
            key = row[EP_NUMBER_KEY] # Ep number is key to dict
            value_1_title = row[EP_TITLE_KEY] # Title is dict[key][0]-- Will be provided to user at beginning of game
            value_2_info = row[EP_INFO_KEY] # Info blurb is dict[key][1]-- First hint
            value_3_warnings = row[CONTENT_WARNINGS_KEY] # Content warnings are dict[key][2]-- Second hint
            value_4_blurb = row[EP_BLURB_KEY] # Blurb from episode is dict[key][3]-- Third hint
            value_5_fears = row[FEARS_KEY] # Fears are dict[key][4]-- Answer
            values = [value_1_title, value_2_info, value_3_warnings, value_4_blurb, value_5_fears] # Arrange values for dict
            game_dict[key] = values # Put values in dict

    # Return the dictionary
    return game_dict

# Function
# Gives user ep title and number
def begin_game(game_dict, episode_number):
    '''
    Prints game rules, episode number and title
     Param: game_dict: Dictionary of all episodes
     Param: episode_number: Episode number
    return: None
    '''
    print(
    '''
    Welcome to Take a Statement, Guess the Fear! You will be given random Magnus
    Archive episodes and you will try to guess one of the main fears assiciated
    with that episode. Each fear can be referred to by many names, so here are the
    names you should use while entering your guess:

    The Buried
    The Corruption
    The Dark
    The Desolation
    The End
    The Extinction
    The Eye
    The Flesh
    The Hunt
    The Lonely
    The Slaughter
    The Spiral
    The Stranger
    The Vast
    The Web

    Thank you for playing, and have fun!
    ''')
    # Find episode title in dict
    title = game_dict[episode_number][EP_TITLE]

    # Print episode number and title
    print(f'What fear is assiciated with MAG {episode_number}: {title}?')

# Function
# Take and check guesses
def take_guess(game_dict, episode_number, guess):
    '''
    Checks if the guess is correct or not
     Param: game_dict: Dictionary of all episodes
     Param: episode_number: Episode number
     Param: guess: Guess made by user
    return: True if guess is right or False if guess is wrong
    '''
    # Returns True or False based on whether guess was wrong or right
    if guess in game_dict[episode_number][FEARS]:
        # print(f'{guess} is correct!')-- right now print statements are in main()
        # Could also print other values in fears list (Here are all correct answers: )
        game_won = True

    else:
        # print(f'{guess} is incorrect. Please try again or ask for hint.')
        game_won = False

    return game_won

# Function
# Give user hints (info blurb, content warnings, blurb from episode)
def give_hints(game_dict, episode_number, hint_number):
    '''
    Gives hint to user
     Param: game_dict: Dictionary of all episodes
     Param: episode_number: Episode number
     Param: hint_number: Number of hints user is on
    return: hint
    '''
    #### Will need to be reorganized because not all episodes have content warnings--
    #### Add if statement-- if episode_number >= [number it starts having content warnings]
    #### else: [have all hints except for content warnings]

    # if game_dict[episode_number][CONTENT_WARNINGS] == 'none': (prob won't need because the transcripts have content warnings)

    # Give hint based on how many user has been given
    if hint_number == 1: # User's first hint
        statement_info_hint = game_dict[episode_number][EP_INFO]
        hint = f'Statement Info: {statement_info_hint}'

    elif hint_number == 2: # User's second hint
        warnings_hint = game_dict[episode_number][CONTENT_WARNINGS]
        hint = f'Content Warnings: {warnings_hint}'

    elif hint_number == 3: # User's third hint
        ep_blurb_hint = game_dict[episode_number][EP_BLURB]
        hint = f'Blurb from episode: {ep_blurb_hint}'

    else: # User has already gotten all hints
        hint = 'You have used all your hints!'

    return hint

# Function
# Prints all fears related to episode
def give_answer(game_dict, episode_number):
    '''
    Prints answer to user if they give up (lame!)
     Param: game_dict: Dictionary of all episodes
     Param: episode_number: Episode number
    return: None
    '''
    # Find fears in dict and print them out one by one
    print(game_dict[episode_number][FEARS])

main()