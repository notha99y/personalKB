def how_sum_brute(target_sum, numbers: list):
    """
    m: target_sum
    n: len(numbers)

    Time: O(n^m * m) because of the for loop to create new_remainder_result
    Space: O(m) call stack is just the depth of the tree for this case
    """
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum_brute(remainder, numbers)
        if remainder_result is not None:
            new_remainder_result = []
            for i in remainder_result:
                new_remainder_result.append(i)
            new_remainder_result.append(num)
            return new_remainder_result

    return None


def how_sum_w_memo(target_sum, numbers: list, memo: dict):
    """
    Time: O(n*m^2)
    Space: O(m^2) because memo now is storing a list which can hae a max of the len(m)
    """
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    if target_sum in memo:
        return memo[target_sum]

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum_w_memo(remainder, numbers, memo)

        if remainder_result is not None:
            new_remainder_result = []
            for i in remainder_result:
                new_remainder_result.append(i)
            new_remainder_result.append(num)
            memo[remainder] = new_remainder_result

            return new_remainder_result
    memo[target_sum] = None
    return None


if __name__ == "__main__":
    print(how_sum_brute(7, [2, 3]))
    print(how_sum_brute(7, [5, 3, 4, 7]))
    print(how_sum_brute(7, [2, 4]))
    print(how_sum_brute(8, [2, 3, 5]))
    print('-'*88)
    print(how_sum_w_memo(7, [2, 3], {}))
    print(how_sum_w_memo(7, [5, 3, 4, 7], {}))
    print(how_sum_w_memo(7, [2, 4], {}))
    print(how_sum_w_memo(8, [2, 3, 5], {}))
    print(how_sum_w_memo(30, [2, 3, 5], {}))
