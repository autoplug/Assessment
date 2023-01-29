def ArrayChallenge(arr):
    s_arr = sorted(arr, reverse=True)
    right = [s_arr[0]]
    left = [s_arr[1]]
    result = []
    for i in range(2, len(s_arr)-1, 2):
        if sum(right) < sum(left):
            right.append(s_arr[i])
            left.append(s_arr[i+1])
        else:
            right.append(s_arr[i+1])
            left.append(s_arr[i])
    if sum(right) != sum(left):
        return '-1'
    right.sort()
    left.sort()
    if right[0] < left[0]:
        result = right + left
    else:
        result = left + right

    challenge_token = "61h20g4oca"
    final_output = ','.join(map(str, result))
    concatenated_string = final_output + challenge_token

    for i in range(2, len(concatenated_string), 3):
        concatenated_string = concatenated_string[:i] + \
            "X" + concatenated_string[i+1:]
    return concatenated_string
