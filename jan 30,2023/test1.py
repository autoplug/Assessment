# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    count = 0
    similar = 1
    similar_list = []
    for idx in range(1, len(S)):
        if S[idx] == S[idx-1]:
            similar += 1
        elif similar > 2:
            similar_list.append(similar)
            similar = 1
        else:
            similar = 1
    similar_list.append(similar)
    for item in similar_list:
        count += item//3
    return count
