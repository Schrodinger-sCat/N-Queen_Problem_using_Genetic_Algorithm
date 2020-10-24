def fitness(board):
    i=1
    total_attack=0
    for x in board:
        j=1
        for y in board:
            if(i!=j):
                dx = x - y
                dy = i - j
                if(abs(dx)==abs(dy) or x==y):
                    total_attack=total_attack+1
            j=j+1
        i=i+1
        total_non_attack=((len(board)*(len(board)-1))-total_attack)/2
    return total_non_attack

def crossover(board1, board2, index):
    i=0
    new_board1 = [0, 0, 0, 0, 0, 0, 0, 0]
    new_board2 = [0, 0, 0, 0, 0, 0, 0, 0]
    while(i<len(board1)):
        if(i<index):
            new_board1[i]=board1[i]
            new_board2[i]=board2[i]
        else:
            new_board1[i]=board2[i]
            new_board2[i]=board1[i]
        i=i+1
    return new_board2, new_board1

def mutation(board, mutant_gene, index):
    board[index-1]=mutant_gene
    return board

board=[3, 2, 5, 4 , 3, 2, 1, 3]
print(fitness(board))

#board1=[2, 4, 7, 4 , 8, 5, 5, 2]
#board2=[3, 2, 7, 5 , 2, 4, 1, 1]
#new_board1, new_board2=crossover(board1, board2, 3)
#print(new_board1)
#print(new_board2)