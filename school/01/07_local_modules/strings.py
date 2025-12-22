def remove_substring(text: str, substring: str) -> str:
    if not substring:
        return text

    result = ""
    i = 0

    while i < len(text):
        matched = True
        for j in range(len(substring)):
            if i + j >= len(text) or text[i + j] != substring[j]:
                matched = False
                break

        if matched:
            i += len(substring)
        else:
            result += text[i]
            i += 1

    return result
