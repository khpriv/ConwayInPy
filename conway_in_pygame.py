import random
import time
import copy
import pygame

rows = 120
columns = 120
generations = 0

# Initialize pygame
pygame.init()

tics_per_seconds = 60

# Set the height and width of the screen
screen_width = 1080
screen_height = 1080
size = [screen_width, screen_height]
rect_width = int(screen_width / columns)
rect_height = int(screen_height / rows)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code")


def create_gametable():
    pop = [' ', '#']
    table = []
    for y in range(rows+1):
        table.append([])
        for x in range(columns+1):
            table[y].append(random.choices(pop, [1, 1])[0])
    return table


def count_neighbours(current_table, x, y):
    neighbour_alive = 0
    nav_list_x = [-1, 0, 1]
    nav_list_y = [-1, 0, 1]
    if x == 0:
        nav_list_x.remove(-1)
    if x == columns:
        nav_list_x.remove(1)
    if y == 0:
        nav_list_y.remove(-1)
    if y == rows:
        nav_list_y.remove(1)

    neighbours_total = len(nav_list_x) * len(nav_list_y) - 1
    for xl in nav_list_x:
        for yl in nav_list_y:
            if xl == 0 and yl == 0:
                pass
            elif current_table[xl+x][yl+y] == '#':
                neighbour_alive += 1

    neighbour_dead = neighbours_total - neighbour_alive
    return neighbour_alive, neighbour_dead


def print_gametable(table):
    alive_num = 0
    for row in range(len(table)):
        alive_num += table[row].count('#')
    return alive_num


def main():
    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    gametable = create_gametable()
    print_gametable(gametable)

    global generations
    next_gametable = [None] * (rows + 1)
    for x in range(len(next_gametable)):
        next_gametable[x] = [' '] * (columns + 1)

    while not done:
        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(tics_per_seconds)
        # Clear the screen and set the screen background
        screen.fill("black")
        if generations > 1000:
            done = True

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

        for row in range(rows):
            for column in range(columns):
                alive, dead = count_neighbours(gametable, row, column)
                if gametable[row][column] == '#':
                    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                    if alive < 2:
                        next_gametable[row][column] = ' '
                    # Any live cell with two or three live neighbours lives on to the next generation.
                    elif 1 < alive < 4:
                        # pass
                        next_gametable[row][column] = '#'
                        rect = pygame.Rect(row * rect_width, column * rect_height, rect_width, rect_width)
                        pygame.draw.rect(screen, "white", rect)
                    # Any live cell with more than three live neighbours dies, as if by overpopulation.
                    elif alive > 3:
                        next_gametable[row][column] = ' '
                elif gametable[row][column] == ' ':
                    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                    if alive == 3:
                        next_gametable[row][column] = '#'
                        rect = pygame.Rect(row * rect_width, column * rect_height, rect_width, rect_width)
                        pygame.draw.rect(screen, "white", rect)
                    else:
                        next_gametable[row][column] = ' '
        gametable = copy.deepcopy(next_gametable)

        if print_gametable(gametable) == 0:
            # If all dead end the game pretty much
            done = True
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
w.rect(screen, "white", rect)
                    # Any live cell with more than three live neighbours dies, as if by overpopulation.
                    elif alive > 3:
                        next_gametable[row][column] = ' '
                elif gametable[row][column] == ' ':
                    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                    if alive == 3:
                        next_gametable[row][column] = '#'
                        rect = pygame.Rect(row * rect_width, column * rect_height, rect_width, rect_width)
                        pygame.draw.rect(screen, "white", rect)
                    else:
                        next_gametable[row][column] = ' '
        gametable = copy.deepcopy(next_gametable)

        if print_gametable(gametable) == 0:
            # If all dead end the game pretty much
            don