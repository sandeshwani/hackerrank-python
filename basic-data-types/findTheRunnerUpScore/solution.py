"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains . The second line contains an array   of  integers each separated by a space.
Constraints


Output Format
Print the runner-up score.
Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
Explanation 0
Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""

class Solution:
    
    def solve(self):
        n = int(input())
        arr = map(int, input().split())
        l = list(arr)
        logic(l)

    def logic(self,l):
        max = -101
        for i in l:
            if max < i:
                max = i
        secondMax = -101
        for i in l:
            if secondMax < i & i != max:
                secondMax = i
        print(secondMax)
    
if __name__ == '__main__':
    e = Solution
    e.solve()