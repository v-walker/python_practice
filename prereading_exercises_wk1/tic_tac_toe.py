# # set-up of nested loops for tic-tac-toe board
# SIZE = 3
# for y in range(SIZE):
#     for x in range(SIZE):
#         print(y, x)

# # output
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# # create board w/ empty list, then .append() empty list
# SIZE = 3
# board = [] # start w/ empty list
# for y in range(SIZE):
#     # each element in the board will also be a list
#     board.append([])
#     for x in range(SIZE):
#         pass
# print(board)

# # output
# [[], [], []]

# # now add "coordinates" in each of the inner lists
# SIZE = 3
# board = [] # start w/ empty list
# for y in range(SIZE):
#     # each element in the board will also be a list
#     board.append([])
#     for x in range(SIZE):
#         # fill inner lists with the coordinates
#         board[y].append(f"[{y}][{x}]")
# print(board)

# # output
# # [['[0][0]', '[0][1]', '[0][2]'], ['[1][0]', '[1][1]', '[1][2]'], ['[2][0]', '[2][1]', '[2][2]']]

# now print as grid
SIZE = 3
board = [] # start w/ empty list
for y in range(SIZE):
    # each element in the board will also be a list
    board.append([])
    for x in range(SIZE):
        # fill inner lists with the coordinates
        board[y].append(f"[{y}][{x}]")

for row in board:
    for column in row:
        print("%s  " % column, end="") #?? what is this "end" variable and what does it do?
    print("\n")

# output
# [0][0]  [0][1]  [0][2]  

# [1][0]  [1][1]  [1][2]  

# [2][0]  [2][1]  [2][2]  