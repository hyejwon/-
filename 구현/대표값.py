def main():
    aver = round(sum(a)/len(a))
    score = 0
    res = 0
    min_ = 2147000000
    for i, x in enumerate(a):
        # 평균 차 계산
        diff = abs(x-aver)
        if diff < min_:
            min_ = diff
            score = x
            res = i+1  # 현재 학생 번호
        elif diff == min_:
            if x > score:
                score = x
                res = i+1
    return aver, res


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    average, stu_id = main()
    print(average, stu_id)
