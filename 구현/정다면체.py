from collections import Counter
# import sys
# sys.stdin = open("input.txt", "r")


def main(n, m):
    # n 면체 눈의 합
    sum_l = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum_l.append(i+j)
    counts = Counter(sum_l)
    max_value = max(counts.values())
    answer = []
    for k, v in counts.items():
        if v == max_value:
            answer.append(k)
    return print(*answer, sep=" ")


if __name__ == "__main__":
    n, m = map(int, input().split())
    main(n, m)
    # answer = main()
    # print(answer)


# 다른 풀이
# cnt = [0]*(n+m+3)
# max = -2147000000
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         cnt[i+j] += 1
# for i in range(n+m+1):
#     if cnt[i] > max:
#         max = cnt[i]
# for i in range(n+m+1):
#     if cnt[i] == max:
#         print(i, end=' ')
# print()
