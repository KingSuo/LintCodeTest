"""
描述
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。

符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

我们可以认为1也是一个丑数

样例
如果n = 9， 返回 10

挑战
要求时间复杂度为O(nlogn)或者O(n)
"""

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        
        low_2 = low_3 = low_5 = 0    
        list=[1]
        if n==1:
            return list[0]
        while len(list) < n:
            for i_2 in range(low_2,len(list)):
                n_2 = 2 * list[i_2]
                if n_2 > list[-1]:
                    break
            for i_3 in range(low_3,len(list)):
                n_3 = 3 * list[i_3]
                if n_3 > list[-1]:
                    break
            for i_5 in range(low_5,len(list)):
                n_5 = 5 * list[i_5]
                if n_5 > list[-1]:
                    break
            min_value = min(n_2, n_3, n_5)
            if min_value == n_2:
                low_2 = i_2
            elif min_value == n_3:
                low_3 = i_3
            else:
                low_5 = i_5
            list.append(min_value)
        return list[-1]

A
A
A
                
