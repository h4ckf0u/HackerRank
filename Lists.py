if __name__ == '__main__':
    N = int(input())
    arr = list()
    for _ in range(N):
        command, *args = input().split()
        arg = list(map(int, args))

        if command == "insert":
            i = arg[0]
            x = arg[1]
            arr.insert(i,x)
        if command == "remove":
            x = arg[0]
            arr.remove(x)
        if command == "append":
            x = arg[0]
            arr.append(x)
        if command == "sort":
            arr.sort()
        if command == "pop":
            arr.pop()
        if command == "reverse":
            arr.reverse()
        elif command == "print":
            print(arr)





