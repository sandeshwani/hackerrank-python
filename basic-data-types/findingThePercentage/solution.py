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
        ## as line contains multiple vaule, we use *
        ##Single asterisk as used in function declaration allows variable number of arguments passed from calling environment. Inside the function it behaves as a tuple.
        ## https://www.tutorialspoint.com/What-does-the-Star-operator-mean-in-Python
        ##line is a list
            name, *line = input().split()
            #We convert the list that is in variable line to float using map function.
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()

        if query_name in student_marks:
            total = sum(student_marks[query_name])
            avg = total/(len(student_marks[query_name]))
            print(f"{avg:.2f}")

if __name__ == '__main__':
    e = Solution
    e.solve()
