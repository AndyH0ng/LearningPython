#
# * R R R
# C
# C
#
# Column-by-Row
#

# Array: Vector 자료구조
import numpy as np
x = np.array([1, 3, 5])
print(x)    # Result: [1 3 5]

y = np.array([2, 7, 3, 5])
print(y)    # Result: [2 7 3 5]

z = np.array([1, 0, 0])
t = x + z
print(z)    # Result: [2 3 5]



# Matrix 자료구조
A = np.array([ [1, 2, 3], [4, 5, 6] ])
print(A)    # Result: [[1 2 3]
            #          [4 5 6]] is two-by-three matrix

B = np.array([ [1, 4], [2, 5], [3, 6] ])
print(B)    # Result: [[1 4]
            #          [2 5]
            #          [3 6]] is three-by-two matrix

C = np.array([ [1, 2, 3] ])
print(C)    # Result: [[1 2 3]] is one-by-three matrix

D = np.array([1, 2, 3])
print(D)    # Result: [1 2 3] is array

E = np.arange(6).reshape((2, 3))
# arrange(6): 0부터 5까지 arrange
# reshape(2, 3): two-by-three matrix로 reshape
print(E)    # Result: [[0 1 2]
            #          [3 4 5]]

F = np.zeros((5, 4))
# zeros((5, 4)): five-by-four matrix로 0을 저장
print(F)    # Result: [[0 0 0 0]
            #          [0 0 0 0]
            #          [0 0 0 0]
            #          [0 0 0 0]
            #          [0 0 0 0]]

