import random, platform, os

# Function to create a grid of letters with hidden words.
def creat_word_search(words, size):
    grid = [[' 'for _ in range(size)] for _ in range(size)] 

    for word in words:
        for _ in range(10):
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, size -1)
                col = random.randint(0, size - len(word))
            else:
                row = random.randint(0, size - len(word))
                col = random.randint(0, size -1)

            if all(grid[row + (i if direction == 'vertical' else 0)][col + (i if direction == 'horizontal' else 0)] == ' ' for i in range(len(word))):
                for i, letter in enumerate(word):
                    grid[row + (i if direction == 'vertical' else 0)][col + (i if direction == 'horizontal' else 0)] = letter
                break

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

# str input in ordinal order
list_words = []
for i in range(5):
    ordinal = 'st'
    if  i == 1:
        ordinal = 'nd'
    if  i == 2:
        ordinal = 'rd'
    if  i == 3:
        ordinal = 'th'
    if  i == 4:
        ordinal = 'th'

    word = input(f'Enter the {i + 1}{ordinal} word: ').upper()
    list_words.append(word)


# Check the system to clean the terminal.
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

size_grid = 15

grid_wordsearch = creat_word_search(list_words, size_grid)
display_w_search(grid_wordsearch)