def efficientJanitor(weight):
    l = len(weight)
    start = 0
    end = l - 1
    count = 0
    while start < end:
        # print("inside while")
        if weight[start] + weight[end] <= 3:
            count += 1
            start = start + 1
            end = end - 1
        elif weight[start] + weight[end] > 3:
            count += 1
            end = end - 1
        if start == end:
            count += 1
    return int(count)


n = int(input())
w = [float(i) for i in input().split(" ")]
w = sorted(w)
print(efficientJanitor(w))
