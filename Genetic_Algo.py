import random
import matplotlib.pyplot as plt
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
                    #x1= str(x)
                    #y1= str(y)
                    #i1= str(i)
                    #j1= str(j)
                    #print("x: "+x1+" y: "+y1+" i: "+i1+" j: "+j1)
                    #b = (abs(dx) == abs(dy))
                    #print(b)
                    #b=(x==y)
                    #print(b)
                    total_attack=total_attack+1
            j=j+1
        i=i+1
        total_non_attack=((len(board)*(len(board)-1))-total_attack)/2
    #print(total_attack)
    return total_non_attack

#board=[2, 4, 4, 1 , 5, 1, 2, 4]
#board=[3, 2, 5, 4 , 3, 2, 1, 3]
#print(fitness(board))

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
        #print(new_board2)
    return new_board2, new_board1

def mutation(board, f):
    fit=f
    while(fit<=f):
        new_board = board
        index = random.randint(1, 8)
        mutant_gene= random.randint(1, 8)
        new_board[index - 1] = mutant_gene
        fit=fitness(new_board)
    return new_board

#board1=[2, 4, 7, 4 , 8, 5, 5, 2]
#board2=[3, 2, 7, 5 , 2, 4, 1, 1]
#new_board1, new_board2=crossover(board1, board2, 3)
#print(new_board1)
#print(mutation(new_board1, 4, 5))
#print(new_board2)
ultimate_list=[]
x_axis=[]
y_axis=[]
iter=1
while(iter<=12):
    n = random.randint(5, 10)
    i = 1
    randomlist = []
    while (i <= n):
        new_set = []
        j = 1
        while (j <= 8):
            number = random.randint(1, 8)
            new_set.append(number)
            j = j + 1
        randomlist.append(new_set)
        i = i + 1
    print("These are randomly generated population:\n", randomlist)
    if(len(ultimate_list)>=1):
        counter=random.randint(1,len(ultimate_list))
        ran=random.sample(range(0, len(ultimate_list)), counter)
        print("\nThese are added from old population:")
        for c in ran:
            randomlist.append(ultimate_list[c])
            print("\n",ultimate_list[c])
    rand = random.sample(range(0, len(randomlist)), 2)
    randomly_selected = [randomlist[rand[0]], randomlist[rand[1]]]
    print("\nThese are randomly selected to crossover:\n", randomly_selected)
    n = random.randint(1, 8)
    print("\nRandomly generated index number is: ", n)
    new_board1, new_board2 = crossover(randomly_selected[0], randomly_selected[1], n)
    print("\nWe get these new boards after cross-over: \n", new_board1, "\n", new_board2)
    print("\nFitness for New board 1: ", fitness(new_board1))
    print("\nFitness for New board 2: ", fitness(new_board2))
    possible_non_attack1 = ((len(new_board1) * (len(new_board1) - 1))) / 2
    possible_non_attack2 = ((len(new_board2) * (len(new_board2) - 1))) / 2
    f1 = fitness(new_board1)
    f2 = fitness(new_board2)
    if (possible_non_attack1 > f1):
        new_board1 = mutation(new_board1, f1)
        print("\nMutated New Board 1:\n", new_board1)

    if (possible_non_attack2 > f2):
        new_board2 = mutation(new_board2, f2)
        print("\nMutated New Board 2:\n", new_board2)

    f1 = fitness(new_board1)
    f2 = fitness(new_board2)
    if (f1 > f2):
        ultimate_list.append(new_board1)
        y_axis.append(f1)
    else:
        ultimate_list.append(new_board2)
        y_axis.append(f2)
    x_axis.append(iter)
    if(f1==possible_non_attack1):
        print("\nThe non-attacking board is:\n", new_board1)
        break
    elif(f2==possible_non_attack2):
        print("\nThe non-attacking board is:\n", new_board1)
        break
    iter=iter+1
print("\nx axis: ", x_axis)
print("\ny axis: ", y_axis)
plt.plot(x_axis, y_axis)
plt.xlabel("Iteration")
plt.ylabel("Fitness Value")
plt.show()

"""if(possible_non_attack1>f1 and possible_non_attack2>f2):
    print("\nCreating new population set")
    n = random.randint(5, 10)
    i=1
    new_population=[]
    while(i<=n):
        new_set=[]
        j=1
        while(j<=8):
            number = random.randint(1, 8)
            new_set.append(number)
            j=j+1
        new_population.append(new_set)
        i=i+1
    print("\nNew generated population is: ", new_population)"""