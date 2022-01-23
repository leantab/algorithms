memo = {}


def canConstructString(target, list):
    if target == '':
        return True

    if target in memo:
        return memo[target]

    for word in list:
        if target.startswith(word):
            sufix = target.lstrip(word)
            rec = canConstructString(sufix, list)
            memo[sufix] = rec
            if rec:
                return True
    return False


print(canConstructString(
    'abcdef',
    ['ab', 'abc', 'cd', 'cde', 'def', 'ef', 'abcd'])
)

print(canConstructString(
    'skateboard',
    ['sk', 'skat', 'bo', 'te', 't', 'boar', 'ateb'])
)
