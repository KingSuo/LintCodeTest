"""
描述
合并两个排序的整数数组A和B变成一个新的数组。

样例
给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

挑战
你能否优化你的算法，如果其中一个数组很大而另一个数组很小？
"""

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        
        if A[0] >= B[-1]:
            return B + A 
        elif A[-1] <= B[0]:
            return A + B
        else:
            j = 0
            new_arr = []
            if len(A) >= len(B):
                for i in range(len(B)):
                    while B[i] >= A[j]:
                        new_arr.append(A[j])
                        if j == len(A) - 1:
                            return new_arr + B[i:]
                        j += 1
                    if B[i] < A[j]:
                        new_arr.append(B[i])
                return new_arr + A[j:]
            else:
                for i in range(len(A)):
                    while A[i] >= B[j]:
                        new_arr.append(B[j])
                        if j == len(B) - 1:
                            return new_arr + A[i:]
                        j += 1
                    if A[i] < B[j]:
                        new_arr.append(A[i])
                return new_arr + B[j:]

class Solution2:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        
        if A[0] >= B[-1]:
            return B + A 
        elif A[-1] <= B[0]:
            return A + B
        else:
            i = j = 0
            new_arr = []
            if len(A) >= len(B):
                while i < len(B):
                    last_j = j
                    while B[i] >= A[j]:
                        if j == len(A) - 1:
                            new_arr += A[last_j:]
                            return new_arr + B[i:]
                        j += 1
                    new_arr += A[last_j:j]
                    last_i = i
                    while B[i] < A[j]:
                        if i == len(B) - 1:
                            new_arr += B[last_i:]
                            return new_arr + A[j:]
                        i += 1
                    new_arr += B[last_i:i]
                return new_arr + A[j:]
            else:
                while i < len(A):
                    last_j = j
                    while A[i] >= B[j]:
                        if j == len(B) - 1:
                            new_arr += B[last_j:]
                            return new_arr + A[i:]
                        j += 1
                    new_arr += B[last_j:j]
                    last_i = i
                    while A[i] < B[j]:
                        if i == len(A) - 1:
                            new_arr += A[last_i:]
                            return new_arr + B[j:]
                        i += 1
                    new_arr += A[last_i:i]
                return new_arr + B[j:]

A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
                                
