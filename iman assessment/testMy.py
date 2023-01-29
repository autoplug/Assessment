def StringChallenge(strParam):
    tags = ["div", "i", "b", "em", "p"]
    result = {}
    for tag in tags:
        if strParam.count(f"<{tag}>") != strParam.count(f"</{tag}>"):
            if f"<{tag}>" in strParam:
                result[tag] = strParam.index(f"<{tag}>")
            elif f"</{tag}>" in strParam:
                result[tag] = strParam.index(f"</{tag}>")
    r = 10000000000
    k = ""

    for key in result:
        if result[key] < r:
            r = result[key]
            k = key

    challenge_token = "61h20g4oca"
    final_output = f"{k}"
    # Concatenate the final output and challenge token
    concatenated_string = final_output + challenge_token
    print(result)
# Replace every third character with "X"
    for i in range(2, len(concatenated_string), 3):
        concatenated_string = concatenated_string[:i] + \
            "X" + concatenated_string[i+1:]

    # code goes here
    return concatenated_string if k else "true"


# keep this function call here
print(StringChallenge("<div><div><b></b></div></p>"))
