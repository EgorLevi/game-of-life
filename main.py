import random
import time
import json

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False

# class Matrix:
#     def __init__(self, global_sige):
#         self.gsize = global_sige
#         self.matrix = create_matrix(self.gsize)
    
def create_matrix(x):
        matrix = []
        for i in range(x):
            for j in range(x):
                matrix.append(Cell(i,j))
        return matrix


def print_matrix(matrix):
    # для консолей с поддержкой эмози 
    cell_life_sigths = {True:"🟢", False:"⬛"}
    # для консолей с буковами
    #cell_life_sigths = {True:"◉", False:"◯"}

    for i in range(Matrix_global_size*Matrix_global_size):
        if i%10 == 0 and i >1:
            print()
        print(cell_life_sigths[matrix[i].alive], end=' ')

def print_cells_cordinates(matrix):
    i = 0
    for cell in matrix:
        if i%10 == 0 and i >1:
            print()
        print(f"({cell.x},{cell.y})", end=' ')
        i += 1
    print()

def create_some_life(matrix):
    for _ in range(int(matrix.__len__())):
        pos = random.randint(0, matrix.__len__()-1)
        matrix[pos].alive = True
    return matrix

def life_gos_on(matrix):
    d = 0

    while 1:
        d+=1 #счетчик поколений
        control_matrix = [] # контрольная матрица для записи нового поколения

        # рааспечатки
        print(f"\n_____________Поколение {d}_________")
        print_matrix(matrix)

        for i in range(matrix.__len__()):
            # состояния соседей
            aln = []

            if matrix[i].x != 0:
                # есть соседи сверху
                # добавляем соседей сверху
                # 1 сосед прямо над ячейкой
                aln.append(matrix[i-Matrix_global_size].alive)

                # если есть сосед сверху-слева -- добавляем
                if matrix[i].y != 0:
                    aln.append(matrix[i-Matrix_global_size-1].alive)
                # если есть сосед сверху-справа -- добавляем
                if matrix[i].y != Matrix_global_size-1:
                    aln.append(matrix[i-Matrix_global_size+1].alive)

            if matrix[i].x != Matrix_global_size-1:
                # есть соседи снизу
                aln.append(matrix[i+Matrix_global_size].alive)

                # если есть есть снизу-слева
                if matrix[i].y != 0:
                    aln.append(matrix[i+Matrix_global_size-1].alive)
                # если есть есть снизу-справа
                if matrix[i].y != Matrix_global_size-1:
                    aln.append(matrix[i+Matrix_global_size+1].alive)
                pass

            if matrix[i].y != 0:
                # есть соседи слева
                aln.append(matrix[i-1].alive)

            if matrix[i].y != Matrix_global_size-1:
                # есть соседи справа
                aln.append(matrix[i+1].alive)
                pass

            #считаем соседей и меняем значение текущей точки
            aln = aln.count(True)
            if matrix[i].alive:
                if aln ==2 or aln ==3:
                    pass
                else:
                    matrix[i].alive = False

            else:
                if aln > 3:
                    matrix[i].alive = True

            control_matrix.append(matrix[i])

        # обновляем рабочую матрицу

        matrix = control_matrix[:]
        control_matrix = []
        time.sleep(1)
        # игра продолжается до бесконечности, но вметво этой строки можно прописать логику на
        # завершение при отвутсвии изменений

# задаем размерность матриц
Matrix_global_size = 10 # тут имеется ввиду 10*10, те всего 100 ячеек
m = create_matrix(Matrix_global_size)
m = create_some_life(m)
# print_cells_cordinates(m) #ТЕСТОВАЯ - распечатка координат ячеек
# print_matrix(m) #ТЕСТОВАЯ - распечатка матрицы
life_gos_on(m)



