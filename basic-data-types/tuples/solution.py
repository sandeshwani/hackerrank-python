if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    a = list(a)
    z = tuple(a)
    print(hash(z))
