"""
SEARCH IN MATRIX
--------

You are given a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


def search_in_matrix(matrix, target):
    matrix_length = len(matrix)
    if matrix_length == 0:
        return False

    index_in_matrix = len(matrix[0])
    if index_in_matrix == 0:
        return False

    column_index = 0
    row_index = index_in_matrix - 1
    while column_index < matrix_length and row_index >= 0:
        if matrix[column_index][row_index] == target:
            return column_index, row_index
        elif matrix[column_index][row_index] < target:
            column_index += 1
        else:
            row_index -= 1
    return [-1, -1]


matrix = [[1, 4, 7, 12, 15, 1000],
          [2, 5, 19, 31, 32, 1001],
          [3, 8, 24, 33, 35, 1002],
          [40, 41, 42, 44, 45, 1003],
          [99, 100, 103, 106, 128, 1004]]

# Testing Valid Functionality
print(search_in_matrix(matrix=matrix, target=44))
print(search_in_matrix(matrix=matrix, target=128))
print(search_in_matrix(matrix=matrix, target=2))
print(search_in_matrix(matrix=matrix, target=1003))

# Testing Invalid Functionality
print(search_in_matrix(matrix=matrix, target=14))
print(search_in_matrix(matrix=matrix, target=2000))
print(search_in_matrix(matrix=matrix, target=17))
print(search_in_matrix(matrix=matrix, target=130))


# #########  SIMPLIFIED  #########
# def search_in_matrix(matrix, target):
#
#
#     if len(matrix) == 0:
#         return False
#
#     for column_index in range(len(matrix)):
#         for row_index in range(len(matrix[0])):
#             if matrix[column_index][row_index] == target:
#                 return column_index, row_index
#     return [-1, -1]
