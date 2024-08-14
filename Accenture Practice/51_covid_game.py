def find_winner(N, lyrics):
    players = list(range(1, N + 1))  # List of players from 1 to N
    current_index = 0  # Start with the first player
    
    # Process the song lyrics repeatedly until one player remains
    i = 0  # Index for the lyrics
    while len(players) > 1:
        if lyrics[i] == 'x':
            # Pass the parcel to the next player
            current_index = (current_index + 1) % len(players)
        elif lyrics[i] == 'y':
            # Eliminate the current player
            players.pop(current_index)
            # If a player is eliminated, don't increment the current_index
            # because the next player takes the place of the eliminated one
            if current_index == len(players):
                current_index = 0
        
        # Move to the next lyric in the song
        i = (i + 1) % len(lyrics)
    
    # The remaining player is the winner
    return players[0]

# Input section
N = int(input())  # Number of family members
lyrics = input().strip()  # Lyrics of the song

# Find and print the winner
print(find_winner(N, lyrics))
