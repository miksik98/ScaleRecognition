def levenshtein(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if a[0] == b[0]:
        return levenshtein(a[1:], b[1:])
    return 1 + min(levenshtein(a[1:], b[1:]), min(levenshtein(a, b[1:]), levenshtein(a[1:], b)))

