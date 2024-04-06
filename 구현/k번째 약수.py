# k번째 약수

def main():
    global n
    global k
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
        else:
            pass

    if len(a) > k:
        print(a[k - 1])
    else:
        print(-1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    main()