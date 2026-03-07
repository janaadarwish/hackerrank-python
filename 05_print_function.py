if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")
# The end="" argument in the print function prevents it from adding a newline after each number, allowing them to be printed on the same line.