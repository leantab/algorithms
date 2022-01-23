def lcs(list):
    if len(list) == 0:
        return 0
    sums = [0]*(len(list))
    for i in range(0, len(list)):
        if i == 0:
            sums[i] = list[i]
            start_index = i
            last_index = i
            continue
        new_sum = sums[i-1] + list[i]
        if new_sum > list[i]:
            sums[i] = new_sum
        else:
            sums[i] = list[i]

    return max(sums)


print(lcs([-1, 5, -3, 4, 2, -4, 5]))
print(lcs([]))
print(lcs([-1, 5, -3, 1, 2, -4, -5]))
