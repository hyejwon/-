from itertools import combinations


def main():
    global n
    global k
    c = list(combinations(a, 3))
    total = set()
    for i in c:
        total.add(sum(i))
    final = list(total)
    final.sort(reverse=True)
    return print(final[k-1])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    main()
