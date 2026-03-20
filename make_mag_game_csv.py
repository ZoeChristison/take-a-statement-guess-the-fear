import csv

FILENAME = 'mag_game_data_storage.csv'

# Function
# Calls other function to make and add to data to csv file
def main():
    '''
    Makes CSV file to hold game info (episode number,
    episode title, episode info blurb, content warnings,
    blurb/excerpt from episode (maybe??), fear(s) associated with
    episode)
    return: None
    '''
    # Make loop so we can continue to add lines to CSV
    add_epsiode = 'y'
    while add_epsiode == 'y':
        # Get episode number and title
        episode_number = input('Episode number: ')
        episode_title = input(f'Title of episode {episode_number}: ')

        # Get info that will be used as hints in game
        episode_info_blurb = input(f'MAG {episode_number}: {episode_title} info blurb: ')
        content_warnings = input(f'MAG {episode_number}: {episode_title} content warnings: ')
        episode_blurb = input(f'MAG {episode_number}: {episode_title} episode blurb/key word/excerpt: ')

        # Get info on fears associated with episode
        number_of_fears = int(input(f'How many fears are associated with MAG {episode_number}: {episode_title}? '))
        i = 0
        fears = []
        while i != number_of_fears:
            associated_fear = input('Enter fear: ')
            fears.append(associated_fear)
            i += 1

        # Call add_to_csv_file() to add episode info
        add_to_csv_file(FILENAME, episode_number, episode_title, episode_info_blurb, content_warnings, episode_blurb, fears)
        print(f'Added line: {episode_number},{episode_title},{episode_info_blurb},{content_warnings},{episode_blurb},{fears}')

        # Continue loop
        add_epsiode = input('Add another episode (y/n): ').lower()

# Function
# Add input to file
def add_to_csv_file(filename, episode_number, episode_title, episode_info_blurb, content_warnings, episode_blurb, fears):
    '''
    Adds name and email to CSV file.
     Param: filename: Name of file to check item in
     Param: episode_number: Episode number of series
     Param: episode_title: Title of episode in series
     Param: episode_info_blurb: About blurb at top of episode
     Param: content_warnings: Episode content warnings
     Param: episode_blurb: Small excerpt from episode
     Param: fears: The fear(s) associated with the episode
    return: None
    '''
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        new_row = [episode_number,episode_title,episode_info_blurb,content_warnings,episode_blurb,fears]
        # Write the new row
        writer.writerow(new_row)

main()