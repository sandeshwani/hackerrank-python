"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

Marks for Malika are  whose average is 

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50
"""

class Solution:
    
    @staticmethod
    def solve():
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            #Other way of taking the input is below
            """singleLine = input().split()
            name, line = singleLine[0], singleLine[1:]"""
            scores = list(map(float,line))
            student_marks[name] = scores
        query_name = str(input())
        if student_marks.__contains__(query_name):
            x = student_marks.get(query_name)
            total = sum(x)
            avg = total/3
            print('%.2f' %avg)
            #print("{0:.2f}".format(avg))
        else:
            print("%s not found" %query_name)
    
if __name__ == '__main__':
    e = Solution
    e.solve()