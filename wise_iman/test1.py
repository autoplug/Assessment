def solution(requests):
    result = []
    result.append(200)
    for i in range(1, len(requests)):
        if requests[max(i-5, 0):i].count(requests[i]) >= 2:
            result.append(400)
            requests[i] = ""
            continue
        if requests[max(i-30, 0):i].count(requests[i]) >= 5:
            result.append(400)
            requests[i] = ""
            continue
        result.append(200)
    return result


# print(solution(["a", "a", "a", "a"]))
print(solution(["x", "a", "x", "p", "a", "x", "x", "a", "x"]))
print("abc"[0:0])
