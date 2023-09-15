import random

# Function to create a grid of letters with hidden words.
def creat_word_search(words, size):
    grid = [[' 'for _ in range(size)] for _ in range(size)] 

    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, size -1)
            col = random.randint(0, size - len(word))
        else:
            row = random.randint(0, size - len(word))
            col = random.randint(0, size -1)


        for letter in word:
            grid[row][col] = letter
            if direction == 'horizontal':
                col += 1
            else:
                row += 1
    
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return grid

# Function to display the grid on the screen.
def display_w_search(grid):
    for l in grid:
        print(' '.join(l))
    print()


list_words = ['BALL', 'HOUSE', 'BEE', 'TRAIN', 'DANCE']
size_grid = 15

grid_wordsearch = creat_word_search(list_words, size_grid)
display_w_search(grid_wordsearch)