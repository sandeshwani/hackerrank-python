'''
Solution 1: Simple list
'''

'''
if __name__ == '__main__':
    N = int(input())
    y = list()
    for _ in range(N):
        fullQuery = input().split(' ')
        command = fullQuery[0]
        if command == 'insert':
            y.insert(int(fullQuery[1]),int(fullQuery[2]))
        elif 'print' == command:
            print(y)
        elif 'remove' == command:
            y.remove(int(fullQuery[1]))
        elif 'append' == command:
            y.append(int(fullQuery[1]))
        elif 'sort' == command:
            y.sort()
        elif 'pop' == command:
            y.pop()
        elif 'reverse' == command:
            y.reverse()
'''

'''
Solution 2: Little complicated for starter. Using `eval`
'''
if __name__ == '__main__':
    N = int(input())
    y = list()
    for _ in range(N):
        fullQuery = input().split(' ')
        command = fullQuery[0]
        args = fullQuery[1:]
        if command != 'print':
            prepareCommand = "y." + command +  "(" + ",".join(args) + ")"
            eval(prepareCommand)
        else:
            print(y)
