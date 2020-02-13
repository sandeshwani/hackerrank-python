"""
You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.
"""

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    n = int(input("Enter n: "))
    #Solution A: without using list comprehensions in Python.
    print("**************Start of Solution A***********************")
    solutionA(x,y,n)
    print("--------------Start of Solution B-----------------------")
    #Solution B: with using list comprehensions in Python.
    solutionB(x,y,n)
    
    
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
    

if __name__ == '__main__':
    main()