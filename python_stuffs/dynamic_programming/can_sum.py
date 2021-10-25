def can_sum_brute(target_sum, numbers: list):
    """
    Time: O(n^m)
    Space: O(m)
    """

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        reminder = target_sum - num
        if can_sum_brute(reminder, numbers):
            return True

    return False


def can_sum_w_memo(target_sum, numbers, memo):
    """
    Time: O(n*m)
    Space: O(m)
    """
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    if target_sum in memo:
        return memo[target_sum]

    for num in numbers:
        reminder = target_sum - num
        memo[reminder] = can_sum_w_memo(reminder, numbers, memo)
        if memo[reminder]:
            return True
    memo[target_sum] = False
    return False



if __name__ == "__main__":

    # print(can_sum_brute(7, [2, 3]))
    # print(can_sum_brute(7, [5, 3, 3, 7]))
    # print(can_sum_brute(7, [2, 4]))
    # print(can_sum_brute(8, [2, 3, 5]))
    # print(can_sum_brute(300, [7,14]))

    print('-'*88)

    # print(can_sum_w_memo(7, [2, 3], {}))
    # print(can_sum_w_memo(7, [5, 3, 3, 7], {}))
    # print(can_sum_w_memo(7, [2, 4], {}))
    # print(can_sum_w_memo(8, [2, 3, 5], {}))
    print(can_sum_w_memo(300, [7,14], {}))
