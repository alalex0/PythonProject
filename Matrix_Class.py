# "Matrix has you
# 1) Создать класс Matrix, у которого есть приватное поле matrix представляющее из себя двумерный 
# массив размерностями m на n.
# Значения m и n задаются в конструкторе класса Matrix.
# 2) В классе Matrix реализовать метод add(Matrix x) который к старому содержимому матрицы прибавляет
# содержимое матрицы x (параметра)
# 3) Предусмотреть в классе Matrix возможность сложения матриц разных резмерностей. В этом случае метод
# add() должен выдавать ошибку и не совершать сложение.
# Старая матрица при этом должна остаться как есть."
import random

class Matrix:
    def __init__(self,m,n):
        self.m=m
        self.n=n
        self.__matrix=[[random.randint(1,10) for _ in range(self.m)] for _ in range(self.n)]
    def get_matrix(self):
        return self.__matrix
   
    def add(self,matrix_new):
        matrix_sum=[]
        def check(matrix,matrix_new):
            if len(matrix)!=len(matrix_new):
                 return False
            for i in range(len(matrix)):
                if len(matrix[i])!=len(matrix_new[i]):
                    return False  
            return True       
        if check(self.__matrix,matrix_new):
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                    matrix_sum.append(self.__matrix[i][j]+matrix_new[i][j])
            self.__matrix=matrix_sum
            return self.__matrix
        print("Матрицы не равны")
        return self.__matrix
    
    def add_any(self,matrix_new):
        matrix_sum=[]
        for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                    try:
                            matrix_sum.append(self.__matrix[i][j]+matrix_new[i][j])
                    except (IndexError):
                        matrix_sum.append(0)
                    else:
                         print("Матрицы не равны")
        self.__matrix=matrix_sum
        return self.__matrix
        



matrix=Matrix(3,3)
print("matrix", matrix.get_matrix())
matrix_new=[[1,2,3],[1,1,1],[1,1,1]]
print("matrix_new", matrix_new)
matrix.add(matrix_new)
print("matrix_resalt", matrix.get_matrix())

# print(matrix.add_any(matrix_new))
# print(matrix.get_matrix())
