import random
import time
import copy

rows = 20
columns = 20
generations = 0


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
        print(table[row])
        alive_num += table[row].count('#')
    print(f'Num alive: {alive_num} Current gen: {generations}')
    return alive_num


def main():
    gametable = create_gametable()
    # gametable = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', '#', ' ', ' '], [' ', ' ', '#', ' ', ' '], [' ', ' ', '#', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    print_gametable(gametable)
    cells_checked = 0
    tables_copied = 0
    global generations
    # next_gametable = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    next_gametable = [None] * (rows + 1)
    for x in range(len(next_gametable)):
        next_gametable[x] = [' '] * (columns + 1)

    while generations < 1000:
        generations += 1
        for row in range(rows):
            for column in range(columns):
                alive, dead = count_neighbours(gametable, row, column)
                cells_checked += 1
                if gametable[row][column] == '#':
                    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                    if alive < 2:
                        next_gametable[row][column] = ' '
                    # Any live cell with two or three live neighbours lives on to the next generation.
                    elif 1 < alive < 4:
                        # pass
                        next_gametable[row][column] = '#'
                    # Any live cell with more than three live neighbours dies, as if by overpopulation.
                    elif alive > 3:
                        next_gametable[row][column] = ' '
                elif gametable[row][column] == ' ':
                    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                    if alive == 3:
                        next_gametable[row][column] = '#'
                    else:
                        next_gametable[row][column] = ' '
        gametable = copy.deepcopy(next_gametable)
        # gametable = next_gametable.copy()
        tables_copied += 1
        # next_gametable.clear()

        if print_gametable(gametable) == 0:
            print("Umarli")
            break
        time.sleep(0.5)


if __name__ == "__main__":
    main()
