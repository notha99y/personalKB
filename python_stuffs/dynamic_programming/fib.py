def fib_recursive(n):
    if n <= 2:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_recursive_w_memo(n, memo: dict):

    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib_recursive_w_memo(n - 1, memo) + fib_recursive_w_memo(
        n - 2, memo
    )
    return memo[n]


if __name__ == "__main__":
    # print(fib_recursive(0))
    # print(fib_recursive(1))
    # print(fib_recursive(7))
    # print(fib_recursive(50))

    print(fib_recursive_w_memo(0, {}))
    print(fib_recursive_w_memo(1, {}))
    print(fib_recursive_w_memo(7, {}))
    print(fib_recursive_w_memo(50, {}))
