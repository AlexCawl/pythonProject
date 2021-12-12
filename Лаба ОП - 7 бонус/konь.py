import copy


def path(m, n, x, y, board):
    road_map = [(x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y - 2), (x + 1, y - 2),
                (x + 2, y - 1), (x + 2, y + 1)]

    for i in range(len(road_map)):
        road = road_map[i]
        if (0 <= road[0] < m and 0 <= road[1] < n) and board[road[0]][road[1]] == 0:
            pass
        else:
            road_map[i] = ()

    while () in road_map:
        road_map.remove(())

    return road_map


def main_function(m, n, x, y, board, counter):
    board[x][y] = counter

    if counter == n ** 2:
        return True

    roads = path(m, n, x, y, board)

    if len(roads) == 0:
        return 'Казахстан угрожает нам бомбардировкой'

    values = []
    for new_pos in roads:
        board_test = copy.deepcopy(board)
        values.append((len(path(m, n, new_pos[0], new_pos[1], board_test)), new_pos))

    values.sort()
    pos = values[0][1]
    main_function(m, n, pos[0], pos[1], board, counter + 1)


def start(m, n, x, y):
    matrix = [[0 for i in range(n)] for j in range(m)]
    matrix[x][y] = 1
    main_function(m, n, x, y, matrix, 1)

    return matrix


file_input = open('input.txt', 'r')
file_output = open('output.txt', 'w')

text = file_input.readlines()
M, N = list(map(int, text[0].split()))
X, Y = list(map(int, text[1].split()))

arr = start(M, N, X - 1, Y - 1)
flag_output = True
for horizontal in arr:
    if 0 in horizontal:
        flag_output = False
        break

if flag_output:
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr[i])):
            file_output.write(f"{arr[i][j]:4} ", )
        file_output.write('\n')
else:
    file_output.write('Маршрут не существует')

