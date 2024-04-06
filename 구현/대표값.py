def main():
    global n
    global a
    aver = round(sum(a)/len(a))
    diffs = []
    for i in a:
        # 평균 차 계산
        diff = abs(i-aver)
        diffs.append(diff)

    min_score = min(diffs)
    scores = dict(zip(a, diffs))

    for k, v in scores.items():
        if k == min_score:
            print(v)



    return aver, scores


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    average, stu_id = main()
    print(average, stu_id)
