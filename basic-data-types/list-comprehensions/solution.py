"""
https://www.hackerrank.com/challenges/list-comprehensions/problem
You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.
"""

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    n = int(input("Enter n: "))
    #Solution A: without using list comprehensions in Python.
    print("**************Start of Solution A***********************")
    solutionA(x,y,n)
    print()
    print("--------------Start of Solution B-----------------------")
    #Solution B: with using list comprehensions in Python.
    solutionB(x,y,n)
    print()
    #Solution C: without using list comprehensions in Python.
    print("//////////////Start of Solution C///////////////////////")
    solutionC(x,y,z,n)
    print()
    print("++++++++++++++Start of Solution D+++++++++++++++++++++++")
    #Solution D: with using list comprehensions in Python.
    solutionD(x,y,z,n)
    print()
    print("++++++++++++++Start of Solution E+++++++++++++++++++++++")
    #Solution E: Simple for loops in python. Added most recently on 25th July 2022
    solutionE(x,y,z,n)
    print()
    print("++++++++++++++Start of Solution f+++++++++++++++++++++++")
    #Solution F: Using list comprehensions. Added most recently on 25th July 2022
    solutionF(x,y,z,n)
    print()

def solutionA(x,y,n):
    ar = []
    p = 0
    for i in range(x+1):
        for j in range(y+1):
            if i + j != n:
                ar.append([])
                ar[p] = [i,j]
                p += 1
    print(ar)

def solutionB(x,y,n):
    result = [[i,j] for i in range(x+1) for j in range(y+1) if (i + j) != n ]
    print(result)


def solutionC(x,y,z,n):
    ar = []
    p = 0
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    ar.append([])
                    ar[p] = [i,j,k]
                    p += 1
    print(ar)

def solutionD(x,y,z,n):
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n ]
    print(result)

def solutionE(x,y,z,n):
    mylist = list()
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if i+j+k != n:
                    mylist.append([i,j,k])
    print(mylist)

def solutionF(x,y,z,n):
    mylist = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
    print(mylist)


if __name__ == '__main__':
    main()
