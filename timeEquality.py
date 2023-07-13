lst = list(map(int, input().split()))
def Time_To_Equality(lst):
    maxElement = float('-inf')
    for ele in lst:
        if ele > maxElement:
            maxElement = ele
    res = 0
    for ele in lst:
        res += (maxElement - ele)
    return res
print(Time_To_Equality([2, 4, 1, 3, 2]))
print(Time_To_Equality(lst))
